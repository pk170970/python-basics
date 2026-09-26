from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI() # create your web application

SYSTEM_PROMPT = '''
    You are an expert AI assistant which solves complex or simple user queries and explain them in very simple words using examples. Don't answer anything other that coding related questions, if someone ask just say Sorry, I can only answer coding related questions.
'''

class MessageRequest(BaseModel):
    message:str



@app.get('/') # registers a route, so someone sends a get request
def home():
    return {'message': 'Fast api is running'}

@app.get('/health')
def healt_check():
    return {'status':'ok'}

@app.post('/chat')
def chat(request: MessageRequest, session_id = None):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise HTTPException(
            status_code=503,
            detail='GEMINI_API_KEY is missing. Add to your missing file'
        )
    client = genai.Client(api_key=api_key)

    try:
        interaction = client.interactions.create(
                model = 'gemini-3.5-flash-lite',
                system_instruction= SYSTEM_PROMPT,
                input = request.message,
                previous_interaction_id= session_id
            )
    except errors.APIError as error:
        raise HTTPException(
            status_code=502,
            detail='The gemini request failed. Try again later'
        ) from error
    return {'reply': interaction.output_text}