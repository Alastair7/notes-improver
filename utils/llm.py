from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol, cast

from openai.types.chat import (
    ChatCompletionMessageParam,
)

from jinja2 import Template
from openai import OpenAI

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
            raise ValueError("query or messages must be provided")

        chat_history: list[dict[str, str]] = []
        prompt = Template(system_prompt).render(**kwargs)

        chat_history.append({"role": "system", "content": prompt})

        if messages:
            chat_history.extend(
                {"role": m.role, "content": m.content} for m in messages
            )
        elif query:
            chat_history.append({"role": "user", "content": query})

        # Add logging system: LogGuru, StructuredLog, built-in logging.
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=cast(list[ChatCompletionMessageParam], chat_history),
        )

        return response.choices[0].message.content or ""


def parse_files(llm: LlmBase, files_to_parse: list[Path]):
    for file in files_to_parse:
        print("Parsing file:", file.name)
        raw_content = file.read_text(encoding="utf-8")

        improved_note = llm.invoke(
            raw_content, messages=None, system_prompt=syncing_template
        )
        md_file_path = file.with_suffix(".md")

        with md_file_path.open("w", encoding="utf-8") as f:
            f.write(improved_note)
