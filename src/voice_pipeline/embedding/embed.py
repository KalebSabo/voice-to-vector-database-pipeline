"""Embed pending transcript text with Ollama."""

from pathlib import Path
import shutil

import ollama

from voice_pipeline.config import (
    EMBEDDING_MODEL,
    TRANSCRIPTS_EMBEDDED,
    TRANSCRIPTS_PENDING,
    ensure_data_dirs,
)
from voice_pipeline.embedding.move_embeddings import move_files


def main() -> None:
    ensure_data_dirs()
    folder_path = Path(TRANSCRIPTS_PENDING)

    for file_path in folder_path.iterdir():
        if not file_path.is_file():
            print("Unknown File! exiting...")
            return

        file_content = file_path.read_text(encoding="utf-8")
        print(f"{file_path} read...")
        print("------------------")
        print(f"File preview: '{file_content[:50]}...'")

        response = ollama.embed(
            model=EMBEDDING_MODEL,
            input=file_content,
        )

        vector = response["embeddings"][0]

        print(f"Vector dimensions: {len(vector)}")
        print(f"First 5 numbers of the vector: {vector[:5]}")
        print("------------------")

        try:
            file_vector_name = TRANSCRIPTS_EMBEDDED / f"{file_path.stem}_vectorized.txt"
            with open(file_vector_name, "x", encoding="utf-8") as file:
                file.write(str(vector))
            print(f"{file_path} vectorized successfully")
        except OSError as e:
            print(f"An error occurred while creating the file: {e}")

    if input("Would you like to move all embeddings and text to Chromadb? : ").lower() == "y":
        move_files()


if __name__ == "__main__":
    main()
