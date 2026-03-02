from typing import TypedDict
from jinja2 import Template
from openai.types.chat import ChatCompletionToolParam
from utils.config import get_notes_dir
from utils.files import Note


NOTES_DIR = get_notes_dir().resolve()
NOTE_TEMPLATE = """
```markdown
---
keywords: [{{note.keywords|join(",")}}]
title: {{note.title}}
description: {{note.description}}
---

{{note.text}}
"""


class GenerateNewNoteDict(TypedDict):
    status: str
    path: str
    title: str
    description: str
    message_to_user: str


def generate_new_note(
    title: str, description: str, keywords: str, text: str, path: str
) -> GenerateNewNoteDict:
    """
    Generate a note based on a prompt.
    """

    keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
    note = Note(
        keywords=set(keyword_list), title=title, description=description, text=text
    )

    note_path = (NOTES_DIR / path).resolve()

    if not note_path.is_relative_to(NOTES_DIR):
        raise ValueError("Path must be inside notes/")

    if note_path.exists():
        raise ValueError("Note already exists.")

    if note_path.suffix != ".md":
        raise ValueError("The file extension must be a markdown")

    note_path.parent.mkdir(parents=True, exist_ok=True)

    content = Template(NOTE_TEMPLATE).render(note=note)  # pyright: ignore[reportAny]

    _ = note_path.write_text(content)  # pyright: ignore[reportAny]

    return {
        "status": "success",
        "path": str(note_path),
        "title": note.title,
        "description": note.description,
        "message_to_user": f"You can find the note in: {str(note_path)}",
    }


GENERATE_NEW_NOTE_TOOL_SCHEMA: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "generateNewNote",
        "description": (
            "Generate a new note based on a prompt. "
            "The note MUST be a markdown file (.md)."
            "Pass the parameters directly (no nested object). "
            "Use only the following flat properties: title, description, keywords, text, path. "
            "Keywords must be a comma-separated string. "
            "title must be meaningful"
            "Path must be only the filename ending in .md."
            "DO NOT wrap the note in another object or repeat it elsewhere."
            "Respond only in valid JSON, nothing else."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "examples": ["Batman: The Dark Knight"]},
                "description": {
                    "type": "string",
                    "examples": ["Batman is a fictional superhero."],
                },
                "keywords": {
                    "type": "string",
                    "description": "Comma separated strings of keywords.",
                    "examples": ["batman", "superhero", "justice"],
                },
                "text": {
                    "type": "string",
                    "examples": ["# Batman: The Dark Knight\nBatman, ..."],
                },
                "path": {
                    "type": "string",
                    "pattern": r"^[\w.-]+\.md$",
                    "examples": ["batman.md", "ai.md"],
                },
            },
            "required": ["title", "description", "keywords", "text", "path"],
            "additionalProperties": False,
        },
    },
}
