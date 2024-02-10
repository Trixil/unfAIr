
import os
from pydub import AudioSegment

def convert_samples():
    voice_samples_dir = 'C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09/' # the directory containing voice samples

    # Iterate through each file in the voice samples directory
    for filename in os.listdir(voice_samples_dir):
        if not filename.endswith('.mp3') and not filename.endswith('.wav'): # If the file is not in .mp3 or .wav format
            try:
                # Convert the file to .mp3 using PyDub
                sound = AudioSegment.from_file(os.path.join(voice_samples_dir, filename))
                sound.export(os.path.join(voice_samples_dir, filename.split('.')[0] + '.mp3'), format="mp3")
                os.remove(os.path.join(voice_samples_dir, filename)) # remove the original file
            except Exception as e:
                print("Error converting file: " + filename)
                print(str(e))

convert_samples()
