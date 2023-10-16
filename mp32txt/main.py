import whisper

model = whisper.load_model("base")
result = model.transcribe("mp32txt/test.m4a")
print(result)