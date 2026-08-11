"""Load staged text + embeddings into a persistent ChromaDB collection."""

from pathlib import Path
import ast
import json
import shutil

import chromadb

from voice_pipeline.config import (
    CHROMA_COLLECTED_TEXT,
    CHROMA_COLLECTED_VECTORS,
    CHROMA_COLLECTION,
    CHROMA_STORAGE,
    CHROMA_TEXT,
    CHROMA_VECTORIZED,
    ensure_data_dirs,
)

client = chromadb.PersistentClient(path=str(CHROMA_STORAGE))
collection = client.get_or_create_collection(name=CHROMA_COLLECTION)


def main() -> None:
    ensure_data_dirs()

    for file_path in CHROMA_TEXT.iterdir():
        if not file_path.is_file():
            continue

        document = file_path.read_text(encoding="utf-8")
        print(f"Reading... {document[:50]}")

        for vector_file_path in CHROMA_VECTORIZED.iterdir():
            if vector_file_path.stem != f"{file_path.stem}_vectorized":
                continue

            raw_text = vector_file_path.read_text(encoding="utf-8").strip()
            vector = []

            if raw_text.startswith("[") and raw_text.endswith("]"):
                print("Detected bracketed list. Parsing with JSON...")
                try:
                    vector = json.loads(raw_text)
                except json.JSONDecodeError:
                    print("JSON parsing failed. Trying Python literal evaluation...")
                    vector = ast.literal_eval(raw_text)

            print("\n--- Success! ---")
            print(f"Data type: {type(vector)}")
            print(f"First item type: {type(vector[0])}")
            print(f"Total dimensions: {len(vector)}")
            print(f"Vector preview: {vector[:5]}")
            collection.add(
                ids=[file_path.stem],
                embeddings=[vector],
                documents=[document],
                metadatas=[{"source": str(file_path), "author": "Author"}],
            )
            shutil.move(str(file_path), CHROMA_COLLECTED_TEXT)
            shutil.move(str(vector_file_path), CHROMA_COLLECTED_VECTORS)

    print("Done...")
    print(f"Total Docs in DB: {collection.count()}")


if __name__ == "__main__":
    main()
