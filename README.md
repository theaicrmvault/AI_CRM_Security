# Hello LLM

My first standalone AI application.
Calls the Groq LLM API using Python and answers questions
in the terminal with full conversation memory.

---

## What This Does

- Takes user questions in the terminal
- Sends them to the Groq LLM API (free)
- Remembers the full conversation across turns
- Handles errors with clear messages
- Protects API keys using environment variables

---

## Tech Stack

| Tool                  | Purpose                         |
|-----------------------|---------------------------------|
| Python 3.11           | Core programming language       |
| Groq API              | Free LLM inference platform     |
| llama-3.1-8b-instant  | Language model                  |
| python-dotenv         | Environment variable management |
| VS Code               | Development environment         |
| GitHub                | Version control and hosting     |

---

## Project Structure

hello-llm/
├── app.py               Main chatbot application
├── requirements.txt     Python dependencies
├── .env.example         API key template (safe to commit)
├── .env                 Your real API key (never committed)
├── .gitignore           Keeps secrets out of git
├── README.md            This file
├── tests/
│   └── test_app.py      Unit tests
└── logs/
    └── progress.md      Daily learning log

---

## Setup and Run

### Step 1 — Clone the repository
git clone https://github.com/YOUR_USERNAME/hello-llm.git
cd hello-llm

### Step 2 — Create virtual environment
python -m venv venv
venv\Scripts\activate

### Step 3 — Install dependencies
python -m pip install -r requirements.txt

### Step 4 — Set up API key
Get a free key at https://console.groq.com/keys

Copy .env.example to .env
Paste your key in .env replacing the placeholder

### Step 5 — Run
python app.py

---

## How It Works

1. User types a question in the terminal
2. Question is added to conversation history list
3. Full history is sent to Groq API with a system prompt
4. API returns an answer
5. Answer is added to history for next turn
6. Process repeats with full context preserved

---

## Security Practices

- API key stored in .env file — never written in code
- .env is listed in .gitignore — never committed to GitHub
- .env.example committed as a safe template for others
- No hardcoded credentials anywhere in the codebase

---

## What I Learned

- How to call a real LLM API from Python
- How conversation history and context works
- How to protect secrets using environment variables
- Python functions, loops, and error handling
- Git version control and GitHub workflow

---

## Daily Progress

See logs/progress.md for my day by day learning log.

---

## Author

Your Name
GitHub: https://github.com/theaicrmvault

---

## License

MIT