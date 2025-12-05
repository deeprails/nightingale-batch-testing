# Project Configuration
PROJECT_ID = "nightingale-deeprails"
LOCATION = "global"
MODEL_NAME = "gemini-2.5-pro"
BUCKET_NAME = "nightingale-deeprails-vertex-videos"
VIDEO_TYPE_NAME = "BSN206 Handwashing"
PROMPT_VERSION = "new_dec5_1"

# Video Settings
FPS = 10.0
TTL_SECONDS = 2400.0  # 40 minutes
DEFAULT_TEMP = 0.5
REGRADE_TEMP = 0.7

# Testing Configuration
# Set to None to run all, or a list of integers to run specific chunks.
# Readiness chunks are 0-indexed relative to readiness (0, 1)
# Mastery chunks are 0-indexed relative to mastery (0, ..., 9)
RUN_READINESS_CHUNKS = []
RUN_MASTERY_CHUNKS = [2,9]

# Logic Constants
NUM_READINESS_CHUNKS = 2
NUM_MASTERY_CHUNKS = 10
NUM_READINESS_ITEMS = 12
NUM_MASTERY_ITEMS = 40

# Rubric Items
RUBRIC_ITEMS = [
    # Item 1
    "Wore a Nightingale College uniform (grey scrubs with a Nightingale logo on the chest)",
    # Item 2
    "Wore a Nightingale College ID visible on their shirt",
    # Item 3
    "Wore their hair such that it is not obstructing their face",
    # Item 4
    "Wore no jewelry anywhere on their hands",
    # Item 5
    "Wore no jewelry on their wrists or arms",
    # Item 6
    "Kept fingernails short, natural, and free of polish",
    # Item 7
    "Has access to a clean, dry demonstration area for donning gloves, such as a dry countertop or a separate table",
    # Item 8
    "Has access to a sink with running water",
    # Item 9
    "Has access to a dispenser pump with liquid hand soap",
    # Item 10
    "Has access to unused paper towels",
    # Item 11
    "Has access to sterile gloves in sterile packaging",
    # Item 12
    "Has access to hands-free garbage can or a designated garbage area",
    # Item 13
    "Turns sink water on",
    # Item 14
    "Allows water to run for a few seconds",
    # Item 15
    "Wets both hands under warm water",
    # Item 16
    "Keeps both hands at or below the level of the elbows when moving towards the soap dispenser. Brief hand movements upwards are acceptable.",
    # Item 17
    "Dispenses small amount of hand soap onto wet hands (may use a hands free dispenser) and/or demonstrates soap was applied with visible lather",
    # Item 18
    "Points fingers and arms downward into the sink most of the time while washing hands. Arm and hand positioning should ensure water can flow down their hands.",
    # Item 19
    "Washes all areas of both hands, including between fingers and under nails, for at least 15 seconds",
    # Item 20
    "Rinses hands until all soap is gone such that the soapy water flows down their hands and into the sink",
    # Item 21
    "Does not touch sink areas during rinsing process",
    # Item 22
    "Allows sink water to continue to run after rinsing",
    # Item 23
    "Grabs a clean paper towel after washing hands",
    # Item 24
    "Uses clean paper towel to dry hands",
    # Item 25
    "Dries hands completely, without skipping any areas",
    # Item 26
    "Disposes of paper towel without contaminating hands by touching other surfaces",
    # Item 27
    "Grabs another clean paper towel",
    # Item 28
    "Uses the paper towel to turn off sink water. Note: when the faucet is not in frame, you will have to use audio to determine if the sink water is still running.",
    # Item 29
    "Does not touch anything when transitioning to the sterile glove package",
    # Item 30
    "Touches only the sterile glove outer wrapper when opening it.",
    # Item 31
    "Places or gently drops the inner wrapper containing the gloves onto the clear, clean surface. The student should only touch the sterile glove outer wrapper while completing this step.",
    # Item 32
    "Opens the inner wrapper of the sterile glove package and establishes sterile field by completely unfolding the inner wrapper. The wrapper should not rest on other objectsor hang over edges of the table or sink basin.",
    # Item 33
    "Opens inner sterile wrapper by touching only the 1-inch folded margin on the outer edge of the wrapper",
    # Item 34
    "With one hand, picks up the glove for the other hand by pinching the folded, nonsterile cuff of the glove with bare fingers",
    # Item 35
    "Maintaining hold on the glove cuff, uses the grabbing hand to assist the other hand into the glove",
    # Item 36
    "All fingers and thumb of the first gloved hand are in proper spaces in the glove and the folded cuff remains intact (not rolled out)",
    # Item 37
    "Body of glove covers the entire first gloved hand to the wrist and the rest of the lower arm remains unobstructed by shirt sleeves",
    # Item 38
    "With the gloved hand, slides fingers under the cuff of the second glove, between the folded cuff and the body of the glove",
    # Item 39
    "Maintains hold on the glove cuff for the ungloved hand without touching nonsterile surfaces like the cuff or skin with the gloved thumb.",
    # Item 40
    "Uses only gloved hand to assist positioning of the ungloved hand into the glove",
    # Item 41
    "All fingers and thumb of the second gloved hand are in proper spaces in the glove and the folded cuff remains intact (not rolled out)",
    # Item 42
    "Body of glove covers the entire second gloved hand to the wrist and the rest of the lower arm remains unobstructed by shirt sleeves",
    # Item 43
    "Keeps hands at or above the waist area for the majority of the time after donning both gloves to avoid brushing against nonsterile surfaces",
    # Item 44
    "Grabs middle, sterile area of the used inner wrapper that held the gloves with one gloved hand to discard",
    # Item 45
    "Discards used inner wrapper of glove packaging into trash receptacle or designated waste area without touching any other surface",
    # Item 46
    "Removes glove from one hand by pinching the glove exterior with other hand",
    # Item 47
    "Pulls hand out while maintaining hold on the glove",
    # Item 48
    "Uses still gloved hand to hold the used glove before taking the other off OR disposes of the first glove into the trash receptacle or designated waste area immediately.",
    # Item 49
    "Insert a few bare fingers into the glove where wrist meets palm",
    # Item 50
    "Pushing with the inserted fingers, take glove off by folding the inside of the glove over the outside",
    # Item 51
    "If the first glove has not been disposed of, the second glove also rolls over it as part of removal such that the second glove entirely wraps around the first glove",
    # Item 52
    "Discard used gloves in the trash receptacle or designated waste area without touching any other surface"
]

# Mappings
readiness_item_to_prompt = [0,0,0,0,0,0,1,1,1,1,1,1]
mastery_item_to_prompt = [0,0,0,0,0,1,1,1,1,1,2,2,
                          2,2,2,2,3,3,3,4,4,5,5,5,
                          5,6,6,6,6,6,7,7,7,8,8,8,
                          9,9,9,9]

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
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment.",
    # Item 9
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment.",
    # Item 10
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment.",
    # Item 11
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment.",
    # Item 12
    "### Rules\n - Note that some items may be obscured or out of frame; you should use visual and audio clues to make an informed judgment.",
    # Item 13
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 14
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 15
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 16
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 17
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.\n - The student must apply soap after wetting their hands.",
    # Item 18
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 19
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 20
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 21
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 22
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - Listen to audio cues to be sure the water is turned on.",
    # Item 23
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 24
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 25
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 26
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 27
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 28
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.",
    # Item 29
    "### Rules\n - If the student talks about and/or mimes the action instead of performing it, give them a **Not Demonstrated** score.\n - For the purposes of the video, the student touching the recording device to transition is not a break in sterility.",
    # Item 30
    "### Rules\n - Students may have practiced with this glove package, so it may be opened already. However, both the outer plastic wrapper and inner wax paper wrapper must be present and repackaged as best as possible. The student cannot earn points related to the outer package if it's not present.",
    # Item 31
    "### Rules\n - Students may have practiced with this glove package, so it may be opened already. However, both the outer plastic wrapper and inner wax paper wrapper must be present and repackaged as best as possible. The student cannot earn points related to the outer package if it's not present.",
    # Item 32
    "### Success Examples\n - Opens sterile glove inner wrapper without touching other surfaces.\n - When opening inner wrapper, only touches folded portions and strictly inside the outer 1 inch margin of the unfolded section.\n\n### Failure Examples\n - Gloves move off the sterile field while opening inner wrapper.\n - Touches anywhere inside 1 inch margin of unfolded wrapper while establishing sterile field, even an inch and a half past the border is too far.",
    # Item 33
    "### Success Examples\n - Opens sterile glove inner wrapper without touching other surfaces.\n - When opening inner wrapper, only touches folded portions and strictly inside the outer 1 inch margin of the unfolded section.\n\n### Failure Examples\n - Gloves move off the sterile field while opening inner wrapper.\n - Touches anywhere inside 1 inch margin of unfolded wrapper while establishing sterile field, even an inch and a half past the border is too far.",
    # Item 34
    "### Rules\n - The outside of the cuff is the nonsterile, interior portion of the glove that has been folded up and over the sterile part of the glove. The student must only touch the outside of the cuff with their bare hands; touching anywhere else on the glove is a break in sterility.",
    # Item 35
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 36
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".\n - The student should have the gloves pulled all the way on; there should be no space left at the ends of fingers.",
    # Item 37
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 38
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 39
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 40
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 41
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".\n - The student should have the gloves pulled all the way on; there should be no space left at the ends of fingers.",
    # Item 42
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 43
    "### Rules\n - If, at any point while putting on or wearing the gloves, the folded cuff rolls such that the exterior surface of the glove instead of the fold touches skin, that is a break in sterility. The student cannot earn points for the one item closest to the sterility break.\n - Do not identify the student's hands as left or right. If you refer to the hands, say \"the first hand\" or \"the second hand\".",
    # Item 44
    "### Rules\n - If the student touched only the sterile central region of the used inner wrapper when discarding, then mark them as Pass. If wrapper handling is partially off-camera, listen for rustling and look for immediate disposal into trash. If both are missing, mark Not Demonstrated. If the discarding process appears to touch other surfaces, mark Fail and explicitly describe (which surface) in rationale.",
    # Item 45
    "### Rules\n - The inner wrapper that contained the gloves is sterile except for a one inch wide margin around the edges, so the gloves can only contact inside that margin",
    # Item 46
    "",
    # Item 47
    "",
    # Item 48
    "",
    # Item 49
    "",
    # Item 50
    "",
    # Item 51
    "",
    # Item 52
    ""
]
# Prompts
TIMESTAMP_PROMPT = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and create a timeline of key events.

### Instructions
1. Watch the video carefully from start to finish.
2. Identify the timestamps for key events in the process, such as drying hands, opening glove package, etc.
3. Do not evaluate the quality of the performance. Focus only on WHAT happened and WHEN.
4. Output a JSON object with a list of events, each having a timestamp (e.g., "00:15") and a brief description.

Example Output:
{
  "events": [
    {"timestamp": "00:05", "event": "Turns on sink water"},
    {"timestamp": "00:10", "event": "Wets hands"},
    ...
  ]
}
"""

PROMPT_1 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of their preparation for the task.

### Readiness Criteria
You will be evaluating whether or not the student did six things properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
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

### Video Events
{{{VIDEO_EVENTS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
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

### Video Events
{{{VIDEO_EVENTS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
 """

PROMPT_4 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the handwashing task. The previous steps in handwashing are provided for context.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed five components of handwashing properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_5 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the handwashing task. The previous steps in handwashing are provided for context.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed six components of handwashing properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_6 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps of handwashing are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed three components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously. If a step is off screen or visually occluded and you are unsure of how to proceed, err on the side of the student passing.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_7 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed two components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the examples below and use them to understand how students may fail or succeed to complete the skill mastery criteria.
2. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously. If a step is off screen or visually occluded and you are unsure of how to proceed, err on the side of the student passing.
4. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_8 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously. If a step is off screen or visually occluded and you are unsure of how to proceed, err on the side of the student passing.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_9 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed five components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously. If a step is off screen or visually occluded and you are unsure of how to proceed, err on the side of the student passing.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_10 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed three components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student met each of the skill mastery criteria successfully and continuously.
4. For each item, evaluate if the student completed the exact task using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_11 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Rules section below, being sure to understand them completely and keep them in mind during your evaluation.
2. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
3. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously.
4. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning.
5. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

PROMPT_12 = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving, and then evaluate several specific details of the sterile gloving task. The previous steps in handwashing and sterile gloving are provided for context.

Sterility is very important in sterile gloving, and must be maintained throughout. The unfolded inner glove wrapper (besides a 1 inch margin around its edge) and the exterior surface of the gloves are considered sterile. Everything else, including the student's hands and the inside of the gloves are considered non-sterile.
Sterile gloves have a cuff folded such that some of the nonsterile interior is exposed. This is so that the student can grab a portion of the glove with their bare hands while putting it on, but it means that once the gloves are on, the gloved fingers cannot touch the cuff. The cuff also prevents the glove's sterile exterior from rolling inward and touching nonsterile skin, and, as such, the folded cuff must be maintained as long as the gloves are worn.

### Skill Mastery Criteria
You will be evaluating whether or not the student completed four components of gloving properly:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the Previous Steps in handwashing and sterile gloving, and use that context to inform your evaluations of the current Skill Mastery Criteria.
2. Watch the video and assess whether the student completed each of the skill mastery criteria successfully and continuously.
3. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning.
4. Attach a clear and brief piece of feedback with a neutral tone to each score that summarizes your chain-of-thought reasoning. Cite specific visual and/or audio evidence to support your reasoning.
5. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details.

{{{INFO}}}
"""

EVALUATOR = """
You are an expert nursing education evaluator who checks the work of nursing education graders. Your job is to review a video of a nursing student demonstrating a specific skill, and check to be sure that the grader did not make any errors in its evaluation.

The grader is very effective and trustworthy for the most part, but struggles with some specific issues. It will sometimes assert that something has happened when it hasn't or miss something that did occur. Be sure to check each statement it makes by checking the video. Do not assume that it is correct, but also do not assume it is wrong; it is correct a majority of the time.

### Rubric Items
You will be evaluating the following items:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Grader’s Assessment
The grader’s assessment for these items is as follows:
{{{PREVIOUS_RESULTS}}}

### Steps
1. Read the section below, being sure to understand the information completely and how the evaluation of these rubric items should be done.
2. Watch the video without considering the grader's assessment in order to form your own judgment for whether the student successfully met that item.
3. Then, watch the video again while considering the grader's assessment in order to determine whether you agree with the grader's original score and rationale.
3. For each rubric item, determine whether you agree with the grader’s original score, thinking step by step.
4. For each rubric item, determine whether each detail in the grader's original rationale is correct and well written.
5. For each item, output:
   - `score_verdict`: **True** if you agree with the grader’s score for this item, or **False** if you do not.
   - `rationale_verdict`: **True** if you approve of the grader’s rationale for this item, or **False** if you do not.
   - `reasoning`: A clear, detailed explanation of your chain of thought reasoning (including why you agree or disagree with the grader on that item). Cite specific visual and/or audio evidence directly from the video to support your reasoning.

{{{INFO}}}
"""

REGRADER = """
You are an expert nursing education evaluator. Your job is to review a video of a nursing student demonstrating handwashing & sterile gloving. You are the second grader in the process, so be extra thorough in your evaluation. The previous steps in handwashing and sterile gloving are provided for context.

### Rubric Items Needing Re-evaluation
An evaluator disagreed with the original grader on the following items:
{{{RUBRIC_ITEMS}}}

### Video Events
{{{VIDEO_EVENTS}}}

### Previous Steps
{{{PREVIOUS_STEPS}}}

### Steps
1. Read the section below, being sure to understand the information completely and keep it in mind during your evaluation.
2. Review the description of each of the rubric items, using the rules and/or examples to fully understand the requirements for each item.
3. Review the previous steps in handwashing and sterile gloving, and use that context to inform your regrades of the current rubric items.
4. Watch the video and assess whether the student completed each of the rubric items completely and fully, thinking step by step.
5. For each item, evaluate if the student completed the exact task or exhibited exactly the prescribed behavior using chain-of-thought reasoning.
6. For each item, output:
   - `score`: **Not Demonstrated** if the student did not make a good faith attempt to complete the rubric item, **Fail** if the student attempted the rubric item but did not complete it satisfactorily, or **Pass** otherwise.
   - `rationale`: A concise but complete explanation of your judgment. Write clearly with a neutral tone as if giving feedback to the student, covering all relevant details. Cite specific visual and/or audio evidence to support your reasoning.

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

4. Video Timeline:
{{{VIDEO_EVENTS}}}

## Instructions
Analyze the Rubric: deeply understand the specific criteria required for a passing score.
Incorporate Additional Information: Review the given rules and/or examples, if any for the Rubric Item to totally understand all nuances of the criterion.
Review the Evidence: Watch the video carefully, looking specifically for the actions mentioned in the rubric.
Weigh the Arguments: Read the history of the dispute. Look for patterns where the Graders and Evaluators disagree.
Note: Do not default to the "Evaluator" or the "Grader." Trust only the visual evidence from the video and the strict text of the Rubric.
Adjudicate: Decide the final score based strictly on whether the student met the criteria defined in the Rubric and Rules.
Explain: Write a final rationale that gives feedback to the student on the specific criteria that they did and did not meet. Do not reference the previous agents or their disagreements.
"""
