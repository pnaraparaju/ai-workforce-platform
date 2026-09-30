from app.llm.ollama import OllamaLLM


def get_llm() -> OllamaLLM:
    return OllamaLLM()