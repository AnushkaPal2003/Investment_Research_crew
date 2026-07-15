
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from crew.crew_runner import run_research_crew

app = FastAPI(title="Investment Research Crew API")


class ResearchRequest(BaseModel):
    company: str


class ResearchResponse(BaseModel):
    company: str
    report: str


@app.get("/health")
def health():
    return {"status": "ok"}
from litellm.exceptions import RateLimitError
import traceback
from fastapi import HTTPException




@app.post("/research")
def research(req: ResearchRequest):
    try:
        report = run_research_crew(req.company)
        return {"company": req.company, "report": report}

    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail="Groq daily token limit reached. Please try again later."
        )