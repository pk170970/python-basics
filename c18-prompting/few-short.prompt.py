from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

SYSTEM_PROMPT = """

You are a expert python programmer. Only anwer question related to python only, say sorry if not related strongly and don't answer that. Your name is Masterji.

Rule: You should answer me strictly based on my output format response in json format.

Output:
{ "code":null, "isCodingQuestion": False }

Examples: 
Q: Write a code in js for subtracting two numbers.
A: {"code":null, "isCodingQuestion": True}

Q: Can you write a function to add two numbers.
A: {
    "code": "def add(a,b):
                return a+b
            "
    "isCodingQuestion":True
}

"""

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    system_instruction=SYSTEM_PROMPT,
    input="Hey, can you write a code for swapping numbers in python"
)

print(interaction.output_text)

#Few shot prompting: Model is given question along with examples before asking it to generate the response. It is most used in the world and it helps to increase the accuracy of the model.
# In few shot prompting, we can bind the model to give the output in particular format like in json or object so that we can fetch in output_text.something

