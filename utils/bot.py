from utils.llm import LlmBase, Message


class ConversationalBot:
    def __init__(self, llm: LlmBase):
        self._chat_history: list[Message] = []
        self._llm: LlmBase = llm

    def ask_model(self, message: Message) -> str:
        """Send a message to the LLM. It also updates the chat history internally."""

        if message.content.strip() == "":
            raise ValueError("Message must not be empty or whitespaced")

        self._add_message_to_chat_history(message=message)

        model_response = self._llm.invoke(
            query=None,
            messages=self._chat_history,
        )

        model_message = self._build_model_response_message(model_response)
        self._add_message_to_chat_history(model_message)

        return model_response

    def _build_model_response_message(self, response: str) -> Message:
        return Message(role="assistant", content=response)

    def _add_message_to_chat_history(self, message: Message) -> None:
        self._chat_history.append(message)
