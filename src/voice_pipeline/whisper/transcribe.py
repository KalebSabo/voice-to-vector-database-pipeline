"""Transcribe pending audio files with OpenAI Whisper."""

from pathlib import Path
import shutil

import whisper

from voice_pipeline.config import (
    AUDIO_PENDING,
    AUDIO_TRANSCRIBED,
    TRANSCRIPTS_BASE,
    WHISPER_MODEL,
    ensure_data_dirs,
)


def transcribe() -> None:
    ensure_data_dirs()
    folder_path = Path(AUDIO_PENDING)

    for file_path in folder_path.iterdir():
        if not file_path.is_file():
            print("Unknown File! exiting...")
            return

        print(f"{file_path} moving...")
        out_dir = TRANSCRIPTS_BASE / file_path.stem
        out_dir.mkdir(parents=True, exist_ok=True)

        model = whisper.load_model(WHISPER_MODEL)

        result = model.transcribe(
            str(file_path),
            no_speech_threshold=0.6,
            condition_on_previous_text=False,
            temperature=0.0,
            compression_ratio_threshold=2.4,
        )

        import whisper.utils as wu

        writer = wu.get_writer("all", str(out_dir))
        writer(result, str(file_path))
        print(f"{file_path} has been transcribed")
        shutil.move(str(file_path), AUDIO_TRANSCRIBED)


def main() -> None:
    try:
        transcribe()
    except Exception as e:
        print(f"Error occured!: {e}")


if __name__ == "__main__":
    main()
