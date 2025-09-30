from dataclasses import dataclass
from pathlib import Path


@dataclass
class Note:
    keywords: set[str]
    text: str


def get_files_with_text(path: Path, text: str) -> list[Path]:
    return [file for file in path.glob("*.md") if text in file.read_text()]


def get_md_file_content(path: Path) -> Note:
    return Note(keywords=set(), text="")
