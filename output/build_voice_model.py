
# Use the gtts library for text to speech
from gtts import gTTS
  
def build_voice_model(transcript):
    """
    Function to generate speech based on text inputs using Google's Text-to-Speech technology.

    Parameters:
    transcript (str): The text to be converted to speech.

    Returns:
    audio_file: the audio file of the transcribed text
    """

    # Create an object of gTTS
    tts = gTTS(text=transcript, lang='en', slow=False)
    
    # Name of the audio file
    audio_filename = "speech.ogg"

    # Saving the speech audio into a file
    tts.save(audio_filename)

    # Return the audio file
    return audio_filename
