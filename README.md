# voice-to-vector-database-pipeline
A custom voice to vector database pipeline.

## Features:
- OpenAI Whisper transcribing audio files
- Qwen 3 embedding model
- ChromaDB vector database

## Requirements
- Ensure you have:
    - OpenAI Whisper large-v3
    - qwen3-embedding:8b
    - chromadb

## How-to:
- Upload audio files (such as .mp3) into the *audio* folder
- Run ```python3 ./whisper/transcribe.py```
- Move a transcribed .txt file from the *base* folder into the *pending* folder of /embedding
- Run ```python3 ./embedding/main.py```
- Run ```python3 ./chromadb/main.py```
# Now you should have a vector database, named chroma_storage, with vector embeddings and text documents from a recording! 

#### Naming conventions
- Please note that the transcribed text document will be changing names throughout the pipeline 

## Current Progress
Working on automation instead of manually executing files. 
