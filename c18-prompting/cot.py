# chain of thought prompting -> Instead of solving everything at once, we are saying to model that break the task in chunks and answer
# step by step. Deepseek and o3 gpt model based on chain of thought prompting, we want our model to think for more accurate.

from google import genai
from google.genai import types
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client()

SYSTEM_PROMPT = '''
    You are a expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN, OUTPUT steps.
    You need to first PLAN on what need's to be done. Planning will be of multiple steps. Once you think
    enough PLAN is done, you can return the OUTPUT.

    Rule: 
    - Strictly follow the given json output format.
    - Only run one step at a time.
    - Sequence of step is START where user gives an input, PLAN(that can be mulitple times) and OUTPUT(going to be displayed to the user)

    Output:
    {
    'step':START | PLAN | OUTPUT, content: 'string'
    }

    Example: 
    START: Hey, Can you solve Can you solve 5 * 7 - 10 / 10
    PLAN: {'step': PLAN, content: 'Seems, user is interested in AI problem'}
    PLAN: {'step':PLAN, content: 'We should use bodmas rule to solve this problem'}
    PLAN: {'step':PLAN, content: 'First 10 / 10 is 1 so expression becomes 5 * 7 - 1'}
    PLAN: {'step':PLAN, content: 'Then solving the multiplication which results 35 so expression becomes 35 -1'}
    OUTPUT:{'step':OUTPUT, content:'Final answer of this is 34'}
'''

history = 'The user wants a Python code to swap two numbers. I should plan to provide the most pythonic way to do this, which is using tuple unpacking (a, b = b, a), as well as the traditional method using a temporary variable for educational purposes.'
    # 'parts': [{'text': 'The user wants a Python code to swap two numbers. I should plan to provide the most pythonic way to do this, which is using tuple unpacking (a, b = b, a), as well as the traditional method using a temporary variable for educational purposes.'}]

history = []
isPlanningDone = False

# Fastest successful models:
# gemini-3.5-flash-lite: 1.19 seconds
# gemini-3-flash-preview: 2.09 seconds
# gemini-3.1-flash-lite: 3.37 seconds
# gemini-3.6-flash: 3.52 seconds
# gemini-flash-lite-latest: 12.07 seconds
# gemini-3.1-flash-lite-preview: 12.23 seconds

previous_interaction_id = None

while True:
    request = {
        'model': 'gemini-3.5-flash-lite',
        'system_instruction': SYSTEM_PROMPT,
        'input': "Write a python program for swapping two numbers" if len(history) == 0 else "What's next ?",
        'store': True,
    }

    if not isPlanningDone:
        if previous_interaction_id is not None:
            request["previous_interaction_id"] = previous_interaction_id

        interaction = client.interactions.create(**request)

        text = interaction.output_text

        if not text:
            raise ValueError("Gemini returned empty output")

        text = text.strip()

        if text.startswith("```"):
            text = text.removeprefix("```json").removeprefix("```")
            text = text.removesuffix("```").strip()

        output = json.loads(text)
        print(output)
        history.append({
            "interaction_id" : interaction.id,
            "output": output
        })
        previous_interaction_id = interaction.id
        isPlanningDone = True if output['step'] == 'OUTPUT' else False
        print('========================/n')
    else:
        break

print(history)