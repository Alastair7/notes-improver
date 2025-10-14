from pathlib import Path
from textwrap import dedent

import pytest

from utils.files import search_files_with_keywords


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords: [hola, mundo]
    ---

    # Title
     """)

    md_no_keywords_with_content = dedent("""\
            # Title
            """)

    (tmp_path / "hola_mundo.md").write_text(md_structure)

    return tmp_path


def test_search_files_with_keywords_should_return_empty_list(init_data_folder: Path):
    keywords = ["adiós", "test"]
    result = search_files_with_keywords(init_data_folder, keywords)

    assert result == []


def test_search_files_with_keywords_should_return_file_if_any_keyword_exists(
    init_data_folder: Path,
):
    keywords = ["hola", "mundo"]

    result = search_files_with_keywords(path=init_data_folder, keywords=keywords)

    assert result == [init_data_folder / "hola_mundo.md"]
