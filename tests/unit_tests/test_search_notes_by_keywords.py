from pathlib import Path
from notes import _search_notes_by_keywords
from textwrap import dedent
import pytest

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

    (help_dir / "helper.md").write_text(md_structure)
    (tmp_path / "note_with_matching_keywords.md").write_text(md_structure)

    return tmp_path

def test_search_notes_by_keywords_should_not_found_notes_if_not_exist(init_test_data_folder: Path):
    result = _search_notes_by_keywords(['keywords','not','exist'], init_test_data_folder)

    assert result == "Not found any notes with the provided keywords"

def test_search_notes_by_keywords_should_found_notes(init_test_data_folder: Path):
    result = _search_notes_by_keywords(['hello','world'], init_test_data_folder)

    first_note = result.splitlines()[0]

    assert first_note == "note_with_matching_keywords.md"

def test_search_notes_by_keywords_should_found_notes_inside_directories(init_test_data_folder: Path):
    expected = "note_with_matching_keywords.md\nhelp/helper.md"
    result = _search_notes_by_keywords(['hello','world'], init_test_data_folder)

    assert result in expected 

