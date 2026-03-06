from src.llm.gemini_model import GeminiModel


class ModelFactory:

    @staticmethod
    def get_model(provider: str = "gemini", streaming: bool = False):

        if provider == "gemini":
            return GeminiModel.get_model(streaming)

        raise ValueError(f"Unsupported model provider: {provider}")