
import os

def list_voice_samples(directory):
    try:
        files_in_directory = os.listdir(directory)
        voice_samples = [file for file in files_in_directory if file.endswith('.wav')]
        return voice_samples
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

voice_samples_path = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"
voice_samples = list_voice_samples(voice_samples_path)
