import whisper

model = whisper.load_model("base")


def recognize(audio_paths, language="en"):
    try:
        result = model.transcribe(audio_paths[0], language=language)
        return {'transcript': result["text"]}
    except RuntimeError as e:
        print("RuntimeError: ", e)
        return {'error': "An exception occurred", 'transcript': ""}
