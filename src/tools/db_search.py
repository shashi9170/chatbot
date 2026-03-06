from langchain_core.tools import tool

@tool
def DB_search(query: str) -> str:
    """Search the internal database for user information."""
    
    return "Shashi Prakash, I live in bihar"