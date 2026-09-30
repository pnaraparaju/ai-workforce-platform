from abc import ABC, abstractmethod

from app.schemas import Message


class LLM(ABC):

    @abstractmethod
    def generate(self, messages: list[Message]) -> str:
        pass
