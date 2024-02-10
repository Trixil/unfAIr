
import os
import librosa
import numpy as np
from pocketsphinx import AudioFile, get_model_path
from exceptions import FileOpeningError, SoundProcessingError

def extract_phonetic_data(file_path):
    # Check if file exists.
    if not os.path.exists(file_path):
        raise FileOpeningError(file_path)
        
    # Load sound file
    try:
        y, sr = librosa.load(file_path, sr=None)
    except Exception as e:
        raise SoundProcessingError(str(e))

    frame_size = 5 * sr
    overlap = 0.5 * frame_size
    frames = librosa.util.frame(y, frame_length=int(frame_size), hop_length=int(overlap)).T
    model_path = get_model_path()

    # Transcribe each frame using CMU Sphinx
    transcriptions = []
    for frame in frames:
        decoder = AudioFile(audio_file=frame, lm=False, keyphrase='hello', kws_threshold=1e-20, model_path=model_path)
        result = decoder.hyp().hypstr
        transcriptions.append(result)

    # Return the transcriptions
    return transcriptions
