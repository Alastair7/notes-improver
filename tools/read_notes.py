from typing import TypedDict

from openai.types.chat import ChatCompletionToolParam

from utils.config import get_notes_dir
from utils.files import get_md_file_content

NOTES_DIR = get_notes_dir().resolve()


class NoteDict(TypedDict):
    title: str
    description: str
    keywords: list[str]
    text: str


def read_note_content(filename: str) -> NoteDict:
    """
    Read a note and return a JSON.
    """

    file_path = (NOTES_DIR / filename).resolve()

    if not str(file_path).startswith(str(NOTES_DIR)):
        raise ValueError("Invalid file path")

    if not file_path.exists():
        raise FileNotFoundError(f"Note not found: {filename}")

    note = get_md_file_content(file_path)

    return {
        "title": note.title,
        "description": note.description,
        "keywords": list(note.keywords),
        "text": note.text,
    }


READ_NOTE_TOOL_SCHEMA: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "readNoteContent",
        "description": "Read a markdown note.",
        "parameters": {
            "type": "object",
            "properties": {"filename": {"type": "string"}},
            "required": ["filename"],
        },
    },
}
