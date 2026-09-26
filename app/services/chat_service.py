from app.llm.ollama import OllamaLLM
llm = OllamaLLM()


def generate_response(message: str) -> str:
    return llm.generate(message)