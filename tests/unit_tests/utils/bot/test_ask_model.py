import pytest
from utils.bot import ConversationalBot
from utils.llm import Message


class FakeLlm:
    def __init__(self, show_success: bool):
        self.response: str = "Hello!"
        self.show_success: bool = show_success

    def invoke(
        self,
        query: str | None,  # pyright: ignore[reportUnusedParameter]
        messages: list[Message] | None,  # pyright: ignore[reportUnusedParameter]
        system_prompt: str = "",  # pyright: ignore[reportUnusedParameter]
    ):
        if not self.show_success:
            raise ValueError("Forced value error by test")

        return self.response

    def set_response(self, content: str) -> None:
        self.response = content


@pytest.mark.parametrize(
    "message, expected",
    [("", pytest.raises(ValueError)), (" ", pytest.raises(ValueError))],
)
def test_ask_model_message_should_not_be_empty_or_whitespaced(
    message: str, expected: pytest.RaisesExc
):
    with expected:
        llm = FakeLlm(show_success=True)

        bot = ConversationalBot(llm=llm)
        user_message = build_user_message(message)

        _ = bot.ask_model(message=user_message)


def test_ask_model_should_return_bot_message_when_success():
    llm = FakeLlm(show_success=True)
    bot = ConversationalBot(llm=llm)

    user_message = build_user_message("Hello! Bot")
    bot_message = bot.ask_model(user_message)

    assert bot_message == "Hello!"


def build_user_message(content: str) -> Message:
    return Message(role="user", content=content)
