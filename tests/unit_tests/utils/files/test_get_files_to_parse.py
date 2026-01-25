from utils.files import get_files_to_parse
from pytest import fixture

from pathlib import Path


@fixture()
def init_data_folder(tmp_path: Path) -> Path:
    (tmp_path / "empty_file.txt").write_text("")

    return tmp_path

def test_get_files_to_parse_should_return_empty_list_if_no_txt_files_to_parse(init_data_folder: Path):
    notes_dir = init_data_folder

    output = get_files_to_parse(notes_dir)

    assert output == []

def test_get_files_to_parse_should_ignore_file_if_content_is_empty(init_data_folder: Path):
    notes_dir = init_data_folder
    empty_file = notes_dir / "empty_file.txt"

    output = get_files_to_parse(notes_dir)

    assert empty_file not in output

def test_get_files_to_parse_should_ignore_already_parsed_notes(init_data_folder: Path):
    notes_dir = init_data_folder

    parsed_note = (notes_dir / "already_parsed.md")
    parsed_note.write_text("## Content")

    ignore_note = (notes_dir / "already_parsed.txt")
    ignore_note.write_text("Content")

    to_parse_note = (notes_dir / "not_parsed.txt")
    to_parse_note.write_text("Parse me")

    output = get_files_to_parse(notes_dir)

    assert to_parse_note in output 
    assert [parsed_note, ignore_note] not in output

