"""
=========================================
Hello LLM — Capstone Starter Project
=========================================
Author  : Your Name
Date    : 2026-05-23
GitHub  : https://github.com/YOUR_USERNAME/hello-llm

What this does:
    Calls the Groq LLM API and answers user questions
    in the terminal. Remembers conversation history
    across multiple turns.

How to run:
    1. Activate venv:  venv\Scripts\activate
    2. Install deps:   python -m pip install -r requirements.txt
    3. Run:            python app.py
"""

import os
import sys
from dotenv import load_dotenv

# ── Load .env file into environment ──────────────────
# python-dotenv reads the .env file and makes all
# variables available via os.getenv()
load_dotenv()

# ── Read values from environment ─────────────────────
# Never hardcode secrets in code — always use env vars
API_KEY = os.getenv("GROQ_API_KEY")
MODEL   = os.getenv("MODEL", "llama-3.1-8b-instant")

# ── Validate API key exists before doing anything ────
# Fail early with a clear message — better than a
# confusing error deep inside the program
if not API_KEY:
    print("ERROR: GROQ_API_KEY not found.")
    print("  1. Copy .env.example to .env")
    print("  2. Paste your key from https://console.groq.com/keys")
    sys.exit(1)

# ── Import Groq SDK ───────────────────────────────────
# Installed via: python -m pip install groq
try:
    from groq import Groq
except ImportError:
    print("ERROR: groq package missing.")
    print("  Run: pip install -r requirements.txt")
    sys.exit(1)

# Initialize the client using the API key from .env
client = Groq(api_key=API_KEY)

# System prompt tells the model how to behave
SYSTEM_PROMPT = (
    "You are a helpful, concise assistant. "
    "Answer clearly and briefly. "
    "If you do not know something, say so honestly."
)


def ask(question, history):
    """
    Send a question to the LLM and return the answer.

    How it works:
        1. Add user question to history list
        2. Send full history + system prompt to Groq API
        3. Extract answer text from API response
        4. Add answer to history for next turn
        5. Return the answer

    Args:
        question (str) : The user's question
        history  (list): List of previous messages

    Returns:
        str: The assistant's answer
    """
    # Step 1 — add user message to history
    history.append({"role": "user", "content": question})

    # Step 2 — call Groq API with full conversation history
    # The system prompt is prepended to every request
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
        temperature=0.7,
        max_tokens=512,
    )

     # Step 3 — extract answer from API response object
    answer = response.choices[0].message.content.strip()

    # Step 4 — add assistant reply to history
    history.append({"role": "assistant", "content": answer})

    # Step 5 — return answer to caller
    return answer


def main():
    """
    Main loop — runs the interactive terminal chatbot.
    Keeps asking for input until user types quit.
    """
    print("=" * 50)
    print("  Hello LLM — your first AI app")
    print(f"  Model  : {MODEL}")
    print("  Type your question. Type 'quit' to exit.")
    print("=" * 50)

    # Conversation history — plain Python list of dicts
    # This is what gives the AI memory across turns
    history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C and Ctrl+D gracefully
            print("\nGoodbye!")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Exit commands
        if user_input.lower() in {"quit", "exit", "q", "bye"}:
            print("Goodbye!")
            break

        try:
            answer = ask(user_input, history)
            print(f"\nAssistant: {answer}")
        except Exception as e:
            print(f"API error: {e}")

# ── Initialize the Groq client ────────────────────────
# This object handles all API communication
if __name__ == "__main__":
    main()