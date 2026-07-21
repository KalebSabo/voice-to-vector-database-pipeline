from pathlib import Path    # used to get file paths
import os
import shutil
from main import EMBEDDED_FOLDER, PENDING_FOLDER

CHROMA_VECTOR_FOLDER = Path("./chromadb/docs/vectorized")
CHROMA_TEXT_FOLDER = Path("./chromadb/docs/text")

def move_files():
    parse_folders = [EMBEDDED_FOLDER, PENDING_FOLDER]
    try:
        for folder in parse_folders:
            folder_path = Path(folder)
            for file_path in folder_path.iterdir():
                if file_path.is_file():
                    file_name = file_path
                    print(f"{file_name} moving...")
                    if folder == EMBEDDED_FOLDER:
                        shutil.move(file_name, CHROMA_VECTOR_FOLDER)
                    elif folder == PENDING_FOLDER:
                        shutil.move(file_name, CHROMA_TEXT_FOLDER)
                    else:
                        raise Exception("Destination folders cannot be found!")
                else:
                    print("Unknown File! exiting...")
                    return
        return
    except IOError as e:
        print(f"An error occurred while moving the file: {e}")
