# Daily Progress Log

# Daily Progress Log — Hello LLM

## Purpose
Daily record of what I built, learned, and struggled with.
Committed to GitHub every day as proof of consistent work.

---

## Day 1 — 2026-05-23
Time spent: X hours
Goal: Get Groq API working and run first AI response.
Done:
- Set up hello-llm project folder in VS Code
- Created Python virtual environment
- Installed groq and python-dotenv packages
- Connected to Groq API successfully
- Received first AI response from llama3-8b-8192 model
Blocker 1: 
- Device Guard blocked venv pip.exe on local machine.
Fix: Used python -m pip instead of pip directly.
Blocker 1: 
- Got error llama3-8b-8192 model has been dicomissioned
Fix: changed model to llama-3.1-8b-instant
Key learning: API keys must never be written in code.
              Always use environment variables.
              Do not use deperecated LLM.
Tomorrow: dig deeper into the build.

---

## Day 2 — 2026-MM-DD
Time spent:
Goal:
Done:
Blocker:
Fix:
Key learning:
Tomorrow:

---

## Day 3 — 2026-MM-DD
Time spent:
Goal:
Done:
Blocker:
Fix:
Key learning:
Tomorrow:

---

## Lessons Learned (Running List)

| Date       | Lesson                                              |
|------------|-----------------------------------------------------|
| 2026-05-23 | Never put API keys in code — use .env always        |
| 2026-05-23 | venv must be active before installing packages      |
| 2026-05-23 | python -m pip works when pip.exe is blocked         |
| 2026-05-23 | .gitignore must list .env to keep secrets safe      |

---

## Commands Reference

# Activate virtual environment
venv\Scripts\activate

# Install packages
python -m pip install -r requirements.txt

# Run the app
python app.py

# Run tests
python -m pytest tests/ -v

# Daily git workflow
git add .
git commit -m "docs: update Day N progress log"
git push