from langchain_google_genai import ChatGoogleGenerativeAI
from src.config.settings import GEMINI_API_KEY

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.7
    )

    return llm