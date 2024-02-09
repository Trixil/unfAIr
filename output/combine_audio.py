from pydub import AudioSegment

# List of audio files in the order of sentences
audio_files = ["audio1.wav", "audio2.wav", "audio3.wav"]

# Function to combine audio files
def combine_audio_files(input_files):
    combined_audio = AudioSegment.empty()

    for file in input_files:
        audio_segment = AudioSegment.from_wav(file)
        combined_audio += audio_segment

    return combined_audio

# Call the function to combine audio files
combined_audio = combine_audio_files(audio_files)

# Save the combined audio file
output_file = "output.wav"
combined_audio.export(output_file, format="wav")
