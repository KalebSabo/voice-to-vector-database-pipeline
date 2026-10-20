# voice-to-vector-database-pipeline

A custom local voice to vector database pipeline.

## Features

- OpenAI Whisper transcription
- Qwen 3 embedding model (via Ollama)
- ChromaDB vector database

## Project layout

```
.
├── src/voice_pipeline/     # Application package
│   ├── config.py           # Shared paths & model settings
│   ├── whisper/            # Audio → text
│   ├── embedding/          # Text → vectors
│   └── vectorstore/        # Vectors → ChromaDB
├── scripts/                # Thin CLI entry points
├── data/                   # Runtime artifacts (gitignored contents)
│   ├── audio/              # pending/ · transcribed/
│   ├── transcripts/        # base/ · pending/ · embedded/
│   └── chroma/             # docs staging + storage/
├── pyproject.toml
└── requirements.txt
```

## Requirements

- Python 3.10+
- OpenAI Whisper `large-v3`
- Ollama model `qwen3-embedding:8b`
- ChromaDB

```bash
pip install -e .
# or
pip install -r requirements.txt
```

## How to run

1. Place audio files (e.g. `.mp3`) in `data/audio/pending/`
2. Transcribe:

   ```bash
   python scripts/transcribe.py
   # or: voice-transcribe
   ```

3. Copy a transcribed `.txt` from `data/transcripts/base/<name>/` into `data/transcripts/pending/`
4. Embed:

   ```bash
   python scripts/embed.py
   # or: voice-embed
   ```

5. Store in ChromaDB:

   ```bash
   python scripts/store.py
   # or: voice-store
   ```

You should now have a persistent vector database under `data/chroma/storage/` with embeddings and documents from the recording.

## Naming conventions

Transcript and vector filenames change as files move through the pipeline stages. Paths are centralized in `src/voice_pipeline/config.py`.

## Current progress

Working on automation instead of manually executing each stage.
