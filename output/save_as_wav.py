import wave

def save_as_wav(file_name, frames, sample_width, sample_rate, num_channels):
    with wave.open(file_name, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b''.join(frames))

# Usage example
frames = []  # generate your audio frames here
sample_width = 2  # adjust according to your audio data
sample_rate = 44100  # adjust according to your audio data
num_channels = 1  # adjust according to your audio data
save_as_wav('output.wav', frames, sample_width, sample_rate, num_channels)
