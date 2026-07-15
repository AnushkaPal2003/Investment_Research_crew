import litellm

_original_completion = litellm.completion

def _patched_completion(*args, **kwargs):
    messages = kwargs.get("messages")
    if messages:
        for msg in messages:
            if isinstance(msg, dict):
                msg.pop("cache_breakpoint", None)
    return _original_completion(*args, **kwargs)

litellm.completion = _patched_completion
from crewai import Crew, Process

import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from agents.agents import (
    build_financial_agent,
    build_industry_agent,
    build_risk_agent,
    build_writer_agent,
)
from tasks.tasks import (
    build_financial_task,
    build_industry_task,
    build_report_task,
    build_risk_task,
)


def run_research_crew(company: str) -> str:
    industry_agent = build_industry_agent()
    financial_agent = build_financial_agent()
    risk_agent = build_risk_agent()
    writer_agent = build_writer_agent()

    industry_task = build_industry_task(industry_agent, company)
    financial_task = build_financial_task(financial_agent, company)
    risk_task = build_risk_task(risk_agent, industry_task, financial_task)
    report_task = build_report_task(writer_agent, industry_task, financial_task, risk_task, company)

    crew = Crew(
        agents=[industry_agent, financial_agent, risk_agent, writer_agent],
        tasks=[industry_task, financial_task, risk_task, report_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return str(result)
