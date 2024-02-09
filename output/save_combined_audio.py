import os
import wave
from pydub import AudioSegment

# Function to combine multiple audio files into a single WAV file
def combine_audio_files(input_folder, output_file):
    # Get the list of audio files present in the input folder
    audio_files = [f for f in os.listdir(input_folder) if f.endswith(".wav")]

    if len(audio_files) == 0:
        print("No audio files found in the specified input folder.")
        return

    # Create an empty list to store the audio segments
    audio_segments = []

    # Load each audio file and append its audio segment to the list
    for audio_file in audio_files:
        audio_path = os.path.join(input_folder, audio_file)
        audio_segment = AudioSegment.from_wav(audio_path)
        audio_segments.append(audio_segment)

    # Concatenate the audio segments into a single audio segment
    combined_audio = audio_segments[0]
    for i in range(1, len(audio_segments)):
        combined_audio += audio_segments[i]

    # Export the combined audio as a WAV file
    combined_audio.export(output_file, format="wav")

# Specify the input folder and output file name
input_folder = "path/to/folder/containing/audio/files"
output_file = "combined_audio.wav"

# Call the function to combine the audio files
combine_audio_files(input_folder, output_file)
