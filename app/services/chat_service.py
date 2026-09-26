from app.llm.base import LLM

def generate_response(message: str, llm: LLM) -> str:
    return llm.generate(message)
