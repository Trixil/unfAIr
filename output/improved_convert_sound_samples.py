
import os
from pydub import AudioSegment

def convert_samples(voice_samples_dir='C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09/', output_format='mp3'):
    error_files = []

    # Iterate through each file in the voice samples directory
    for filename in os.listdir(voice_samples_dir):
        if not filename.endswith(f'.{output_format}') and (filename.endswith('.mp3') or filename.endswith('.wav')): 
            # If the file is not in .mp3 or .wav format or in the target output format
            try:
                # Convert the file to the output format using PyDub
                sound = AudioSegment.from_file(os.path.join(voice_samples_dir, filename))
                sound.export(os.path.join(voice_samples_dir, f'{filename.split(".")[0]}.{output_format}'), format=output_format)
                os.remove(os.path.join(voice_samples_dir, filename)) # remove the original file
            except Exception as e:
                print(f"Error converting file: {filename}")
                print(str(e))
                error_files.append(filename)  # add the problematic file to the error_files list

    return (len(error_files) == 0, error_files)  # returns True and an empty list if no errors.
