from typing import TypedDict

from openai.types.chat import ChatCompletionToolParam

from utils.config import get_notes_dir

NOTES_DIR = get_notes_dir().resolve()


class NotesCountDict(TypedDict):
    count: int
    filenames: list[str]


def list_notes() -> NotesCountDict:
    """Return the number of notes and their filenames."""
    notes = sorted(f.name for f in NOTES_DIR.glob("*.md"))
    return {"count": len(notes), "filenames": notes}


LIST_NOTES_TOOL_SCHEMA: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "listNotes",
        "description": "Get the number of notes and their filenames.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
}
