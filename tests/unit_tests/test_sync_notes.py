from pathlib import Path

from pytest import fixture

from notes import _sync_notes


@fixture()
def init_data_folder(tmp_path: Path) -> Path:
    return tmp_path


class FakeLlm:
    def invoke(self, query: str, system_prompt: str = "", **kwargs) -> str:
        return query


def test_sync_notes_should_return_no_items_to_parse_when_no_txt_files(
    init_data_folder: Path,
):
    llm = FakeLlm()
    result = _sync_notes(llm, init_data_folder)

    assert result == "No items to parse"


def test_sync_notes_should_return_success_message_when_txt_files_are_parsed(
    init_data_folder: Path,
):
    notes_dir = init_data_folder
    (notes_dir / "file_to_parse.txt").write_text("Hello World")

    llm = FakeLlm()
    result = _sync_notes(llm, init_data_folder)

    assert result == "All existing .txt in notes_dir where parsed successfully"
    assert len(list(notes_dir.rglob("*.md"))) == 1
