
import os

def extract_voice_samples(directory):
    audio_files = []
    total_files = 0
    
    try:
        # List all files in the given directory
        file_list = os.listdir(directory)
        
        # Filter list to only include .ogg files (assuming voice samples are in .ogg format)
        audio_files = [file for file in file_list if file.endswith('.ogg')]
        
        total_files = len(audio_files)
        
    except FileNotFoundError:
        print(f"Error: The directory {directory} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access the files in {directory}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    
    # Print out total number of audio files
    print(f"Total number of audio files: {total_files}")
    
    # Return list of audio files
    return audio_files

# Replace the below directory with the actual directory path
directory = 'C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09'

extract_voice_samples(directory)
