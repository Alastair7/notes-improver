from pathlib import Path

import pytest

from utils.files import get_files_with_text


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    (tmp_path / "1.md").write_text("# Title\nSome text here.")
    (tmp_path / "2.md").write_text("Just some text.")
    (tmp_path / "3.md").write_text("Another markdown file.")
    (tmp_path / "4.txt").write_text("Just a text file")

    return tmp_path


def test_get_files_with_text_without_matches(init_data_folder: Path):
    result = get_files_with_text(
        init_data_folder, "This text does not exist in the text files."
    )

    assert result == []

def test_get_files_with_text_with_matches(init_data_folder: Path):
    result = get_files_with_text(init_data_folder, "text")

    assert set(result) == {init_data_folder / "1.md", init_data_folder / "2.md"}

def test_get_files_with_text_search_only_md_filetypes(init_data_folder: Path):
    result = get_files_with_text(init_data_folder, "text")

    assert "4.txt" not in set(result) 

