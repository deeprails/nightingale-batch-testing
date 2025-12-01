
# Project Configuration
PROJECT_ID = "nightingale-deeprails"
LOCATION = "global"
MODEL_NAME = "gemini-3-pro-preview"
BUCKET_NAME = "nightingale-deeprails-vertex-videos"
VIDEO_TYPE_NAME = "BSN206 Handwashing"
PROMPT_VERSION = "nov30_1"

# Video Settings
FPS = 10.0
TTL_SECONDS = 2100.0  # 35 minutes

# Logic Constants
NUM_READINESS_CHUNKS = 2
NUM_MASTERY_CHUNKS = 10
NUM_READINESS_ITEMS = 12
NUM_MASTERY_ITEMS = 41

# Rubric Items
RUBRIC_ITEMS = [
    # Item 1
    "Wore a Nightingale College uniform",
    # Item 2
    "Wore a Nightingale College ID visible on their shirt",
    # Item 3
    "Wore their hair such that it is pulled away from their face",
    # Item 4
    "Wore no jewelry anywhere on their hands",
    # Item 5
    "Wore no jewelry on their wrists or arms",
    # Item 6
    "Kept fingernail length short (<1mm beyond end of finger)",
    # Item 7
    "Demonstration area is relatively clean and clear (e.g. no unnecesary substances or objects within 18 inches of gloving supplies that aren't being used in the demonstration)",
    # Item 8
    "Has access to a sink with running water",
    # Item 9
    "Has access to liquid hand soap with dispenser pump",
    # Item 10
    "Has access to unused paper towel or napkins",
    # Item 11
    "Has access to sterile gloves in sterile packaging (and sterile drape/field if used)",
    # Item 12
    "Has access to hands-free garbage can or a designated garbage area",
    # Item 13
    "Turns sink water on",
    # Item 14
    "Allows water to run for a few seconds",
    # Item 15
    "Wets both hands",
    # Item 16
    "Keeps both hands at or below the level of the elbows when moving them toward soap dispenser. Brief movements upwards are acceptable.",
    # Item 17
    "Dispenses small amount of hand soap (~3-5 ml) onto wet hands (may use a hands free dispenser)",
    # Item 18
    "Positions fingers downward into the sink for most of the time while washing hands. Brief movements upwards are acceptable.",
    # Item 19
    "Washes all areas of both hands for at least 15 seconds",
    # Item 20
    "Keeps fingers pointed downward into the sink for most of the time while rinsing both hands until all soap is gone. Brief movements upwards are acceptable.",
    # Item 21
    "Does not touch sink areas during rinsing process",
    # Item 22
    "Allows sink water to continue to run after rinsing",
    # Item 23
    "Grabs a clean paper towel after washing",
    # Item 24
    "Uses clean paper towel to dry hands",
    # Item 25
    "Dries hands generally starting from fingertips and ending at the wrists",
    # Item 26
    "Disposes of paper towel without contaminating their hands",
    # Item 27
    "Grabs another clean paper towel",
    # Item 28
    "Uses the paper towel to turn off sink water. Note: when the faucet is not in frame, you will have to use audio to determine if the sink water is still running.",
    # Item 29
    "Does not touch anything when transitioning to the sterile glove package",
    # Item 30
    "Touches only the sterile glove outer wrapper when opening it.",
    # Item 31
    "Without touching anything else, places or gently drops the inner wrapper onto the clear, clean surface",
    # Item 32
    "Opens sterile glove inner wrapper and establishes sterile field without touching or overlapping other surfaces",
    # Item 33
    "Opens inner sterile wrapper by touching only the 1-inch folded margin edge",
    # Item 34
    "With one hand, picks up the glove for the other hand by pinching the outside of the cuff",
    # Item 35
    "Maintaining hold on the glove cuff, uses the grabbing hand to assist the other hand into the glove",
    # Item 36
    "All fingers and thumb of the first gloved hand are in proper spaces in the glove and the folded cuff remains intact (not rolled out)",
    # Item 37
    "Body of glove covers the entire first gloved hand to the wrist and the rest of the lower arm remains unobstructed by shirt sleeves",
    # Item 38
    "With the gloved hand, slides fingers under the cuff of glove for the ungloved hand",
    # Item 39
    "Maintains hold on the glove cuff for the ungloved hand without using thumb of the gloved hand",
    # Item 40
    "Uses only gloved hand to assist positioning of the ungloved hand into the glove",
    # Item 41
    "All fingers and thumb of the second gloved hand are in proper spaces in the glove and the folded cuff remains intact (not rolled out)",
    # Item 42
    "Body of glove covers the entire second gloved hand to the wrist and the rest of the lower arm remains unobstructed by shirt sleeves",
    # Item 43
    "After donning both gloves, keeps hands at or above the waist area for the majority of the time",
    # Item 44
    "Grabs middle area of used glove wrapper with one gloved hand to discard",
    # Item 45
    "Discards used wrapper into trash receptacle without touching any surface",
    # Item 46
    "Remove glove from one hand by pinching in the middle of the glove exterior with other hand",
    # Item 47
    "Pulls hand out from the middle of the glove",
    # Item 48
    "As one hand pulls out of the glove, interior rolls to fold over the outside",
    # Item 49
    "Use gloved hand to hold the used glove.",
    # Item 50
    "Place bare fingers inside the glove below the palm",
    # Item 51
    "Pushing with the inserted fingers, fold the inside of glove over the outside",
    # Item 52
    "As removal occurs, the second glove also rolls to cover the first glove",
    # Item 53
    "Discard used gloves in the trash receptacle"
]

# Mappings
readiness_item_to_prompt = [0,0,0,0,0,0,1,1,1,1,1,1]
mastery_item_to_prompt = [0,0,0,0,0,1,1,1,1,1,2,2,
                          2,2,2,2,3,3,3,4,4,5,5,5,
                          5,6,6,6,6,6,7,7,7,8,8,8,
                          8,9,9,9,9]

# Rubric Info (Rules & Examples)
RUBRIC_INFO = [
    # Item 1
    "",
    # Item 2
    "",
    # Item 3
    "",
    # Item 4
    "### Rules\n - Note that some students may have discoloration from where they usually wear jewelry or watches; this is not a failure.",
    # Item 5
    "### Rules\n - Note that some students may have discoloration from where they usually wear jewelry or watches; this is not a failure.",
    # Item 6
    "",
    #  Item 7
    "### Rules\n - If there's items that can't be moved near the work area, don't fail the student.",
    # Item 8
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment. Lean towards the student meeting the criteria if there is any doubt.",
    # Item 9
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment. Lean towards the student meeting the criteria if there is any doubt.",
    # Item 10
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment. Lean towards the student meeting the criteria if there is any doubt.",
    # Item 11
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment. Lean towards the student meeting the criteria if there is any doubt.",
    # Item 12
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment. Lean towards the student meeting the criteria if there is any doubt.",
    # Item 13
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 14
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 15
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 16
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 17
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 18
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 19
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 20
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 21
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 22
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 23
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 24
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 25
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.\n - Moving from wrists back to the fingertips is a violation.",
    # Item 26
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 27
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 28
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 29
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 30
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 31
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 32
    "### Rules\n - Verbalization of any of these rubric items is not a sufficient replacement for performing them. If the student only talks about and/or mimes the action, do not give them credit.",
    # Item 33
    "### Rules\n - Students may have practiced with this glove package, so it may be opened already. However, both the outer plastic wrapper and inner wax paper wrapper must be present and repackaged as best as possible. The student cannot earn points related to the outer package if it's not present.",
    # Item 34
    "### Rules\n - Students may have practiced with this glove package, so it may be opened already. However, both the outer plastic wrapper and inner wax paper wrapper must be present and repackaged as best as possible. The student cannot earn points related to the outer package if it's not present.",
    # Item 35
    "### Rules\n - Students may have practiced with this glove package, so it may be opened already. However, both the outer plastic wrapper and inner wax paper wrapper must be present and repackaged as best as possible. The student cannot earn points related to the outer package if it's not present.",
    # Item 36
    "### Success Examples\n - Opens sterile glove inner wrapper without touching other surfaces.\n - When opening inner wrapper, only touches folded portions and strictly inside the outer 1 inch margin of the unfolded section.\n\n### Failure Examples\n - Gloves move off the sterile field while opening inner wrapper.\n - Touches anywhere inside 1 inch margin of unfolded wrapper while establishing sterile field, even an inch and a half past the border is too far.",
    # Item 37
    "### Success Examples\n - Opens sterile glove inner wrapper without touching other surfaces.\n - When opening inner wrapper, only touches folded portions and strictly inside the outer 1 inch margin of the unfolded section.\n\n### Failure Examples\n - Gloves move off the sterile field while opening inner wrapper.\n - Touches anywhere inside 1 inch margin of unfolded wrapper while establishing sterile field, even an inch and a half past the border is too far.",
    # Item 38
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 39
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 40
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 41
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 42
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 43
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 44
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 45
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 46
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 47
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 48
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 49
    "",
    # Item 50
    "",
    # Item 51
    "",
    # Item 52
    "",
    # Item 53
    ""
]

# Prompts
PROMPT_1 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of their preparation for the task.

### Readiness Criteria
You will be evaluating whether or not the student did six things properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_2 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of their preparation for the task.

### Readiness Criteria
You will be evaluating whether or not the student prepared six things properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_3 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the handwashing task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed five components of handwashing properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
 """

PROMPT_4 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the handwashing task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed five components of handwashing properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_5 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the handwashing task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed six components of handwashing properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_6 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed three components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_7 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed two components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the examples below and use them to understand how students may fail or succeed to complete the skill mastery criteria.
2. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning. Output True for the item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_8 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_9 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed five components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2, Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_10 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed three components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning. Output True for that item if they did and False if they did not.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_11 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously.
2. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning. Output True for the item if they did and False if they did not.
3. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
4. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_12 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Steps
1. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously.
2. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning. Output True for the item if they did and False if they did not.
3. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning.
4. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

EVALUATOR = """
You are an expert nursing education evaluator who checks the work of nursing education graders. Your job is to review a video of a nursing student demonstrating a nursing student demonstrating a specific skill, and then evaluate specific components of the task independently and compare them to the grader’s assessment.

### Rubric Items
You will be evaluating the following items:
{{{RUBRIC_ITEMS}}}

### Grader’s Assessment
The grader’s assessment for these items is as follows:
{{{PREVIOUS_RESULTS}}}

### Steps
1. Read the section below, being sure to understand the information completely and keep it in mind during your evaluation.
2. Watch the video and evaluate each rubric item independent of the grader, forming your own judgment for whether the student successfully met that item.
3. For each rubric item, determine whether you agree with the grader’s original score, thinking step by step.
4. For each rubric item, determine whether the grader's original rationale is correct and well written.
5. For each item, output:
   - `score_verdict`: **True** if you agree with the grader’s score for this item, or **False** if you do not.
   - `rationale_verdict`: **True** if you agree with the grader’s rationale for this item, or **False** if you do not.
   - `reasoning`: A clear, detailed explanation of your reasoning (including why you agree or disagree with the grader on that item).

{{{INFO}}}
"""

REGRADER = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving. You are the second grader in the process, so be extra thorough in your evaluation.

### Rubric Items Needing Re-evaluation
An evaluator disagreed with the original grader on the following items:
{{{RUBRIC_ITEMS}}}

### Steps
1. Read the section below, being sure to understand the information completely and keep it in mind during your evaluation.
2. Review each of the rubric items, keeping the rules and/or examples in mind as you understand the requirements.
3. Watch the video and re-assess each listed item, being sure the student absolutely meets the rubric item's criteria.
4. For each item, decide whether the student met the rubric criteria, thinking step by step.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

JUDGE_PROMPT="""
## System/Role Definition
You are the Final Nursing Education Judge. You act as the final decision-maker in a pipeline of automated graders for nursing students demonstrating handwashing and sterile gloving. Your goal is to resolve conflicts between previous graders and evaluators to determine the definitive score and rationale for a nursing student's video submission.

## Context
A nursing student has submitted a video demonstrating handwashing and sterile gloving.
An initial Grader assessed the video for a specific rubric item evaluating a small portion of one of the skills.
An Evaluator reviewed that assessment and found issues.
A Regrader (a fresh set of eyes) assessed the video.
A second Evaluator reviewed the Regrader's assessment and disagreements persist.
Your job is to review the rubric, and the arguments from all four previous agents, and then issue the Final Judgment.

## Inputs
1. Rubric Item to Evaluate:
{{{RUBRIC_ITEM}}}

2. Additional Information for Rubric Item
{{{INFO}}}

3. Evaluation History:
Round 1 Grader: {{{GRADER_1_OUTPUT}}}
Round 1 Evaluator: {{{EVALUATOR_1_OUTPUT}}}
Round 2 Regrader: {{{GRADER_2_OUTPUT}}}
Round 2 Evaluator: {{{EVALUATOR_2_OUTPUT}}}

## Instructions
Analyze the Rubric: deeply understand the specific criteria required for a passing score.
Incorporate Additional Information: Review the given rules and/or examples, if any for the Rubric Item to totally understand all nuances of the criterion.
Review the Evidence: Watch the video carefully, looking specifically for the actions mentioned in the rubric.
Weigh the Arguments: Read the history of the dispute. Look for patterns where the Graders and Evaluators disagree.
Note: Do not default to the "Evaluator" or the "Grader." Trust only the visual evidence from the video and the strict text of the Rubric.
Adjudicate: Decide the final score based strictly on whether the student met the criteria defined in the Rubric and Rules.
Explain: Write a final rationale that gives feedback to the student on the specific criteria that they did and did not meet. Do not reference the previous agents or their disagreements.
"""
