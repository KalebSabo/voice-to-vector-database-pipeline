import chromadb
from pathlib import Path    # used to get file paths
import shutil
import json
import ast

TEXT_PATH = Path("./docs/text")
VECTORIZED_PATH = Path("./docs/vectorized")
DB_PATH = Path("./chroma_storage")
COLLECTED_TEXT_PATH = Path("./docs/collected_text")
COLLECTED_VECTORIZED_PATH = Path("./docs/collected_vectors")

VECTOR_EXT = "_vectorized.txt"

client = chromadb.PersistentClient(path=str(DB_PATH))

collection = client.get_or_create_collection(name="Test")

def main():
    
    for file_path in TEXT_PATH.iterdir():
        if file_path.is_file():
            file_name = file_path
            document = file_name.read_text(encoding='utf-8')
            print(f"Reading... {document[:50]}")
        for vector_file_path in VECTORIZED_PATH.iterdir():
            if vector_file_path.stem == f"{file_name.stem}_vectorized":
                vector_file_name = vector_file_path
                raw_text = vector_file_name.read_text(encoding='utf-8').strip()
                vector = []
    
                # The text includes brackets like a Python or JSON list: "[0.1, 0.2]"
                if raw_text.startswith('[') and raw_text.endswith(']'):
                    print("Detected bracketed list. Parsing with JSON...")
                    try:
                        # json.loads is the safest and fastest way to parse a string formatted as an array
                        vector = json.loads(raw_text)
                    except json.JSONDecodeError:
                        print("JSON parsing failed. Trying Python literal evaluation...")
                        # Fallback just in case it has weird Python-specific formatting
                        vector = ast.literal_eval(raw_text)

                print("\n--- Success! ---")
                print(f"Data type: {type(vector)}")
                print(f"First item type: {type(vector[0])}")
                print(f"Total dimensions: {len(vector)}")
                print(f"Vector preview: {vector[:5]}")
                collection.add(
                    ids=[file_name.stem],
                    embeddings=[vector],
                    documents=[document], 
                    metadatas=[{"source": f"{file_name}", "author": "Author"}] # Optional filters, change with your name
                )
                shutil.move(file_name, COLLECTED_TEXT_PATH)
                shutil.move(vector_file_name, COLLECTED_VECTORIZED_PATH)
                
            else:
                continue

        
    print("Done...")
    print(f"Total Docs in DB: {collection.count()}")
    return    

if __name__ == "__main__":
    main()
    
