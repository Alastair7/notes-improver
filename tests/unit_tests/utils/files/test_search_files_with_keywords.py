from pathlib import Path
from textwrap import dedent

import pytest

from utils.files import search_files_with_keywords


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hello, world]
    ---

    # Title
     """)

    (tmp_path / "hello_world.md").write_text(md_structure)

    return tmp_path


def test_search_files_with_keywords_should_return_empty_list_when_files_do_not_match_keywords(init_data_folder: Path):
    keywords = ["keywords", "that", "dont", "exist"]
    result = search_files_with_keywords(init_data_folder, keywords)

    assert result == []


def test_search_files_with_keywords_should_return_file_if_any_keyword_exists(
    init_data_folder: Path,
):
    keywords = ["hello", "coffee"]

    result = search_files_with_keywords(path=init_data_folder, keywords=keywords)

    assert result == [init_data_folder / "hello_world.md"]
