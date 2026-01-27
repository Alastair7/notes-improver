import os

from openai import OpenAI

from utils.config import get_notes_dir
from utils.files import get_md_file_content
from utils.llm import GeminiLlm


def main():
    notes_dir = get_notes_dir()
    # Add function to get all of the notes content
    note = get_md_file_content(notes_dir / "test_note.md")
    notes = [note]

    client = OpenAI(
        base_url=os.getenv("GEMINI_BASE_URL"), api_key=os.getenv("GEMINI_API_KEY")
    )

    llm = GeminiLlm(client)

    print(llm.invoke("How many notes are right now?", notes=notes))


if __name__ == "__main__":
    main()
