import os
from pytube import YouTube
# from ..mp32txt import transcribe_audio
import whisper
import ssl
import os
ssl._create_default_https_context = ssl._create_unverified_context

def download_youtube_audio(url, destination="yt2txt/"):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        
        out_file = audio.download(output_path=destination)
        
        base, ext = os.path.splitext(out_file)
        
        new_file = base + ".mp3"
        os.rename(out_file, "yt2txt/test.mp3")
        
        return "yt2txt/test.mp3"
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
def transcribe_audio(input_file, output_file):
    model = whisper.load_model("base")
    text = model.transcribe(input_file)['text']
    
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(text)
def transcribe():
    input_file = "yt2txt/test.mp3"
    output_file = "yt2txt/text.txt"
    
    transcribe_audio(input_file, output_file)
if __name__ == "__main__":
    os.remove("yt2txt/test.mp3")
    audio_file = download_youtube_audio('https://www.youtube.com/watch?v=5UcVVBXqj7Y')
    
    if audio_file:
        transcribe()
        
