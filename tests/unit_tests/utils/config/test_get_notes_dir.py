from pathlib import Path

from pytest import MonkeyPatch, fixture, raises

from utils.config import get_notes_dir


@fixture()
def init_tmp_test_folder(tmp_path: Path) -> Path:
    return tmp_path / "notes"


def test_get_notes_dir_should_throw_error_if_enviroment_variable_is_not_set(
    monkeypatch: MonkeyPatch,
):
    monkeypatch.delenv("NOTES_DIR", raising=False)
    with raises(ValueError):
        get_notes_dir()


def test_get_notes_dir_should_create_directory_if_it_not_exists(
    init_tmp_test_folder: Path, monkeypatch: MonkeyPatch
):
    monkeypatch.setenv("NOTES_DIR", str(init_tmp_test_folder))

    result = get_notes_dir()

    assert result == init_tmp_test_folder
