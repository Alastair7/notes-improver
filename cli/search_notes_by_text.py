import sys
from pathlib import Path

import click
from peek import peek

peek.prefix = "PEEK: "
peek.output = "stderr"
peek.show_line_number = True

from utils.files import get_files_with_text


@click.command()
@click.argument("text")
def search_notes_by_text(text):
    # Crear función de utilidad que busque en configuración la carpeta de notas
    click.echo(_search_notes_by_text(text, ))


def _search_notes_by_text(text: str, notes_dir: Path):
    # Decidir cómo hacer el sistema de ficheros
    print("notes dir", notes_dir)
    matching_files = get_files_with_text(notes_dir, text)

    print(matching_files, file=sys.stderr)

    if not matching_files:
        return "Not found any notes with the provided text"

    result = [note.name for note in matching_files]

    return '\n'.join(result)
