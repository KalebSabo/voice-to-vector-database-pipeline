"""Centralized paths and settings for the voice-to-vector pipeline."""

from pathlib import Path

# Project root: src/voice_pipeline/config.py → parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# --- Audio (Whisper input / archived audio) ---
AUDIO_PENDING = PROJECT_ROOT / "data" / "audio" / "pending"
AUDIO_TRANSCRIBED = PROJECT_ROOT / "data" / "audio" / "transcribed"

# --- Transcripts (Whisper output → embedding → Chroma handoff) ---
TRANSCRIPTS_BASE = PROJECT_ROOT / "data" / "transcripts" / "base"
TRANSCRIPTS_PENDING = PROJECT_ROOT / "data" / "transcripts" / "pending"
TRANSCRIPTS_EMBEDDED = PROJECT_ROOT / "data" / "transcripts" / "embedded"

# --- ChromaDB staging & persistence ---
CHROMA_DOCS = PROJECT_ROOT / "data" / "chroma" / "docs"
CHROMA_TEXT = CHROMA_DOCS / "text"
CHROMA_VECTORIZED = CHROMA_DOCS / "vectorized"
CHROMA_COLLECTED_TEXT = CHROMA_DOCS / "collected_text"
CHROMA_COLLECTED_VECTORS = CHROMA_DOCS / "collected_vectors"
CHROMA_STORAGE = PROJECT_ROOT / "data" / "chroma" / "storage"

# --- Models ---
WHISPER_MODEL = "large-v3"
EMBEDDING_MODEL = "qwen3-embedding:8b"
CHROMA_COLLECTION = "Test"


def ensure_data_dirs() -> None:
    """Create expected data directories if they do not exist."""
    for path in (
        AUDIO_PENDING,
        AUDIO_TRANSCRIBED,
        TRANSCRIPTS_BASE,
        TRANSCRIPTS_PENDING,
        TRANSCRIPTS_EMBEDDED,
        CHROMA_TEXT,
        CHROMA_VECTORIZED,
        CHROMA_COLLECTED_TEXT,
        CHROMA_COLLECTED_VECTORS,
        CHROMA_STORAGE,
    ):
        path.mkdir(parents=True, exist_ok=True)
