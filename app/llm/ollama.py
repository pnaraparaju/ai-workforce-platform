import requests

from app.config import settings
from app.llm.base import LLM
from app.schemas import Message

class OllamaLLM(LLM):

    def generate(self, messages: list[Message]) -> str:
        prompt = "\n".join(
            f"{message.role}: {message.content}"
            for message in messages
        )

        response = requests.post(
            f"{settings.ollama_base_url}/api/generate",
            json={
                "model": settings.ollama_model,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        return response.json()["response"]