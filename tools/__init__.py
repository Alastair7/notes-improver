from openai.types.chat import ChatCompletionToolParam
from tools.list_notes import LIST_NOTES_TOOL_SCHEMA, list_notes
from tools.read_notes import READ_NOTE_TOOL_SCHEMA, read_note_content


TOOLS: list[ChatCompletionToolParam] = [
    READ_NOTE_TOOL_SCHEMA,
    LIST_NOTES_TOOL_SCHEMA,
]

TOOL_REGISTRY = {
    "readNoteContent": read_note_content,
    "listNotes": list_notes,
}
