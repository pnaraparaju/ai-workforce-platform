import requests

from app.config import settings
from app.llm.base import LLM


class OllamaLLM(LLM):

    def generate(self, prompt: str) -> str:
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