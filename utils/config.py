import os
from pathlib import Path


def get_notes_dir() -> Path:
    notes_dir = os.getenv("NOTES_DIR")

    if not notes_dir:
        raise Exception("NOTES_DIR environment variable is not set")

    notes_path = Path(notes_dir)

    if not notes_path.exists():
        notes_path.mkdir(parents=True, exist_ok=True)

    return notes_path 
