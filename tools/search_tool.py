import os

from crewai.tools import tool
from tavily import TavilyClient


@tool("web_search")
def web_search(query: str) -> str:
    """Search the web for up-to-date information on a company, industry, or financial topic."""
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    results = client.search(query=query, max_results=5)
    return "\n\n".join(f"{r['title']}: {r['content']}" for r in results["results"])
