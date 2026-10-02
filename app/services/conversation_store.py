from uuid import uuid4

from app.schemas import Message


conversations: dict[str, list[Message]] = {}


def create_conversation() -> str:
    conversation_id = str(uuid4())

    conversations[conversation_id] = []

    return conversation_id

def get_messages(conversation_id: str) -> list[Message]:
    return conversations[conversation_id]

def add_message(conversation_id: str, message: Message) -> None:
    conversations[conversation_id].append(message)

def conversation_exists(conversation_id: str) -> bool:
    return conversation_id in conversations