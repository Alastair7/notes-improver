from pathlib import Path

import click

# from peek import peek
from utils.config import get_notes_dir
from utils.files import get_files_with_text


@click.group()
def main():
    pass


@main.command("search-by-text")
@click.argument("text")
def search_notes_by_text(text: str):
    notes_dir = get_notes_dir()
    click.echo(_search_notes_by_text(text, notes_dir))


def _search_notes_by_text(text: str, notes_dir: Path):
    print("TEXT:", text)
    matching_files = get_files_with_text(notes_dir, text)

    if not matching_files:
        return "Not found any notes with the provided text"

    result = [note.name for note in matching_files]

    return "\n".join(result)


if __name__ == "__main__":
    main()
