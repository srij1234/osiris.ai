import os
from pytube import YouTube
from ..mp32txt.main import transcribe_audio

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

if __name__ == "__main__":
    audio_file = download_youtube_audio('https://www.youtube.com/watch?v=v4t0E3S1N1k')
    
    if audio_file:
        transcribe_audio(audio_file, "text.txt")
