
import random

def match_phonemes(phonemes, voice_samples):
    """
    This function takes in a list of phonemes and a dictionary of voice samples matched to each phoneme.
    The function returns a list of voice samples matching the input phonemes in their respective order.
    
    Parameters:
    phonemes (list): A list of phonemes.
    voice_samples (dict): A dictionary where keys are phonemes and values are lists of corresponding voice samples.
    
    Returns:
    matched_samples (list): A list of selected voice samples in the order of the input phonemes.
    """
    matched_samples = []
    for phoneme in phonemes:
        if phoneme in voice_samples:
            # If multiple voice samples exist for the same phoneme, randomly select one.
            if len(voice_samples[phoneme]) > 1:
                sample = random.choice(voice_samples[phoneme])
            else:
                sample = voice_samples[phoneme][0]
            matched_samples.append(sample)
        else:
            matched_samples.append(None)  # If no voice sample matches a given phoneme, append None
    return matched_samples
