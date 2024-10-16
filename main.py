import whisper

model = whisper.load_model("turbo")
result = model.transcribe("paulin.mp3")
print("TRANSCRIÇÃO: " + result["text"])
