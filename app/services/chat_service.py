from app.llm.base import LLM
from app.schemas import Message


def generate_response(message: str, llm: LLM) -> str:
    messages = [
        Message(
            role="user",
            content=message,
        )
    ]

    return llm.generate(messages)
