import whisper

model = whisper.load_model("base")
text = model.transcribe("mp32txt/test.mp3")['text']
# text=text[text]

with open("mp32txt/text.txt","w",encoding='utf-8') as f:
    f.write(text)