
import nltk
from nltk.corpus import cmudict

# Make sure to download the 'cmudict' package
nltk.download('cmudict')

def breakdown_text(text):
    """
    Breakdown the input text into its individual phonemes.
    
    Parameters:
    text (string): The input string text.
    
    Returns:
    phonemes (list): The list of individual phonemes of the input text.
    """
    
    # Initialize the cmudict phoneme converter
    phoneme_converter = cmudict.dict()

    # Breakdown the text into word tokens
    word_tokens = nltk.word_tokenize(text)

    # Breakdown the word tokens into phonemes
    phonemes = []
    for word in word_tokens:
        # Ignore the word if it's not in the cmudict
        if word.lower() in phoneme_converter:
            word_phonemes = phoneme_converter[word.lower()][0]  # Just use the first pronunciation option
            phonemes.extend(word_phonemes)

    return phonemes
