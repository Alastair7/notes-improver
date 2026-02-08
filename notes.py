import datetime
import logging
import os
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

from utils.bot import ConversationalBot
from utils.config import get_notes_dir
from utils.files import (
    get_all_md_files_content,
    get_files_to_parse,
    get_files_with_text,
    search_files_with_keywords,
)
from utils.llm import GeminiLlm, LlmBase, Message, parse_files

load_dotenv()

WELCOME_MESSAGE = """
    == NOTARIUM == 

Notarium is a Generative AI bot with context about your notes.
    """


logger = logging.getLogger(__name__)

Path.mkdir(Path(".logs"), exist_ok=True)
log_filename = f".logs/log_{datetime.date.today().isoformat()}.log"
logging.basicConfig(
    format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
    filename=log_filename,
    encoding="utf-8",
    level=logging.INFO,
)

logging.getLogger("httpx").setLevel(logging.ERROR)


@click.group()
def main():
    pass


@main.command("search-by-text")
@click.argument("text")
def search_notes_by_text(text: str):
    notes_dir = get_notes_dir()
    click.echo(_search_notes_by_text(text, notes_dir))


@main.command("search-by-keywords")
@click.argument("keywords")
def search_notes_by_keywords(keywords: str):
    notes_dir = get_notes_dir()

    keywords_list = keywords.split(",")
    click.echo(_search_notes_by_keywords(keywords_list, notes_dir))


@main.command("sync")
def sync_notes():
    notes_dir = get_notes_dir()
    logger.info("Starting notes syncing for path: %s", notes_dir)
    client = OpenAI(
        base_url=os.getenv("GEMINI_BASE_URL"), api_key=os.getenv("GEMINI_API_KEY")
    )
    llm = GeminiLlm(client)

    click.echo(_sync_notes(llm=llm, notes_dir=notes_dir))


@main.command("chat")
def chat_with_model():
    """Ask Notarium, a Generative AI bot, anything related to your notes."""
    notes_dir = get_notes_dir()
    client = OpenAI(
        base_url=os.getenv("GEMINI_BASE_URL"), api_key=os.getenv("GEMINI_API_KEY")
    )

    llm = GeminiLlm(client)
    click.echo(message=WELCOME_MESSAGE)

    _chat_with_model(llm, notes_dir)


def _chat_with_model(llm: LlmBase, notes_dir: Path) -> None:
    bot = ConversationalBot(llm=llm)
    notes_context = get_all_md_files_content(notes_dir)
    bot.add_notes_context(notes_context)

    while True:
        prompt: str = click.prompt(text=click.style("Prompt", fg="green", bold=True))  # pyright: ignore[reportAny]
        user_message = Message("user", prompt)
        bot_message = bot.ask_model(user_message)

        notarium_name = click.style("Notarium:", fg="cyan", bold=True)

        click.echo(f"{notarium_name} {bot_message}\n")


def _sync_notes(llm: LlmBase, notes_dir: Path) -> str:
    files_to_parse = get_files_to_parse(notes_dir)
    logger.info("Found %s notes to parse", len(files_to_parse))
    if not files_to_parse:
        return "No items to parse"

    parse_files(llm=llm, files_to_parse=files_to_parse)

    return "All existing .txt in notes_dir where parsed successfully"


def _search_notes_by_text(text: str, notes_dir: Path):
    matching_files = get_files_with_text(notes_dir, text)

    if not matching_files:
        return "Not found any notes with the provided text"

    result = [note.relative_to(notes_dir).as_posix() for note in matching_files]

    return "\n".join(result)


def _search_notes_by_keywords(keywords: list[str], notes_dir: Path):
    matching_files = search_files_with_keywords(notes_dir, keywords)

    if not matching_files:
        return "Not found any notes with the provided keywords"

    result = [note.relative_to(notes_dir).as_posix() for note in matching_files]
    return "\n".join(result)


if __name__ == "__main__":
    main()
