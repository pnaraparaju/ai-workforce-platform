from fastapi import Depends, FastAPI

from app.config import settings
from app.dependencies import get_llm
from app.llm.base import LLM
from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import generate_response

app = FastAPI(title=settings.app_name)


@app.get("/")
def root():
    return {"message": "AI Workforce Platform is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, llm: LLM = Depends(get_llm)):
    response = generate_response(request.message, llm)

    return ChatResponse(response=response)
