from fastapi import FastAPI

from app.config import settings
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
def chat(request: ChatRequest):
    response = generate_response(request.message)

    return ChatResponse(response=response)