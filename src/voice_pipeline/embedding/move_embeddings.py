"""Move embedded vectors and source text into the Chroma staging folders."""

from pathlib import Path
import shutil

from voice_pipeline.config import (
    CHROMA_TEXT,
    CHROMA_VECTORIZED,
    TRANSCRIPTS_EMBEDDED,
    TRANSCRIPTS_PENDING,
    ensure_data_dirs,
)


def move_files() -> None:
    ensure_data_dirs()
    parse_folders = [TRANSCRIPTS_EMBEDDED, TRANSCRIPTS_PENDING]
    try:
        for folder in parse_folders:
            folder_path = Path(folder)
            for file_path in folder_path.iterdir():
                if not file_path.is_file():
                    print("Unknown File! exiting...")
                    return

                print(f"{file_path} moving...")
                if folder == TRANSCRIPTS_EMBEDDED:
                    shutil.move(str(file_path), CHROMA_VECTORIZED)
                elif folder == TRANSCRIPTS_PENDING:
                    shutil.move(str(file_path), CHROMA_TEXT)
                else:
                    raise Exception("Destination folders cannot be found!")
    except OSError as e:
        print(f"An error occurred while moving the file: {e}")
