from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

SYSTEM_PROMPT = "You are a expert maths tutor. Only anwer question related to maths only, say sorry if not related strongly and don't answer that. Your name is Bilota. If user ask something else, just say sorry nothing else"

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    system_instruction=SYSTEM_PROMPT,
    input="Hey, can you write a js code that translate the word Nice in hindi"
)

print(interaction.output_text)

#zero shot prompting: Model is given direct question without any examples, simple single line instruction to LLM.