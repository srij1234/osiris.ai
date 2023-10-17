import whisper

def transcribe_audio(input_file, output_file):
    model = whisper.load_model("base")
    text = model.transcribe(input_file)['text']
    
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(text)

def main():
    input_file = "mp32txt/test.mp3"
    output_file = "mp32txt/text.txt"
    
    transcribe_audio(input_file, output_file)

if __name__ == "__main__":
    main()
