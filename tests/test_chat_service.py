
import pytest

from app.llm.base import LLM
from app.schemas import Message
from app.services.chat_service import generate_response
from app.services.conversation_store import (
    conversations,
    create_conversation,
)


class FailingLLM(LLM):
    def generate(self, messages: list[Message]) -> str:
        raise RuntimeError("Simulated LLM failure")


def test_user_message_is_removed_when_llm_fails():
    conversation_id = create_conversation()

    with pytest.raises(RuntimeError, match="Simulated LLM failure"):
        generate_response(
            message="Hello",
            conversation_id=conversation_id,
            llm=FailingLLM(),
        )

    assert conversations[conversation_id] == []


def test_successful_response_saves_both_messages():
    from app.llm.fake import FakeLLM
    from app.services.conversation_store import get_messages

    conversation_id = create_conversation()

    returned_id, response = generate_response(
        message="Hello",
        conversation_id=conversation_id,
        llm=FakeLLM(),
    )

    messages = get_messages(conversation_id)

    assert returned_id == conversation_id
    assert response == "Fake LLM response to: Hello"
    assert len(messages) == 2
    assert messages[0].role == "user"
    assert messages[0].content == "Hello"
    assert messages[1].role == "assistant"
    assert messages[1].content == response
