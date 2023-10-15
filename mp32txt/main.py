import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_text(mp3_file_path):
    # Load the MP3 file and convert it to WAV format
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export("temp.wav", format="wav")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the WAV audio file
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)

    # Use the recognizer to convert speech to text
    try:
        text = recognizer.recognize_google(audio_data)  # You can choose other engines as well
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == '__main__':
    mp3_file_path = 'test.mp3'
    text = mp3_to_text(mp3_file_path)
    with open("text.txt","w",encoding='utf-8') as f:
        f.write(text)