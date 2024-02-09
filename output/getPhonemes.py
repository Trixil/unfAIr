
def getPhonemes(text):
    # Extracts the characters from the text ignoring white spaces and punctuation
    char_list = [char for char in text if char.isalpha()]

    # For the sake of this basic implementation, we will just assign each character as its own phoneme
    phonemes = char_list

    return phonemes
