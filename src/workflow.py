import re
import json
from src.config import (
    NUM_READINESS_CHUNKS, NUM_MASTERY_CHUNKS, NUM_READINESS_ITEMS, NUM_MASTERY_ITEMS,
    readiness_item_to_prompt, mastery_item_to_prompt, JUDGE_PROMPT
)
from src.api import poll_vertex

def assemble_skeleton_prompts(skeletons, items, additional_info, previous_results, assemble_or_not, is_readiness):
    """Assembles the prompts by filling in the skeletons with rubric items."""
    # Validation
    if is_readiness:
        assert len(skeletons) == NUM_READINESS_CHUNKS
        assert len(items) == NUM_READINESS_ITEMS
        mapping = readiness_item_to_prompt
    else:
        assert len(skeletons) == NUM_MASTERY_CHUNKS
        assert len(items) == NUM_MASTERY_ITEMS
        mapping = mastery_item_to_prompt

    num_chunks = len(skeletons)
    items_for_prompts = [""] * num_chunks
    info_for_prompts = [""] * num_chunks
    results_for_prompts = [""] * num_chunks
    
    # Track which info has been added to which chunk to avoid duplication
    added_info_hashes = [set() for _ in range(num_chunks)]

    for i in range(len(items)):
        try:
            if assemble_or_not[i]:
                chunk_idx = mapping[i]
                items_for_prompts[chunk_idx] += "\n" + items[i]
                
                if additional_info is not None:
                    info_text = additional_info[i]
                    # Simple hash or just string check to avoid dupes in the same chunk
                    if info_text and info_text not in added_info_hashes[chunk_idx]:
                        info_for_prompts[chunk_idx] += "\n" + info_text
                        added_info_hashes[chunk_idx].add(info_text)
                        
                if previous_results is not None:
                    results_for_prompts[chunk_idx] += "\n" + previous_results[i]
        except IndexError as e:
            print(f"DEBUG: IndexError in assemble_skeleton_prompts at i={i}")
            print(f"DEBUG: len(items)={len(items)}")
            print(f"DEBUG: len(assemble_or_not)={len(assemble_or_not)}")
            print(f"DEBUG: len(mapping)={len(mapping)}")
            if additional_info is not None:
                print(f"DEBUG: len(additional_info)={len(additional_info)}")
            if previous_results is not None:
                print(f"DEBUG: len(previous_results)={len(previous_results)}")
            raise e

    finished_prompts = []
    for i in range(len(items_for_prompts)):
        # Only process chunks that have items
        if items_for_prompts[i] != "":
            item_pattern = re.escape(items_for_prompts[i])
            item_target = "{{{RUBRIC_ITEMS}}}"
            filled_skeleton = re.sub(item_target, item_pattern, skeletons[i])
            
            # Always try to replace INFO, even if empty (it will just remove the placeholder if info is empty string)
            info_target = "{{{INFO}}}"
            # If additional_info was None, info_for_prompts[i] is empty string, which is fine
            # But we need to make sure we don't leave {{{INFO}}} if it wasn't replaced
            info_pattern = re.escape(info_for_prompts[i])
            filled_skeleton = re.sub(info_target, info_pattern, filled_skeleton)
                
            if previous_results is not None:
                prev_target = "{{{PREVIOUS_RESULTS}}}"
                prev_pattern = re.escape(results_for_prompts[i])
                filled_skeleton = re.sub(prev_target, prev_pattern, filled_skeleton)
                
            finished_prompts.append(filled_skeleton)

    return finished_prompts

def grading(prompts, rubric_items, additional_info, is_readiness, assemble_or_not, cache_name, video_uri, credentials, temperature):
    """Runs the grading phase."""
    grading_schema = {
        "type": "object",
        "properties": {
            "scores": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "string", "enum": ["Not Demonstrated", "Fail", "Pass"]},
                        "rationale": {"type": "string"}
                    },
                    "required": ["score", "rationale"]
                }
            }
        },
        "required": ["scores"]
    }

    assembled_prompts = assemble_skeleton_prompts(prompts, rubric_items, additional_info, None, assemble_or_not, is_readiness)
    cache_name, responses = poll_vertex(assembled_prompts, grading_schema, cache_name, video_uri, credentials, temperature)

    # Process responses
    grading_scores = []
    
    for i, response in enumerate(responses):
        metadata = response.json().get("usageMetadata", {})
        total = metadata.get("totalTokenCount", 0)
        cached = metadata.get("cachedContentTokenCount", 0)
        
        candidates = response.json().get("candidates", [])
        if not candidates:
             raise ValueError("No candidates returned")
             
        output_text = candidates[0]["content"]["parts"][0]["text"]
        output_data = json.loads(output_text)
        
        for score in output_data["scores"]:
            # Attach token info to the score object temporarily for mapping
            score["_tokens"] = (total, cached)
            grading_scores.append(score)

    # Re-align with original items structure
    grading_result_strings = []
    scores = []
    token_data = []
    
    item_index = 0
    # Skip items not requested at start
    while item_index < len(assemble_or_not) and not assemble_or_not[item_index]:
        grading_result_strings.append("")
        scores.append(None)
        token_data.append((0, 0))
        item_index += 1

    score_idx = 0
    while score_idx < len(grading_scores):
        item = grading_scores[score_idx]
        effective_index = item_index + 1
        if not is_readiness:
            effective_index += NUM_READINESS_ITEMS
            
        result_string = f"Rubric item {effective_index}:\nScore: {item['score']}\nRationale: {item['rationale']}"
        grading_result_strings.append(result_string)
        scores.append(item["score"])
        
        # Retrieve tokens attached earlier
        token_data.append(item.get("_tokens", (0, 0)))
        
        score_idx += 1
        item_index += 1
        
        if item_index >= len(rubric_items):
            break
            
        # Fill gaps
        while item_index < len(assemble_or_not) and not assemble_or_not[item_index]:
            grading_result_strings.append("")
            scores.append(None)
            token_data.append((0, 0))
            item_index += 1

    return cache_name, grading_result_strings, scores, token_data

def evaluation(prompts, rubric_items, additional_info, grading_strings, is_readiness, assemble_or_not, cache_name, video_uri, credentials):
    """Runs the evaluation phase."""
    eval_schema = {
        "type": "object",
        "properties": {
            "verdicts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "score_verdict": {"type": "boolean"},
                        "rationale_verdict": {"type": "boolean"},
                        "reasoning": {"type": "string"}
                    },
                    "required": ["score_verdict", "rationale_verdict", "reasoning"]
                }
            }
        },
        "required": ["verdicts"]
    }

    eval_prompts = assemble_skeleton_prompts(prompts, rubric_items, additional_info, grading_strings, assemble_or_not, is_readiness)
    cache_name, responses = poll_vertex(eval_prompts, eval_schema, cache_name, video_uri, credentials, temperature=1.0)

    eval_verdicts = []
    for response in responses:
        metadata = response.json().get("usageMetadata", {})
        total = metadata.get("totalTokenCount", 0)
        cached = metadata.get("cachedContentTokenCount", 0)

        candidates = response.json().get("candidates", [])
        if not candidates:
            raise ValueError("No candidates")
        output_text = candidates[0]["content"]["parts"][0]["text"]
        output_data = json.loads(output_text)
        for verdict in output_data["verdicts"]:
            verdict["_tokens"] = (total, cached)
            eval_verdicts.append(verdict)

    agreements = [True] * len(rubric_items)
    eval_strings = []
    token_data = []
    
    item_index = 0
    verdict_idx = 0
    
    while item_index < len(assemble_or_not):
        if not assemble_or_not[item_index]:
            eval_strings.append("")
            token_data.append((0, 0))
            item_index += 1
            continue
            
        if verdict_idx >= len(eval_verdicts):
            break
            
        item = eval_verdicts[verdict_idx]
        effective_index = item_index + 1
        if not is_readiness:
            effective_index += NUM_READINESS_ITEMS
            
        eval_string = f"Rubric item {effective_index}\nScore Agreed?: {item['score_verdict']}\nRationale Agreed?: {item['rationale_verdict']}\nReasoning: {item['reasoning']}"
        eval_strings.append(eval_string)
        
        is_agreed = item["score_verdict"] and item["rationale_verdict"]
        agreements[item_index] = is_agreed
        token_data.append(item.get("_tokens", (0, 0)))
        
        verdict_idx += 1
        item_index += 1

    return cache_name, eval_strings, agreements, token_data

def assemble_judge(item, g1, e1, g2, e2, info):
    filled = re.sub("{{{RUBRIC_ITEM}}}", re.escape(item), JUDGE_PROMPT)
    filled = re.sub("{{{GRADER_1_OUTPUT}}}", re.escape(g1), filled)
    filled = re.sub("{{{EVALUATOR_1_OUTPUT}}}", re.escape(e1), filled)
    filled = re.sub("{{{GRADER_2_OUTPUT}}}", re.escape(g2), filled)
    filled = re.sub("{{{EVALUATOR_2_OUTPUT}}}", re.escape(e2), filled)
    filled = re.sub("{{{INFO}}}", re.escape(info), filled)
    return filled

def judge(cache_name, item, g1, e1, g2, e2, info, video_uri, credentials):
    """Runs the judge phase."""
    judge_schema = {
        "type": "object",
        "properties": {
            "score": {"type": "string", "enum": ["Not Demonstrated", "Fail", "Pass"]},
            "rationale": {"type": "string"}
        },
        "required": ["score", "rationale"]
    }
    
    prompt = assemble_judge(item, g1, e1, g2, e2, info)
    cache_name, responses = poll_vertex([prompt], judge_schema, cache_name, video_uri, credentials, temperature=1.0)
    
    judge_json = responses[0].json()
    metadata = judge_json.get("usageMetadata", {})
    tokens = (metadata.get("totalTokenCount", 0), metadata.get("cachedContentTokenCount", 0))
    
    candidates = judge_json.get("candidates", [])
    if not candidates:
        raise ValueError("No candidates")
        
    judge_data = json.loads(candidates[0]["content"]["parts"][0]["text"])
    judge_string = f"Judge gave a final score of {judge_data['score']} with the following rationale: {judge_data['rationale']}"
    
    return cache_name, judge_string, judge_data["score"], judge_data["rationale"], tokens

