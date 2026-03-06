from langchain_google_genai import ChatGoogleGenerativeAI
from src.config.settings import GEMINI_API_KEY


class GeminiModel:

    _normal = None
    _stream = None

    @classmethod
    def get_model(cls, streaming: bool = False):

        if streaming:
            if cls._stream is None:
                cls._stream = ChatGoogleGenerativeAI(
                    model="gemini-2.5-flash",
                    google_api_key=GEMINI_API_KEY,
                    temperature=0.7,
                    streaming=True
                )
            return cls._stream

        if cls._normal is None:
            cls._normal = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=GEMINI_API_KEY,
                temperature=0.7
            )

        return cls._normal