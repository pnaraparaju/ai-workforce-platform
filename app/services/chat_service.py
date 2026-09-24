from app.llm.fake import FakeLLM
llm = FakeLLM()


def generate_response(message: str) -> str:
    return llm.generate(message)