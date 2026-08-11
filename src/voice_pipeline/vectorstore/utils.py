"""Helpers for inspecting and managing the ChromaDB collection."""

import chromadb

from voice_pipeline.config import CHROMA_COLLECTION, CHROMA_STORAGE

client = chromadb.PersistentClient(path=str(CHROMA_STORAGE))
collection = client.get_or_create_collection(name=CHROMA_COLLECTION)


def peek_collection() -> None:
    """Print the number of documents in the collection."""
    print(f"collection #: {collection.count()}")


def remove_document(doc: str) -> None:
    """Remove a document by id."""
    collection.delete(ids=[doc])


if __name__ == "__main__":
    peek_collection()
