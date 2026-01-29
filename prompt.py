import os

from dotenv import load_dotenv
from openai import OpenAI

from utils.config import get_notes_dir
from utils.files import get_all_md_files_content, get_md_file_content
from utils.llm import GeminiLlm, Message


def main():
    load_dotenv()
    notes_dir = get_notes_dir()
    notes = get_all_md_files_content(notes_dir)

    client = OpenAI(
        base_url=os.getenv("GEMINI_BASE_URL"), api_key=os.getenv("GEMINI_API_KEY")
    )

    llm = GeminiLlm(client)

    messages = [Message(role="user", content="What are these notes about")]

    print(llm.invoke(query=None, messages=messages, notes=notes))


if __name__ == "__main__":
    main()
