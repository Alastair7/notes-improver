import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol, cast

from jinja2 import Template
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionMessageParam,
)

logger = logging.getLogger(__name__)

syncing_template = Path("./prompts/syncing_template.md").read_text(encoding="utf-8")
system_prompt = Path("./prompts/system_prompt.md").read_text(encoding="utf-8")


@dataclass
class Message:
    role: Literal["system", "user", "assistant"]
    content: str


class LlmBase(Protocol):
    def invoke(
        self,
        query: str | None,
        messages: list[Message] | None,
        system_prompt: str = "",
        **kwargs,
    ) -> str: ...


@dataclass()
class GeminiLlm:
    client: OpenAI

    def invoke(
        self,
        query: str | None,
        messages: list[Message] | None = None,
        system_prompt: str = system_prompt,
        **kwargs,
    ) -> str:
        if query is None and messages is None:
            empty_input_message = "query or messages must be provided"
            logger.error(empty_input_message)
            raise ValueError(empty_input_message)

        chat_history: list[dict[str, str]] = []

        already_has_system_prompt = any(msg["role"] == "system" for msg in chat_history)
        if not already_has_system_prompt:
            prompt = Template(system_prompt).render(**kwargs)  # pyright: ignore[reportAny]
            chat_history.append({"role": "system", "content": prompt})

        if messages:
            chat_history.extend(
                {"role": m.role, "content": m.content} for m in messages
            )
        elif query:
            chat_history.append({"role": "user", "content": query})

        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=cast(list[ChatCompletionMessageParam], chat_history),
        )

        logger.debug("Chat history: %s", chat_history)
        logger.debug("LLM response: %s", response.choices[0].message.content)

        return response.choices[0].message.content or ""


def parse_files(llm: LlmBase, files_to_parse: list[Path]):
    for file in files_to_parse:
        print("Parsing file:", file.name)
        logger.info("Parsing file: %s", file.name)
        raw_content = file.read_text(encoding="utf-8")

        improved_note = llm.invoke(
            raw_content, messages=None, system_prompt=syncing_template
        )
        md_file_path = file.with_suffix(".md")

        with md_file_path.open("w", encoding="utf-8") as f:
            f.write(improved_note)

        logger.info("Parsing completed: %s", md_file_path)
