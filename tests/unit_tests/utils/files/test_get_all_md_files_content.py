from pathlib import Path
from textwrap import dedent

import pytest

from utils.files import get_all_md_files_content


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hola, mundo]
    title: This is the title in metadata
    description: One liner description
    ---

    # Title

    This is a test note
     """)

    _ = (tmp_path / "empty.md").write_text("")
    _ = (tmp_path / "note_1.md").write_text(md_structure)
    _ = (tmp_path / "note_2.md").write_text(md_structure)

    return tmp_path


def test_get_all_md_files_content_empty_file_is_ignored(init_data_folder: Path):
    notes = get_all_md_files_content(init_data_folder)

    assert len(notes) == 2


def test_get_all_md_files_content_all_files_are_returned_as_list_of_notes(
    init_data_folder: Path,
):
    notes = get_all_md_files_content(init_data_folder)

    assert len(notes) == 2
    for note in notes:
        assert note.title == "This is the title in metadata"
