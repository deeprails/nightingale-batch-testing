import os
import json
import glob
import argparse
import gspread
from datetime import datetime
from src.config import NUM_READINESS_ITEMS, NUM_MASTERY_ITEMS, FPS, VIDEO_TYPE_NAME

# Google Sheets configuration
SPREADSHEET_ID = "1xOUzw7SOaqE3QolG8ybSfOQ--GgStPIVs-aC08NPBDc"
SHEET_NAME = "AI Prompt Eng. Log (NEW)"


def get_sheets_client():
    return gspread.service_account(filename='service_account.json')


def find_first_empty_row(worksheet, check_col='C'):
    """Find the first empty row by checking column C."""
    col_values = worksheet.col_values(ord(check_col) - ord('A') + 1)
    return len(col_values) + 1


def extract_score_and_rationale(grading_string):
    """Extract score and rationale from a grading result string."""
    if not grading_string:
        return None, None
    score = None
    rationale = None
    lines = grading_string.split('\n')
    for line in lines:
        if line.startswith('Score:'):
            score = line.replace('Score:', '').strip()
        elif line.startswith('Rationale:'):
            rationale = line.replace('Rationale:', '').strip()
    return score, rationale


def extract_eval_verdicts(eval_string):
    """Extract score_verdict, rationale_verdict, and reasoning from eval string."""
    if not eval_string:
        return None, None, None
    score_verdict = None
    rationale_verdict = None
    reasoning = None
    lines = eval_string.split('\n')
    for line in lines:
        if line.startswith('Score Agreed?:'):
            score_verdict = line.replace('Score Agreed?:', '').strip()
        elif line.startswith('Rationale Agreed?:'):
            rationale_verdict = line.replace('Rationale Agreed?:', '').strip()
        elif line.startswith('Reasoning:'):
            reasoning = line.replace('Reasoning:', '').strip()
    return score_verdict, rationale_verdict, reasoning


def convert_grader_score(score, is_round_1=True):
    if score is None or score == "":
        return "N/A" if not is_round_1 else ""
    score_map = {
        "Not Demonstrated": "NOT DEMONSTRATED",
        "Fail": "DOES NOT MEET STANDARD",
        "Pass": "MEETS STANDARD"
    }
    return score_map.get(score, score)


def convert_eval_score_verdict(verdict, was_evaluated):
    if not was_evaluated:
        return "EVAL NOT NEEDED"
    if verdict is None or verdict == "":
        return ""
    if str(verdict).lower() == "true":
        return "GRADER SCORE CORRECT"
    elif str(verdict).lower() == "false":
        return "GRADER SCORE INCORRECT"
    return verdict


def convert_eval_rationale_verdict(verdict, was_evaluated):
    if not was_evaluated:
        return "EVAL NOT NEEDED"
    if verdict is None or verdict == "":
        return ""
    if str(verdict).lower() == "true":
        return "GRADER RATIONALE CORRECT"
    elif str(verdict).lower() == "false":
        return "GRADER RATIONALE INCORRECT"
    return verdict


def convert_judge_score(score):
    if score is None or score == "":
        return "N/A"
    score_map = {
        "Not Demonstrated": "NOT DEMONSTRATED",
        "Fail": "DOES NOT MEET STANDARD",
        "Pass": "MEETS STANDARD"
    }
    return score_map.get(score, score)


def flatten_data(data):
    """
    Combine readiness and mastery data into single lists, **aligned by rubric item**.

    We do not assume that the per-phase reporting lists (e.g. grading_strings_r2)
    are full length; instead we align them against the grade arrays, filling in
    sensible defaults when a particular item/round was never run.
    """
    if not data.get("readiness_data") or not data.get("mastery_data"):
        return None  # Incomplete data

    rd = data["readiness_data"] or {}
    md = data["mastery_data"] or {}

    readiness_grades = data.get("readiness_grades", [])
    mastery_grades = data.get("mastery_grades", [])

    num_readiness = len(readiness_grades)
    num_mastery = len(mastery_grades)
    total_items = num_readiness + num_mastery

    keys = [
        "grading_strings_r1", "grading_tokens_r1",
        "eval_strings_r1", "eval_tokens_r1",
        "grading_strings_r2", "grading_tokens_r2",
        "eval_strings_r2", "eval_tokens_r2",
        "judge_rationales", "judge_tokens",
    ]

    # Helper to safely pull a value for a given item index, falling back
    # to an appropriate "empty" default when the list is missing/short.
    def get_item(src, key, idx):
        seq = src.get(key, [])
        if idx < len(seq):
            return seq[idx]
        # Default based on key type
        if "tokens" in key:
            return (0, 0)
        return ""

    flat = {k: [] for k in keys}
    flat["grades"] = []

    for global_idx in range(total_items):
        if global_idx < num_readiness:
            src = rd
            local_idx = global_idx
            grade = readiness_grades[local_idx]
        else:
            src = md
            local_idx = global_idx - num_readiness
            grade = mastery_grades[local_idx]

        flat["grades"].append(grade)
        for k in keys:
            flat[k].append(get_item(src, k, local_idx))

    return flat


def upload_results(json_dir, spreadsheet_id, sheet_name):
    client = get_sheets_client()
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)

    json_files = glob.glob(os.path.join(json_dir, "*.json"))
    print(f"Found {len(json_files)} JSON result files.")

    start_row = find_first_empty_row(worksheet, 'C')
    print(f"Starting upload at row {start_row}")

    rows_to_upload = []
    # Track chunks for merging: list of (start_row, end_row, num_items) for each chunk (readiness/mastery)
    chunk_groups = []
    current_row_offset = 0

    for jf in json_files:
        with open(jf, 'r') as f:
            data = json.load(f)

        if data["status"] != "Complete" and data["status"] != "Failed Readiness":
            print(f"Skipping {data['video_uri']}: Status is {data['status']}")
            continue

        flat = flatten_data(data)
        if not flat:
            print(f"Skipping {data['video_uri']}: Missing detailed data.")
            continue

        print(f"Processing {data['video_uri']}...")

        num_readiness = len(data["readiness_grades"])
        num_mastery = len(data["mastery_grades"])
        total_items = num_readiness + num_mastery

        # Track readiness and mastery chunks separately for merging
        if num_readiness > 0:
            readiness_start = start_row + current_row_offset
            readiness_end = readiness_start + num_readiness - 1
            chunk_groups.append(
                (readiness_start, readiness_end, num_readiness))

        if num_mastery > 0:
            mastery_start = start_row + current_row_offset + num_readiness
            mastery_end = mastery_start + num_mastery - 1
            chunk_groups.append((mastery_start, mastery_end, num_mastery))

        for i in range(total_items):
            # Extract all the fields
            g_string_r1 = flat["grading_strings_r1"][i]
            g_tokens_r1 = flat["grading_tokens_r1"][i]
            e_string_r1 = flat["eval_strings_r1"][i]
            e_tokens_r1 = flat["eval_tokens_r1"][i]
            g_string_r2 = flat["grading_strings_r2"][i]
            g_tokens_r2 = flat["grading_tokens_r2"][i]
            e_string_r2 = flat["eval_strings_r2"][i]
            e_tokens_r2 = flat["eval_tokens_r2"][i]
            j_rationale = flat["judge_rationales"][i]
            j_tokens = flat["judge_tokens"][i]
            grades = flat["grades"][i]  # [g1, g2, judge]

            # Round 1 Grader
            r1_score_raw, r1_rationale = extract_score_and_rationale(
                g_string_r1)
            r1_score = convert_grader_score(r1_score_raw, True)

            # Round 1 Evaluator
            r1_was_evaluated = bool(e_string_r1)
            r1_eval_score_raw, r1_eval_rat_raw, r1_eval_reason = extract_eval_verdicts(
                e_string_r1)
            r1_eval_score = convert_eval_score_verdict(
                r1_eval_score_raw, r1_was_evaluated)
            r1_eval_rat = convert_eval_rationale_verdict(
                r1_eval_rat_raw, r1_was_evaluated)

            # Round 2 Grader
            r2_score_raw, r2_rationale = extract_score_and_rationale(
                g_string_r2)
            r2_score = convert_grader_score(r2_score_raw, False)

            # Round 2 Evaluator
            r2_was_evaluated = bool(e_string_r2)
            r2_eval_score_raw, r2_eval_rat_raw, r2_eval_reason = extract_eval_verdicts(
                e_string_r2)
            r2_eval_score = convert_eval_score_verdict(
                r2_eval_score_raw, r2_was_evaluated)
            r2_eval_rat = convert_eval_rationale_verdict(
                r2_eval_rat_raw, r2_was_evaluated)

            # Judge
            r3_score = convert_judge_score(grades[2])
            r3_rationale = j_rationale

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Ensure tokens are lists/tuples and handle None
            def get_tok(t, idx):
                if not t:
                    return ""
                return t[idx] if t[idx] > 0 else ""

            # Extract video ID from URI
            video_uri = data['video_uri']
            video_id = ""
            parts = video_uri.split('_')
            if len(parts) >= 2:
                video_id = parts[1]

            prompt_id = data['prompt_id']

            row = [
                i + 1,
                timestamp,
                prompt_id,
                VIDEO_TYPE_NAME,
                video_id,
                "",  # Tokens Consumed (computed)
                FPS,
                "",  # CODE DUMP
                "",  # Stage Consensus Reached
                "",  # FINAL SCORE
                "",  # FINAL SCORE - AI-ENG. CHECK
                "",  # FINAL SCORE - AI-ENG. SCORE
                r1_score,
                r1_rationale or "",
                get_tok(g_tokens_r1, 0),
                get_tok(g_tokens_r1, 1),
                r1_eval_score,
                r1_eval_rat,
                r1_eval_reason or "",
                get_tok(e_tokens_r1, 0),
                get_tok(e_tokens_r1, 1),
                "",  # R1 CHECK
                "",  # R1 SCORE
                "",  # R1 COMMENTS
                r2_score,
                r2_rationale or "",
                get_tok(g_tokens_r2, 0),
                get_tok(g_tokens_r2, 1),
                r2_eval_score,
                r2_eval_rat,
                r2_eval_reason or "",
                get_tok(e_tokens_r2, 0),
                get_tok(e_tokens_r2, 1),
                "",  # R2 CHECK
                "",  # R2 SCORE
                "",  # R2 COMMENTS
                r3_score,
                r3_rationale,
                get_tok(j_tokens, 0),
                get_tok(j_tokens, 1),
                "",  # R3 CHECK
                "",  # R3 SCORE
                "",  # R3 COMMENTS
            ]
            rows_to_upload.append(row)

        current_row_offset += total_items

    if rows_to_upload:
        print(f"Uploading {len(rows_to_upload)} rows...")
        # Batch update to optimize
        # Using batch_update logic from notebook (cell updates) is safer for preserving existing data in other columns
        # But if we are appending to new rows, we can just use append_rows or update range.
        # Notebook used batch_update with specific ranges.

        merge_columns = [4, 12, 13, 17, 18, 23, 24, 28, 29, 34, 35]

        cell_updates = []
        for row_idx, row in enumerate(rows_to_upload):
            actual_row = start_row + row_idx
            for col_idx, value in enumerate(row):
                # Skip merge columns for non-first rows of a video group
                if col_idx in merge_columns:
                    # Check if this is the first row of a chunk (readiness/mastery)
                    is_first_row_of_chunk = False
                    for (grp_start, grp_end, _) in chunk_groups:
                        if actual_row == grp_start:
                            is_first_row_of_chunk = True
                            break
                    if not is_first_row_of_chunk:
                        continue  # Skip this cell, it will be merged

                if value != "" and value is not None:
                    # Convert column index to letter (A-Z, then AA, AB, etc.)
                    if col_idx < 26:
                        col_letter = chr(ord('A') + col_idx)
                    else:
                        col_letter = chr(ord('A') + col_idx //
                                         26 - 1) + chr(ord('A') + col_idx % 26)
                    cell_updates.append({
                        'range': f"{col_letter}{actual_row}",
                        'values': [[value]]
                    })

        # Split into chunks to avoid hitting limits if many rows
        CHUNK_SIZE = 5000
        for i in range(0, len(cell_updates), CHUNK_SIZE):
            chunk = cell_updates[i:i+CHUNK_SIZE]
            worksheet.batch_update(chunk)
            print(f"Uploaded chunk {i//CHUNK_SIZE + 1}")

        # Now merge cells for token columns per chunk (readiness/mastery)
        # Build all merge requests and send in a single batch
        print("Merging token cells...")
        merge_requests = []
        for (grp_start, grp_end, num_items) in chunk_groups:
            if num_items > 1:  # Only merge if more than 1 row
                for col_idx in merge_columns:
                    merge_requests.append({
                        'mergeCells': {
                            'range': {
                                'sheetId': worksheet.id,
                                'startRowIndex': grp_start - 1,  # 0-indexed
                                'endRowIndex': grp_end,          # exclusive
                                'startColumnIndex': col_idx,
                                'endColumnIndex': col_idx + 1    # exclusive
                            },
                            'mergeType': 'MERGE_ALL'
                        }
                    })

        if merge_requests:
            spreadsheet.batch_update({'requests': merge_requests})

        print("Upload complete.")
    else:
        print("No rows to upload.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="results",
                        help="Directory containing JSON results")
    parser.add_argument("--sheet_id", default=SPREADSHEET_ID,
                        help="Google Sheet ID")
    parser.add_argument("--sheet_name", default=SHEET_NAME,
                        help="Worksheet Name")
    args = parser.parse_args()

    upload_results(args.dir, args.sheet_id, args.sheet_name)
