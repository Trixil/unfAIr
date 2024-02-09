
def matchPhonemesToVoiceSamples(phonemes, voiceSamples):
    matchedVoiceSamples = []
    
    for phoneme in phonemes:
        if phoneme in voiceSamples:
            matchedVoiceSamples.append(voiceSamples[phoneme])
        else:
            print(f"Warning: Phoneme '{phoneme}' does not have a corresponding voice sample.")
    
    return matchedVoiceSamples
