
from app.llm.base import LLM
from app.schemas import Message
from app.services.conversation_store import (
    create_conversation,
    get_messages,
    conversation_exists,
)


def generate_response(
    message: str,
    conversation_id: str | None,
    llm: LLM,
) -> tuple[str, str]:
    if conversation_id is None:
        conversation_id = create_conversation()
    elif not conversation_exists(conversation_id):
        raise ValueError("Conversation not found")

    messages = get_messages(conversation_id)

    user_message = Message(
        role="user",
        content=message,
    )

    messages.append(user_message)

    try:
        response = llm.generate(messages)
    except Exception:
        messages.pop()
        raise

    messages.append(
        Message(
            role="assistant",
            content=response,
        )
    )

    return conversation_id, response
