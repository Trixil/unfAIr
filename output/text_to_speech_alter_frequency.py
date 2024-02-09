
import pyttsx3
import os 
from pydub import AudioSegment

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.sound = None
        

    def convert_text_to_speech(self, text):
        self.engine.save_to_file(text, 'speech.wav')
        self.engine.runAndWait()

        # create AudioSegment object from the wav file
        self.sound = AudioSegment.from_file('speech.wav')

    def alter_pitch(self, percentage):
        # Alter pitch up by a percentage
        if percentage > 0:
            self.sound = self.sound.speedup(playback_speed=(percentage/100)+1)
        # Alter pitch down by a percentage
        elif percentage < 0:
            self.sound = self.sound.slowdown(playback_speed=1-(abs(percentage)/100))
        
        file_handle = self.sound.export("altered_pitch_speech.wav", format="wav")

    def alter_frequency(self, percentage):
        # Alter frequency up by a percentage
        if percentage > 0:
            self.sound = self.sound.speedup(playback_speed=(percentage/100)+1)
            # Remove transitions between segments
            self.sound = self.sound.crossfade(0)
        # Alter frequency down by a percentage
        elif percentage < 0:
            self.sound = self.sound.slowdown(1-abs(percentage/100))
            # Remove transitions between segments
            self.sound = self.sound.crossfade(0)
        
        file_handle = self.sound.export("altered_frequency_speech.wav", format="wav")
