from app.llm.base import LLM


class FakeLLM(LLM):

    def generate(self, prompt: str) -> str:
        return f"Fake LLM response to: {prompt}"