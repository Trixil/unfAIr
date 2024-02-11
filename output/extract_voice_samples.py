
import os

def extract_voice_samples(directory):
    # List all files in the given directory
    file_list = os.listdir(directory)
    
    # Filter list to only include .ogg files (assuming voice samples are in .ogg format)
    audio_files = [file for file in file_list if file.endswith('.ogg')]
    
    total_files = len(audio_files)
    
    # Print out total number of audio files
    print(f"Total number of audio files: {total_files}")
    
    # Return list of audio files
    return audio_files

# Replace the below directory with the actual directory path
directory = 'C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09'

extract_voice_samples(directory)
