
# Placeholder lists
word_list = ['hello', 'my', 'name', 'is', 'john']
audio_files = ['audio1.ogg', 'audio2.ogg', 'audio3.ogg', 'audio4.ogg', 'audio5.ogg']

def match_word_to_sample(sentence):
    """
    Function to breakdown the sentence into words and match each word with its corresponding voice sample.

    Parameters:
    sentence (str): The sentence to be spoken.

    Returns:
    matched_samples (list): List of filenames of the audio files corresponding to the words in the sentence.
    """
    # Break down the sentence into words
    sentence_words = sentence.split()

    # Initialize matched_samples list
    matched_samples = []
  
    # Loop through each word in the sentence
    for word in sentence_words:
        
        # If the word in the sentence matches a word in the word_list, append the corresponding audio file to the matched_samples list
        if word in word_list:
            index = word_list.index(word)
            matched_samples.append(audio_files[index])
  
    return matched_samples
