from tavily import TavilyClient
from langchain_core.tools import tool
from src.config.settings import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

@tool
def tavily_search(query: str) -> str:
    """
    Search the internet for latest news, current events,
    today's updates, and real-time information.
    """

    print(query)
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        results = []
        for r in response["results"]:
            results.append(f"{r['title']}\n{r['content']}\nSource: {r['url']}\n")

        return "\n\n".join(results)

    except Exception as e:
        return f"Search error: {str(e)}"