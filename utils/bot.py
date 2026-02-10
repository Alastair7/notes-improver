from utils.files import Note
from utils.llm import LlmBase, Message


class ConversationalBot:
    def __init__(self, llm: LlmBase):
        self._chat_history: list[Message] = []
        self._llm: LlmBase = llm
        self.context: list[Note] = []

    def ask_model(self, message: Message) -> str:
        """Send a message to the LLM. It also updates the chat history internally."""

        if message.content.strip() == "":
            raise ValueError("Message must not be empty or whitespaced")

        model_response = self._llm.invoke(
            query=None, messages=self._chat_history, notes=self.context
        )

        model_message = self._build_model_response_message(model_response)

        self._chat_history.append(message)
        self._chat_history.append(model_message)

        return model_response

    def add_notes_context(self, notes: list[Note]):
        self.context = notes

    def _build_model_response_message(self, response: str) -> Message:
        return Message(role="assistant", content=response)
