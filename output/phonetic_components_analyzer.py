
import nltk
from nltk.corpus import cmudict 

# Initialize the CMU Dict
nltk.download('cmudict')
phonetic_dict = cmudict.dict()

def phonetic_components(word):
    """
    This function accepts a word as a string, 
    breaks it down into its phonetic components using the CMU Pronouncing Dictionary,
    and returns the phonetic components as a list.
    """
    try:
        phonemes = phonetic_dict[word.lower()]
        return phonemes
    except:
        return "Word not found in CMU Pronunciation Dictionary."

