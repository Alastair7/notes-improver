from pathlib import Path
import click

from utils.files import get_files_with_text

@click.command()
@click.argument('text')
def search_notes_by_text(text):
    out_folder = Path.cwd() / "out"

    matching_files = get_files_with_text(out_folder, text)

    if not matching_files:
        click.echo("Not found any notes with the provided text")
        return

    return click.echo(str(matching_files))

