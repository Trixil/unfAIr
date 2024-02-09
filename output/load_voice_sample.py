
import librosa

def load_voice_sample(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, sr=22050)
        return audio, sample_rate
    except Exception as e:
        print(f"An error occurred while loading voice sample: {e}")
        return None
