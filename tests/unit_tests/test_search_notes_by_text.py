from pathlib import Path
from textwrap import dedent

import pytest

from cli.search_notes_by_text import _search_notes_by_text


@pytest.fixture
def init_test_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hello, world]
    ---

    # Title
    Hey! This text exists in two notes
     """)

    out_dir = tmp_path / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    (tmp_path / out_dir / "note_with_matching_text.md").write_text(md_structure)

    return tmp_path


def test_search_notes_by_text_should_return_not_found_message_when_text_does_not_match_any_file(init_test_data_folder: Path):

    result = _search_notes_by_text("Test that does not exist", init_test_data_folder)

    assert result == "Not found any notes with the provided text"


def test_search_notes_by_text_should_return_notes_that_contains_the_text(
    init_test_data_folder: Path,
):
    out_dir = init_test_data_folder / "out" 

    result = _search_notes_by_text("Hey! This text exists in two notes", out_dir)
    assert result == "note_with_matching_text.md"
