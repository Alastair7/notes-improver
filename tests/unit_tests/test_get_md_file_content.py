from pathlib import Path
from textwrap import dedent

import pytest

from utils.files import get_md_file_content


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

    (tmp_path / "1.md").write_text(md_structure)
    (tmp_path / "2.md").write_text(md_no_keywords_with_content)

    (tmp_path / "empty.md").write_text("")

    return tmp_path


def test_get_md_file_content_empty_text_should_not_have_keywords_nor_text(
    init_data_folder: Path,
):
    result = get_md_file_content(init_data_folder / "empty.md")

    assert result.keywords == set()
    assert result.text == ""


def test_get_md_file_content_when_no_keywords_should_return_empty_keywords_and_existing_content(
    init_data_folder: Path,
):
    file_path = init_data_folder / "2.md"

    result = get_md_file_content(file_path)

    assert result.keywords == set()
    assert result.text == "# Title"


def test_get_md_file_content_should_show_keywrods(init_data_folder: Path):
    file_path = init_data_folder / "1.md"

    result = get_md_file_content(file_path)

    assert result.keywords == {"hola", "mundo"}
