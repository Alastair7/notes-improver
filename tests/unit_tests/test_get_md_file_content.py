from pathlib import Path
from textwrap import dedent

import pytest

from utils.files import get_md_file_content


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    md_structure = dedent("""\
    ---
    keywords:
    - hola
    - mundo
    ---

    # Title
     """)

    (tmp_path / "1.md").write_text(md_structure)

    (tmp_path / "empty.md").write_text("")

    return tmp_path


def test_get_md_file_content_empty_text_should_not_have_keywords_nor_text(
    init_data_folder: Path,
):
    result = get_md_file_content(init_data_folder / "empty.md")

    assert result.keywords == set()
    assert result.text == ""


# def test_get_md_file_content_show_keywrods(init_data_folder: Path):
#     content = (init_data_folder / "1.md").read_text()
#     file_path = init_data_folder / "1.md"

#     print(content)

#     result = get_md_file_content(file_path)

#     assert result.keywords == ["hola", "mundo"]
#     assert result.text == "# Title"

#     assert 0
