import os

from crewai import Agent, LLM

from tools.search_tool import web_search

# ----------------------------
# Debug (remove later)
# ----------------------------
print("Groq key exists:", bool(os.getenv("GROQ_API_KEY")))
print("Groq key prefix:", os.getenv("GROQ_API_KEY", "")[:8])

# ----------------------------
# LLM
# ----------------------------
try:
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )
except Exception:
    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )


# ----------------------------
# Agents
# ----------------------------
def build_industry_agent():
    return Agent(
        role="Industry Research Analyst",
        goal="Research the company's industry position, competitors, and recent market news",
        backstory="A meticulous market analyst who always backs claims with sourced facts.",
        tools=[web_search],
        llm=llm,
        verbose=True,
    )


def build_financial_agent():
    return Agent(
        role="Financial Analyst",
        goal="Find and summarize the company's key financial metrics and recent performance",
        backstory="A financial analyst who digs up revenue, margins, and valuation signals from public sources.",
        tools=[web_search],
        llm=llm,
        verbose=True,
    )


def build_risk_agent():
    return Agent(
        role="Risk Reviewer",
        goal="Cross-check the industry and financial findings for contradictions, unverified claims, or missing context",
        backstory="A skeptical reviewer who never accepts a claim without checking it against the other findings.",
        llm=llm,
        verbose=True,
    )


def build_writer_agent():
    return Agent(
        role="Report Writer",
        goal="Turn the research and review into a concise, well-structured one-page brief",
        backstory="A clear, concise financial writer who turns raw research into an executive-ready brief.",
        llm=llm,
        verbose=True,
    )