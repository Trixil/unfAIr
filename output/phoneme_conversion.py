
import nltk
from nltk.corpus import cmudict

def get_phonemes(text):
    # Load the CMU Pronouncing Dictionary
    transcriber = cmudict.dict()
    
    words = nltk.word_tokenize(text.lower())
    phonemes = []
    
    for word in words:
        if word in transcriber:
            phonemes.append(transcriber[word][0])   # We take the first pronunciation variant
    
    return phonemes
