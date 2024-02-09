
from gtts import gTTS
import os

def text_to_speech(text, lang='en', slow=False):
    speech = gTTS(text=text, lang=lang, slow=slow)
    speech.save('generated_speech.mp3')

# Running example
text = "Hello, this is a text to speech conversion demo"
text_to_speech(text)
