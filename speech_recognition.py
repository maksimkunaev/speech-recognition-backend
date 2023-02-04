import whisper

model = whisper.load_model("base")


def recognize(audio_paths):
    result = model.transcribe(audio_paths[0], language="en")

    return {'transcript': result["text"]}
