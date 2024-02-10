
import os
import shutil

def sort_audio_files(directory):
    os.chdir(directory)
    files = os.listdir()

    for file in files:
        # Assume initial part of file name before '_' is the character's name
        character_name = file.split('_')[0]
        character_folder = os.path.join(directory, character_name)

        # Check if a directory for the character exists, if not, create it
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

        # Move the audio file to the character's folder
        shutil.move(file, character_folder)
    
    return "Sorting of audio files is completed."

print(sort_audio_files('path/to/your/directory'))
