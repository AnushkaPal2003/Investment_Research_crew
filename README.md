# Investment Research Crew

A multi-agent company due-diligence system built with CrewAI. Give it a company name, get back a one-page research brief.

## How it works

```
Company name
     |
     v
+---------------------+     +----------------------+
| Industry Research    |     | Financial Analyst     |
| Agent (web search)   |     | Agent (web search)    |
+---------------------+     +----------------------+
             \                     /
              v                   v
          +---------------------------+
          |      Risk Reviewer         |
          |  (flags contradictions)    |
          +---------------------------+
                        |
                        v
              +-------------------+
              |  Report Writer     |
              +-------------------+
                        |
                        v
              One-page markdown brief
```

Four role-specialized CrewAI agents run sequentially: two research agents gather industry and
financial signals via web search (Tavily), a risk reviewer cross-checks both outputs for
contradictions before anything is finalized, and a writer agent turns it all into a structured brief.

## Tech stack

CrewAI, Groq (`llama-3.3-70b-versatile`), Tavily, FastAPI, Streamlit, Docker, GitHub Actions.

## Project structure

```
agents/     agent definitions (plain functions, one per role)
tasks/      task definitions (plain functions, one per step)
tools/      Tavily web search tool
crew/       assembles agents + tasks into a Crew and runs it
api/        FastAPI backend, exposes POST /research
frontend/   Streamlit UI that calls the API
tests/      smoke tests (no live API calls)
```

## Run locally

```bash
cp .env.example .env   # add your GROQ_API_KEY and TAVILY_API_KEY
pip install -r requirements.txt

uvicorn api.main:app --reload          # backend on :8000
streamlit run frontend/app.py          # frontend on :8501
```

## Run with Docker

```bash
cp .env.example .env   # add your keys
docker compose up --build
```

Backend: http://localhost:8000/docs
Frontend: http://localhost:8501

## Tests

```bash
pytest tests/ -v
```
## CI/CD

CI/CD pipeline configured with Docker Hub deployment.
