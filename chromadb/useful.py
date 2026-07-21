import chromadb 
from pathlib import Path

db_path = Path("./chroma_storage")

client = chromadb.PersistentClient(path=str(db_path))

collection = client.get_collection(name="Test")

def peek_collection():      # Peek at all collections and count

    print(f"collection #: {collection.count()}")

    #print(f"first 5 rows: {collection.peek()}")

def remove_document(doc):
    collection.delete(ids=[doc])        # Remove collections

if __name__ == "__main__":
    peek_collection() # change this to either peek_collection() or remove_document(doc)