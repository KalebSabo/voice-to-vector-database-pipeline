import whisper
from pathlib import Path    # used to get file paths
import os
import shutil


PENDING_FOLDER = "./audio/pending"
TRANSCRIBED_FOLDER = "./audio/base"  # global variable of the file location for the already transcribed audio files

def transcribe():

    folder_path = Path(PENDING_FOLDER)
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            file_name = file_path
            print(f"{file_name} moving...")
        else:
            print("Unknown File! exiting...")
            return    
        audio = file_path
        out_dir = Path("./base") / audio.stem
        out_dir.mkdir(parents=True, exist_ok=True)

        model = whisper.load_model("large-v3") # Feel free to change this model to suit your needs

        result = model.transcribe(      # please change these settings to suit your needs, but I find it works well for unscripted voice lines
            str(audio),
            no_speech_threshold=0.6,
            condition_on_previous_text=False,
            temperature=0.0,
            compression_ratio_threshold=2.4
        )
        # Write all formats
        import whisper.utils as wu
        writer = wu.get_writer("all", str(out_dir))
        writer(result, str(audio))
        print(f"{audio} has been transcribed")
        shutil.move(audio, TRANSCRIBED_FOLDER)
    

def main():
    try:
        transcribe()    # We are checking if the transcription will work
    except Exception as e:
        print(f"Error occured!: {e}")
        


main()