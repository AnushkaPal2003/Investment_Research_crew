from crewai import Task


def build_industry_task(agent, company):
    return Task(
        description=(
            f"Research {company}'s industry position, main competitors, "
            "and any recent news from the last 6 months."
        ),
        expected_output=(
            "5-8 bullet points covering industry position, competitors, "
            "and recent news, each with a source."
        ),
        agent=agent,
    )


def build_financial_task(agent, company):
    return Task(
        description=(
            f"Find {company}'s key public financial metrics (revenue, growth, "
            "margins if available) and recent performance signals."
        ),
        expected_output="5-8 bullet points of financial metrics and performance, each with a source.",
        agent=agent,
    )


def build_risk_task(agent, industry_task, financial_task):
    return Task(
        description="Review the industry and financial findings. Flag any contradictions, unverified claims, or missing context.",
        expected_output="A short list of flags, or a note confirming no issues were found.",
        agent=agent,
        context=[industry_task, financial_task],
    )


def build_report_task(agent, industry_task, financial_task, risk_task, company):
    return Task(
        description=(
            f"Write a one-page due-diligence brief on {company} using the "
            "industry research, financial findings, and risk review."
        ),
        expected_output=(
            "A markdown-formatted one-page brief with sections: "
            "Industry Position, Financial Snapshot, Risk Notes, Summary."
        ),
        agent=agent,
        context=[industry_task, financial_task, risk_task],
    )
