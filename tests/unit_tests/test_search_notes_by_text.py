from pathlib import Path
from textwrap import dedent

import pytest

from notes import _search_notes_by_text


@pytest.fixture
def init_test_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hello, world]
    ---

    # Title
    Hey! This text exists in two notes
     """)

    help_dir = tmp_path / "help"
    help_dir.mkdir(parents=True, exist_ok=True)

    (help_dir / "helper.md").write_text("# Help Function\nHello helper")
    (tmp_path / "note_with_matching_text.md").write_text(md_structure)

    return tmp_path


def test_search_notes_by_text_should_return_not_found_message_when_text_does_not_match_any_file(
    init_test_data_folder: Path,
):
    result = _search_notes_by_text("Test that does not exist", init_test_data_folder)

    assert result == "Not found any notes with the provided text"


def test_search_notes_by_text_should_return_notes_that_contains_the_text(
    init_test_data_folder: Path,
):
    result = _search_notes_by_text(
        "Hey! This text exists in two notes", init_test_data_folder
    )
    assert result == "note_with_matching_text.md"


def test_search_notes_by_text_should_return_note_if_it_is_in_a_folder(
    init_test_data_folder: Path,
):
    result = _search_notes_by_text("Hello helper", init_test_data_folder)

    assert "help/helper.md" == result
