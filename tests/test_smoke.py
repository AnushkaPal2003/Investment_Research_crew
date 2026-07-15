import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("GROQ_API_KEY", "test-key")
os.environ.setdefault("TAVILY_API_KEY", "test-key")

from fastapi.testclient import TestClient

from agents.agents import (
    build_financial_agent,
    build_industry_agent,
    build_risk_agent,
    build_writer_agent,
)
from api.main import app
from tasks.tasks import build_industry_task

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agents_build_with_correct_roles():
    assert build_industry_agent().role == "Industry Research Analyst"
    assert build_financial_agent().role == "Financial Analyst"
    assert build_risk_agent().role == "Risk Reviewer"
    assert build_writer_agent().role == "Report Writer"


def test_task_description_includes_company():
    agent = build_industry_agent()
    task = build_industry_task(agent, "TestCo")
    assert "TestCo" in task.description
