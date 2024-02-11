
def assemble_samples(samples):
    """
    Function to simulate the assembly of voice samples into a single audio file.

    Parameters:
    samples (list): List of filenames of the .ogg audio files.

    Returns:
    final_audio (str): A single, combined .ogg audio file name.
    """
    # Simulates the assembly of samples by joining filenames
    final_audio = ', '.join(samples)
    
    return final_audio
