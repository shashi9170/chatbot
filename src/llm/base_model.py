from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def get_model(self, streaming: bool = False):
        pass