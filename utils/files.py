from dataclasses import dataclass
from pathlib import Path
from typing import cast

import frontmatter


@dataclass
class Note:
    keywords: set[str]
    title: str
    description: str
    text: str


def get_files_to_parse(path: Path) -> list[Path]:
    txt_files = [file for file in path.rglob("*.txt") if file.stat().st_size > 0]
    md_files = [file.stem for file in path.rglob("*.md")]

    return [file for file in txt_files if file.stem not in md_files]


def get_files_with_text(path: Path, text: str) -> list[Path]:
    return [file for file in path.rglob("*.md") if text in file.read_text()]


def get_md_file_content(path: Path) -> Note:
    content = path.read_text()

    text = frontmatter.loads(content)
    title = cast(str, text.metadata.get("title", ""))
    description = cast(str, text.metadata.get("description", ""))
    keywords = cast(list[str], text.metadata.get("keywords", []))

    return Note(
        keywords=set(keywords), text=text.content, title=title, description=description
    )


def get_all_md_files_content(path: Path) -> list[Note]:
    md_files = [file for file in path.rglob("*.md") if file.stat().st_size > 0]

    return [get_md_file_content(note) for note in md_files]


def search_files_with_keywords(path: Path, keywords: list[str]) -> list[Path]:
    def note_has_keywords(keywords: list[str], file: Path):
        return set(keywords) & get_md_file_content(file).keywords

    return [
        file for file in path.rglob(pattern="*.md") if note_has_keywords(keywords, file)
    ]
