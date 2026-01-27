from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from jinja2 import Template
from openai import OpenAI

syncing_template = Path("./prompts/syncing_template.md").read_text(encoding="utf-8")
system_prompt = Path("./prompts/system_prompt.md").read_text(encoding="utf-8")


class LlmBase(Protocol):
    def invoke(self, query: str, system_prompt: str = "") -> str: ...


@dataclass()
class GeminiLlm:
    client: OpenAI

    def invoke(self, query: str, system_prompt: str = system_prompt, **kwargs) -> str:
        prompt = Template(system_prompt).render(**kwargs)

        # Add logging system: LogGuru, StructuredLog, built-in logging.
        print("PROMPT:", prompt)
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            # Add chat history as parameter instead of only one message.
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query},
            ],
        )

        return response.choices[0].message.content or ""


def parse_files(llm: LlmBase, files_to_parse: list[Path]):
    for file in files_to_parse:
        print("Parsing file:", file.name)
        raw_content = file.read_text(encoding="utf-8")

        improved_note = llm.invoke(raw_content, system_prompt=syncing_template)
        md_file_path = file.with_suffix(".md")

        with md_file_path.open("w", encoding="utf-8") as f:
            f.write(improved_note)
