from dataclasses import dataclass
from pathlib import Path
from typing import cast

import frontmatter


@dataclass
class Note:
    keywords: set[str]
    text: str


def get_files_with_text(path: Path, text: str) -> list[Path]:
    return [file for file in path.rglob("*.md") if text in file.read_text()]


def get_md_file_content(path: Path) -> Note:
    content = path.read_text()

    text = frontmatter.loads(content)
    keywords = cast(list[str], text.metadata.get("keywords", []))

    return Note(keywords=set(keywords), text=text.content)


def search_files_with_keywords(path: Path, keywords: list[str]) -> list[Path]:
    def note_has_keywords(keywords: list[str], file: Path):
        return set(keywords) & get_md_file_content(file).keywords

    return [
        file for file in path.glob(pattern="*.md") if note_has_keywords(keywords, file)
    ]
