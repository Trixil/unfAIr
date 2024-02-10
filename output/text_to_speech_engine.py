
# Importing required libraries
import os
import sys
import pyttsx3

# Initiate the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the speech such as voice, speed, volume etc.
# Set default voice to the system default voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set default speed to moderate speed
engine.setProperty('rate', 150)

# Set default volume to maximum
engine.setProperty('volume', 1.0)

# Function to convert text to speech
def text_to_speech(user_text):
    # Passing the text to the engine
    engine.say(user_text)
    # Blocking method which will not return until the queued say() calls have completed the speech
    engine.runAndWait()

# This is a skeleton of the code. Further functionalities and improvements will be added later.
