from fastapi import FastAPI

from app.config import settings
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(title=settings.app_name)


@app.get("/")
def root():
    return {"message": "AI Workforce Platform is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=f"You said: {request.message}"
    )
