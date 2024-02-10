
import os
import glob
import soundfile as sf

def read_audio_files(directory):
    # os.path.join provided for file path compatibility
    directory_path = os.path.join(directory, '*.wav') 

    audio_files = glob.glob(directory_path)

    for audio_file in audio_files:
        data, samplerate = sf.read(audio_file)
        # Do something with data and samplerate

# Define the directory path
directory = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"

# Call the function
read_audio_files(directory)
