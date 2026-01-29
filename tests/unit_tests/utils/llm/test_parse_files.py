from dataclasses import dataclass
from pathlib import Path
from pytest import fixture

from utils.llm import parse_files


@fixture()
def init_data_folder(tmp_path: Path) -> Path:
    (tmp_path / "file_to_parse.txt").write_text("Hello World")
    (tmp_path / "file_to_parse_2.txt").write_text("Parse me with a LLM")

    return tmp_path


@dataclass()
class FakeLlm:
    def invoke(self, query: str, system_prompt: str = "", **kwargs) -> str:
        return query


def test_parse_files_should_generate_markdown_files_when_parsed(init_data_folder: Path):
    llm = FakeLlm()
    notes_dir = init_data_folder

    files_to_parse = notes_dir.rglob("*.txt")

    parse_files(llm, list(files_to_parse))

    assert len(list(notes_dir.glob("*.md"))) == 2
