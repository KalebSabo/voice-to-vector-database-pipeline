import ollama
from pathlib import Path    # used to get file paths
import shutil
import move_embeddings as mfiles

PENDING_FOLDER = Path("./pending")
EMBEDDED_FOLDER = Path("./embedded")

def main():

    folder_path = Path(PENDING_FOLDER)
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            
            file_name = file_path
            file_content = file_path.read_text(encoding='utf-8')
            print(f"{file_name} read...")
            print("------------------")
            # Prints the first 50 characters
            print(f"File preview: '{file_content[:50]}...'")

            response = ollama.embed(
                            model='qwen3-embedding:8b',     # Feel free to change this model to suit your needs
                            input=file_content,
                            )
    
            vector = response['embeddings'][0]
            
            print(f"Vector dimensions: {len(vector)}")
            print(f"First 5 numbers of the vector: {vector[:5]}")
            print("------------------")
            
            try:
                file_vector_name = f"{file_name.stem}_vectorized.txt"
                with open(str(file_vector_name), 'x', encoding='utf-8') as file:
                    file.write(str(vector))
                print(f"{file_name} vectorized successfully")
                shutil.move(file_vector_name, EMBEDDED_FOLDER)
            except IOError as e:
                print(f"An error occurred while creating the file: {e}")
            
            
        else:
            print("Unknown File! exiting...")
            return
    
    if input("Would you like to move all embeddings and text to Chromadb? : ") == 'y' or 'Y':
        mfiles.move_files()

    return
    


if __name__ == "__main__":
    main()
    