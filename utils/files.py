from pathlib import Path


def get_files_with_text(path: Path, text: str) -> list[Path]:
    return [file for file in path.glob("*.md") if text in file.read_text()]
