from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
from openai import OpenAI

notes_improver_template = Path("./notes_improver_template.md").read_text(encoding="utf-8")

class LlmBase(Protocol):
    def invoke(self, query: str) -> str: ...

@dataclass()
class GeminiLlm():
    client: OpenAI
    
    def invoke(self, query: str) -> str:
        response = self.client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": notes_improver_template },
        {
            "role": "user",
            "content": query        
        }
    ]
)

        return response.choices[0].message.content or ""

def parse_files(llm: LlmBase, files_to_parse: list[Path]):
    for file in files_to_parse:
        raw_content = file.read_text(encoding='utf-8')

        improved_note = llm.invoke(raw_content)
        md_file_path = file.with_suffix(".md")

        with md_file_path.open("w", encoding="utf-8") as f:
            f.write(improved_note)
