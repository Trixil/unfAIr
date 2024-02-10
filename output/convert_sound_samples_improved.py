
import os
from pydub import AudioSegment

def convert_samples(directory_path, output_format):
    conversion_errors = []

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        if not filename.endswith('.mp3') and not filename.endswith('.wav'): # If the file is not in .mp3 or .wav format
            try:
                # Convert the file to the desired format using PyDub
                sound = AudioSegment.from_file(os.path.join(directory_path, filename))
                sound.export(os.path.join(directory_path, filename.split('.')[0] + '.' + output_format), format=output_format)
                os.remove(os.path.join(directory_path, filename)) # remove the original file
            except Exception as e:
                conversion_errors.append(filename)

    if len(conversion_errors) == 0:
        return "Conversion successful for all files"
    else:
        return "Conversion unsuccessful for following files: " + ", ".join(conversion_errors)

print(convert_samples('C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09/', 'mp3'))
