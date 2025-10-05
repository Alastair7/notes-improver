from dataclasses import dataclass
from pathlib import Path
import frontmatter


@dataclass
class Note:
    keywords: set[str]
    text: str


def get_files_with_text(path: Path, text: str) -> list[Path]:
    return [file for file in path.glob("*.md") if text in file.read_text()]


def get_md_file_content(path: Path) -> Note:
    note = Note(keywords=set(), text="")
    content = path.read_text()

    if content == "":
        return note

    # DUDA: Es posible añadirle un tipado a text.metadata[key]?
    text = frontmatter.loads(content) 
    keywords = text.metadata.get("keywords", set())

    return Note(keywords=keywords,text=text.content)
