from app.llm.base import LLM
from app.schemas import Message


class FakeLLM(LLM):

    def generate(self, messages: list[Message]) -> str:
        last_message = messages[-1]

        return f"Fake LLM response to: {last_message.content}"
