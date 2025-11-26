import os
import json
import hashlib
import concurrent.futures
import argparse
from datetime import datetime
from src.config import (
    NUM_READINESS_ITEMS, NUM_MASTERY_ITEMS, RUBRIC_ITEMS, 
    PROMPT_1, PROMPT_2, PROMPT_3, PROMPT_4, PROMPT_5, PROMPT_6, 
    PROMPT_7, PROMPT_8, PROMPT_9, PROMPT_10, PROMPT_11, PROMPT_12,
    EVALUATOR, REGRADER,
    NUM_READINESS_CHUNKS, NUM_MASTERY_CHUNKS, TTL_SECONDS
)
from src.api import get_credentials, cache_video
from src.workflow import grading, evaluation, judge

def process_video(video_uri, output_dir):
    """
    Full pipeline processing for a single video.
    Returns the result dictionary.
    """
    start_time = datetime.now()
    print(f"[{start_time}] Starting processing for {video_uri}")
    
    try:
        credentials = get_credentials()
        
        # 1. Cache Video
        print(f"Caching {video_uri}...")
        cache_resp = cache_video(video_uri, TTL_SECONDS, credentials)
        cache_name = cache_resp.json()["name"]
        print(f"Cached {video_uri} as {cache_name}")
        
        # Initialize Result Containers
        all_readiness_grades = [[None, None, None] for _ in range(NUM_READINESS_ITEMS)]
        all_mastery_grades = [[None, None, None] for _ in range(NUM_MASTERY_ITEMS)]
        
        # Reporting Data Containers
        readiness_data = {
            "grading_strings_r1": [], "grading_tokens_r1": [],
            "eval_strings_r1": [], "eval_tokens_r1": [],
            "grading_strings_r2": [], "grading_tokens_r2": [],
            "eval_strings_r2": [], "eval_tokens_r2": [],
            "judge_strings": [""] * NUM_READINESS_ITEMS, 
            "judge_rationales": [""] * NUM_READINESS_ITEMS,
            "judge_tokens": [(0,0)] * NUM_READINESS_ITEMS
        }
        
        mastery_data = {
            "grading_strings_r1": [], "grading_tokens_r1": [],
            "eval_strings_r1": [], "eval_tokens_r1": [],
            "grading_strings_r2": [], "grading_tokens_r2": [],
            "eval_strings_r2": [], "eval_tokens_r2": [],
            "judge_strings": [""] * NUM_MASTERY_ITEMS, 
            "judge_rationales": [""] * NUM_MASTERY_ITEMS,
            "judge_tokens": [(0,0)] * NUM_MASTERY_ITEMS
        }

        readiness_rubric = RUBRIC_ITEMS[:NUM_READINESS_ITEMS]
        mastery_rubric = RUBRIC_ITEMS[NUM_READINESS_ITEMS:]
        
        # ==========================================
        # READINESS PHASE
        # ==========================================
        print(f"Starting Readiness Phase for {video_uri}")
        
        # Grading Round 1
        r_grading_prompts = [PROMPT_1, PROMPT_2]
        cache_name, r_grad_str_1, r_grades_1, r_tok_1 = grading(
            r_grading_prompts, readiness_rubric, True, 
            [True] * NUM_READINESS_ITEMS, cache_name, video_uri, credentials
        )
        readiness_data["grading_strings_r1"] = r_grad_str_1
        readiness_data["grading_tokens_r1"] = r_tok_1
        
        for i, g in enumerate(r_grades_1):
            all_readiness_grades[i][0] = g

        # Evaluation Round 1
        proceeds = [g != "Pass" for g in r_grades_1]
        r_eval_prompts = [EVALUATOR for _ in range(NUM_READINESS_CHUNKS)]
        cache_name, r_eval_str_1, r_agreements_1, r_eval_tok_1 = evaluation(
            r_eval_prompts, readiness_rubric, r_grad_str_1, True, 
            proceeds, cache_name, video_uri, credentials
        )
        readiness_data["eval_strings_r1"] = r_eval_str_1
        readiness_data["eval_tokens_r1"] = r_eval_tok_1
        
        # Regrading & Judging if needed
        r_redos = [not a for a in r_agreements_1]
        if any(r_redos):
            print(f"Regrading needed for Readiness items: {[i+1 for i, x in enumerate(r_redos) if x]}")
            r_regrade_prompts = [REGRADER for _ in range(NUM_READINESS_CHUNKS)]
            cache_name, r_grad_str_2, r_grades_2, r_tok_2 = grading(
                r_regrade_prompts, readiness_rubric, True, 
                r_redos, cache_name, video_uri, credentials
            )
            readiness_data["grading_strings_r2"] = r_grad_str_2
            readiness_data["grading_tokens_r2"] = r_tok_2
            
            # Update state
            r_proceeds_2 = []
            for i, g in enumerate(r_grades_2):
                if r_redos[i]:
                    all_readiness_grades[i][1] = g
                    r_proceeds_2.append(g != "Pass")
                else:
                    r_proceeds_2.append(False)

            # Evaluation Round 2
            cache_name, r_eval_str_2, r_agreements_2, r_eval_tok_2 = evaluation(
                r_eval_prompts, readiness_rubric, r_grad_str_2, True,
                r_proceeds_2, cache_name, video_uri, credentials
            )
            readiness_data["eval_strings_r2"] = r_eval_str_2
            readiness_data["eval_tokens_r2"] = r_eval_tok_2
            
            # Judge
            judge_needed = [not a for a in r_agreements_2]
            for i, needed in enumerate(judge_needed):
                if needed and r_redos[i]: # Only if it was regraded
                    print(f"Judging Readiness Item {i+1}...")
                    cache_name, j_str, j_score, j_rat, j_tok = judge(
                        cache_name, readiness_rubric[i],
                        r_grad_str_1[i], r_eval_str_1[i],
                        r_grad_str_2[i], r_eval_str_2[i],
                        video_uri, credentials
                    )
                    all_readiness_grades[i][2] = j_score
                    readiness_data["judge_strings"][i] = j_str
                    readiness_data["judge_rationales"][i] = j_rat
                    readiness_data["judge_tokens"][i] = j_tok

        # Check Readiness Pass/Fail
        readiness_passes = 0
        for i in range(NUM_READINESS_ITEMS):
            final = all_readiness_grades[i][2] or all_readiness_grades[i][1] or all_readiness_grades[i][0]
            if final == "Pass":
                readiness_passes += 1
        
        if readiness_passes / NUM_READINESS_ITEMS < 0.8:
            print(f"Readiness failed for {video_uri}. Skipping Mastery.")
            result = {
                "video_uri": video_uri,
                "status": "Failed Readiness",
                "readiness_grades": all_readiness_grades,
                "mastery_grades": [],
                "readiness_data": readiness_data,
                "mastery_data": mastery_data
            }
            _save_result(result, output_dir)
            return result

        # ==========================================
        # MASTERY PHASE
        # ==========================================
        print(f"Starting Mastery Phase for {video_uri}")
        
        m_grading_prompts = [PROMPT_3, PROMPT_4, PROMPT_5, PROMPT_6, PROMPT_7, PROMPT_8, PROMPT_9, PROMPT_10, PROMPT_11, PROMPT_12]
        cache_name, m_grad_str_1, m_grades_1, m_tok_1 = grading(
            m_grading_prompts, mastery_rubric, False,
            [True] * NUM_MASTERY_ITEMS, cache_name, video_uri, credentials
        )
        mastery_data["grading_strings_r1"] = m_grad_str_1
        mastery_data["grading_tokens_r1"] = m_tok_1
        
        for i, g in enumerate(m_grades_1):
            all_mastery_grades[i][0] = g
            
        # Evaluation Round 1
        m_eval_prompts = [EVALUATOR for _ in range(NUM_MASTERY_CHUNKS)]
        cache_name, m_eval_str_1, m_agreements_1, m_eval_tok_1 = evaluation(
            m_eval_prompts, mastery_rubric, m_grad_str_1, False,
            [True] * NUM_MASTERY_ITEMS, cache_name, video_uri, credentials
        )
        mastery_data["eval_strings_r1"] = m_eval_str_1
        mastery_data["eval_tokens_r1"] = m_eval_tok_1
        
        # Regrading
        m_redos = [not a for a in m_agreements_1]
        if any(m_redos):
            print(f"Regrading needed for Mastery items: {[i+1 for i, x in enumerate(m_redos) if x]}")
            m_regrade_prompts = [REGRADER for _ in range(NUM_MASTERY_CHUNKS)]
            cache_name, m_grad_str_2, m_grades_2, m_tok_2 = grading(
                m_regrade_prompts, mastery_rubric, False,
                m_redos, cache_name, video_uri, credentials
            )
            mastery_data["grading_strings_r2"] = m_grad_str_2
            mastery_data["grading_tokens_r2"] = m_tok_2
            
            m_proceeds_2 = []
            for i, g in enumerate(m_grades_2):
                if m_redos[i]:
                    all_mastery_grades[i][1] = g
                    m_proceeds_2.append(True)
                else:
                    m_proceeds_2.append(False)
                    
            # Evaluation Round 2
            cache_name, m_eval_str_2, m_agreements_2, m_eval_tok_2 = evaluation(
                m_eval_prompts, mastery_rubric, m_grad_str_2, False,
                m_proceeds_2, cache_name, video_uri, credentials
            )
            mastery_data["eval_strings_r2"] = m_eval_str_2
            mastery_data["eval_tokens_r2"] = m_eval_tok_2
            
            # Judge
            judge_needed = [not a for a in m_agreements_2]
            for i, needed in enumerate(judge_needed):
                if needed and m_redos[i]:
                    print(f"Judging Mastery Item {i+1}...")
                    cache_name, j_str, j_score, j_rat, j_tok = judge(
                        cache_name, mastery_rubric[i],
                        m_grad_str_1[i], m_eval_str_1[i],
                        m_grad_str_2[i], m_eval_str_2[i],
                        video_uri, credentials
                    )
                    all_mastery_grades[i][2] = j_score
                    mastery_data["judge_strings"][i] = j_str
                    mastery_data["judge_rationales"][i] = j_rat
                    mastery_data["judge_tokens"][i] = j_tok

        result = {
            "video_uri": video_uri,
            "status": "Complete",
            "readiness_grades": all_readiness_grades,
            "mastery_grades": all_mastery_grades,
            "readiness_data": readiness_data,
            "mastery_data": mastery_data
        }
        _save_result(result, output_dir)
        return result

    except Exception as e:
        print(f"ERROR processing {video_uri}: {str(e)}")
        result = {"video_uri": video_uri, "status": "Error", "error": str(e)}
        _save_result(result, output_dir)
        return result

def _save_result(result, output_dir):
    """Helper to save individual result to JSON safely."""
    # Generate a hash of the URI to ensure filename is short and unique
    uri_hash = hashlib.md5(result["video_uri"].encode("utf-8")).hexdigest()
    
    # Try to keep a recognizable prefix from the filename
    base_name = os.path.basename(result["video_uri"])
    # Sanitize: remove non-alphanumeric except typical file chars
    safe_base = "".join([c for c in base_name if c.isalnum() or c in ('-', '_', '.')])
    # Truncate prefix to avoid long paths (30 chars max)
    prefix = safe_base[:30]
    
    filename = f"{prefix}_{uri_hash}.json"
    path = os.path.join(output_dir, filename)
    
    try:
        with open(path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Saved result to {path}")
    except OSError as e:
        # Fallback to pure hash if somehow still too long or invalid
        fallback_path = os.path.join(output_dir, f"video_{uri_hash}.json")
        print(f"Failed to save to {path}, trying fallback {fallback_path}. Error: {e}")
        with open(fallback_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Saved result to {fallback_path}")

def main():
    parser = argparse.ArgumentParser(description="Batch Video Grader")
    parser.add_argument("--videos", nargs="+", help="List of GCS URIs to process")
    parser.add_argument("--file", help="File containing list of GCS URIs (one per line)")
    parser.add_argument("--output", default="results", help="Output directory for JSON results")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output):
        os.makedirs(args.output)
        
    video_list = []
    if args.videos:
        video_list.extend(args.videos)
    if args.file:
        with open(args.file, 'r') as f:
            video_list.extend([l.strip() for l in f if l.strip()])
            
    if not video_list:
        print("No videos provided. Use --videos or --file.")
        return

    print(f"Found {len(video_list)} videos to process.")
    print(f"Using {args.workers} parallel workers.")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_video, uri, args.output): uri for uri in video_list}
        
        for future in concurrent.futures.as_completed(futures):
            uri = futures[future]
            try:
                data = future.result()
                print(f"Finished {uri}: {data['status']}")
            except Exception as exc:
                print(f"{uri} generated an exception: {exc}")

if __name__ == "__main__":
    main()
