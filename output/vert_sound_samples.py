
# This is an analysis script, please replace with the actual content of 'convert_sound_samples.py'
# The code below is based on the provided documentation and may not match with the actual content of 'convert_sound_samples.py'

# Import necessary libraries
from pydub import AudioSegment
import os

# Create a function to convert audio files
def convert_audio_files(directory_path):    

    # Iterate through all the files in the directory
    for filename in os.listdir(directory_path):

        # Check if file is audio and not in '.mp3' or '.wav' format
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            continue

        # Convert audio file to '.mp3' format
        else:
            try:
                # Load file using pydub
                sound = AudioSegment.from_file(os.path.join(directory_path, filename))

                # Export file in '.mp3' format
                sound.export(os.path.join(directory_path, filename.split('.')[0] + '.mp3'), format="mp3")

                # Delete the original file
                os.remove(os.path.join(directory_path, filename))

            # Handle exception
            except Exception as e:
                print(f"Error converting file {filename}. Error: {str(e)}")

# Call the function       
convert_audio_files('your_directory_path')
