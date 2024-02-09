
import helper_functions as hf

def trigger_speech_conversion(text: str) -> str:
    # This function converts a given text into speech representation

    # Process the text (convert text to phonemes using process_user_input function)
    phonemes = hf.process_user_input(text)

    # Perform the conversion here
    # For now, a simplistic conversion operation is implemented:
    # We convert each character in the phonemes string to binary representation,
    # join them and return as the speech_audio.
    speech_audio = ''.join([format(ord(i), '08b') for i in phonemes])
    
    return speech_audio
