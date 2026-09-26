# FastAPI + Gemini Chat Learning Project

## Purpose

Build a small web API in Python that accepts a message, sends it to Gemini, and lets the same user ask a follow-up question. You will write the code yourself, one small step at a time. Ask for help when you get stuck; this guide explains what to build without giving you the finished implementation.

This project uses the Google GenAI SDK and `client.interactions.create()`, which you are already using. It does not use Ollama or require a local model, Docker, agents, or RAG.

## What You Will Build

- `GET /health`: a simple route that confirms the API server is running.
- `POST /chat`: a route that accepts a message, sends it to Gemini, and returns Gemini's answer.
- Follow-up chat: a session ID lets the API connect a new request to that session's previous Gemini interaction.

## Build It Step By Step

### Step 1: Prepare the project

1. Create and activate a Python virtual environment for this project.
2. Install FastAPI, its development server, the Google GenAI SDK, and `python-dotenv`.
3. Put your Gemini API key in a `.env` file. Keep that file private and do not paste the key into Python source code.
4. Make a small server file for the FastAPI application.

**In simple terms:** this step prepares a separate workspace and keeps your secret API key out of your code.

### Step 2: Make a health route

1. Create the FastAPI application object.
2. Add a `GET /health` route.
3. Make it return a small JSON response such as `{"status": "ok"}`.
4. Start the development server and open its `/docs` page. Try the health route there.

**In simple terms:** this checks that FastAPI starts and can answer an HTTP request before Gemini is involved.

### Step 3: Accept a chat message

1. Define a request shape with a required text message and an optional session ID.
2. Add a `POST /chat` route that receives and validates that request.
3. For the first test, return a temporary response that repeats or acknowledges the message.
4. Use `/docs` to send a request and inspect the JSON response.

**In simple terms:** FastAPI receives JSON from the caller, checks that it has the expected fields, and sends JSON back.

### Step 4: Connect one Gemini request

1. Load the API key from the environment and create a Google GenAI client.
2. Inside the chat route, call `client.interactions.create()` with the model name and the incoming message as `input`.
3. Return the generated `interaction.output_text` in the API response.
4. Handle a missing API key or failed Gemini request by returning a useful error instead of an unexplained server crash.

**In simple terms:** the route becomes a bridge: it receives a message, asks Gemini, and returns Gemini's text.

### Step 5: Add follow-up conversation history

1. Keep an in-memory dictionary in the server. Use each session ID as a key and that session's latest Gemini interaction ID as its value.
2. When a request has no session ID, start a new session and make a Gemini interaction without `previous_interaction_id`.
3. When a request has a session ID already known to the server, pass its saved interaction ID as `previous_interaction_id` to `client.interactions.create()`.
4. After Gemini responds, save the new `interaction.id` for that session. Return both the answer and the session ID.
5. Test a first question, then send a follow-up with the returned session ID. Ask something like "Explain your previous answer" and check that Gemini understands the reference.

**In simple terms:** the server remembers which Gemini interaction belongs to each chat. Gemini uses that interaction ID to continue the conversation; you do not need to manually create `assistant` role messages for this API.

## Expected Request Flow

1. Send a message to `POST /chat` without a session ID.
2. The API starts a new conversation and responds with Gemini's answer plus a session ID.
3. Send another message to `POST /chat` with that same session ID.
4. The API finds the previous interaction ID for that session and asks Gemini to continue from it.

## Important Learning Limits

- The in-memory dictionary is only for learning. It is cleared when the server stops or restarts.
- Keep separate session IDs for separate conversations so their history does not get mixed together.
- Do not ask the model to reveal private hidden chain-of-thought. If you want an explanation, ask for a concise plan or an explanation of the answer.
- Once these steps work, the next project can add an agent tool, such as a calculator. RAG can be learned separately after that.

## Completion Checklist

- [ ] The server starts and `GET /health` works.
- [ ] `POST /chat` accepts a message and returns a response.
- [ ] Gemini is called through `client.interactions.create()`.
- [ ] A second request using the same session ID continues the earlier conversation.
- [ ] Different session IDs keep their histories separate.