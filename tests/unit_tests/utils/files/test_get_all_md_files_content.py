from pathlib import Path

import pytest

from utils.files import get_all_md_files_content


@pytest.fixture
def init_data_folder(tmp_path: Path) -> Path:
    _ = (tmp_path / "empty.md").write_text("")

    return tmp_path


def test_get_all_md_files_content_empty_file_is_ignored(init_data_folder: Path):
    notes = get_all_md_files_content(init_data_folder)

    assert len(notes) == 0
