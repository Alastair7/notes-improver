from pathlib import Path
from textwrap import dedent

import pytest
from click.testing import CliRunner

from cli.search_notes_by_text import search_notes_by_text


@pytest.fixture
def init_test_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hello, world]
    ---

    # Title
    Hey! This text exists in two notes
     """)

    (tmp_path / "out" / "note_with_matching_text.md").write_text(md_structure)

    return tmp_path


def test_search_notes_by_text_should_return_not_found_message_when_text_does_not_match_any_file():
    runner = CliRunner()

    result = runner.invoke(
        search_notes_by_text,
        ["Text that does not exist in any file"],
        standalone_mode=False,
    )

    assert 0
    assert result.stdout == "Not found any notes with the provided text\n"


def test_search_notes_by_text_should_return_notes_that_contains_the_text(
    init_test_data_folder: Path,
):
    runner = CliRunner()

    with runner.isolated_filesystem(init_test_data_folder):
        result = runner.invoke(
            search_notes_by_text, ["Hey! This text exists in two notes"]
        )
        assert result.output == "note_with_matching_text.md"
