import os
import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio_files(audio_files):
    recognizer = sr.Recognizer()
    transcriptions = []
    for audio_file in audio_files:
        audio_data = AudioSegment.from_wav(audio_file)
        audio_data.export("temp.wav", format="wav")
        with sr.AudioFile("temp.wav") as source:
            audio = recognizer.record(source)
            try:
                transcription = recognizer.recognize_google(audio)
                transcriptions.append((audio_file, transcription))
            except sr.UnknownValueError:
                transcriptions.append((audio_file, "Google Speech Recognition could not understand audio"))
            except sr.RequestError as e:
                transcriptions.append((audio_file, "Could not request results from Google Speech Recognition service; {0}".format(e)))
    os.remove("temp.wav")
    return transcriptions
