
import numpy as np
import soundfile as sf

def wav_to_numpy(filepath):
    '''Reads a .wav file and converts it to a numpy array
    Args: 
    filepath (str) - The path to the .wav file
    Returns:
    ndarray: numpy array with the content of the .wav file'''

    data, samplerate = sf.read(filepath)
    return data
