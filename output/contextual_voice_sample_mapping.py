
# Placeholder lists
word_list = ['hello', 'my', 'name', 'is', 'john']
context_list = ['goodbye', 'your', 'nickname', 'are', 'doe']
audio_files = ['audio1.ogg', 'audio2.ogg', 'audio3.ogg', 'audio4.ogg', 'audio5.ogg']

def match_word_to_sample_context(sentence):
    """
    Function to breakdown the sentence into words and match each word with its corresponding voice sample considering context.

    Parameters:
    sentence (str): The sentence to be spoken.

    Returns:
    matched_samples (list): List of filenames of the audio files corresponding to the words in the sentence.
    """
    # Break down the sentence into words
    sentence_words = sentence.split()

    # Initialize matched_samples list
    matched_samples = []

    # Initialize a variable to keep track of the previous word
    previous_word = None
  
    # Loop through each word in the sentence
    for word in sentence_words:
        
        # If the word in the sentence matches a word in the word_list
        if word in word_list:
            # and if the previous word matches the context of this word
            index = word_list.index(word)
            if previous_word == context_list[index]:
                matched_samples.append(f"{audio_files[index]}_context.ogg")
            else:
                matched_samples.append(audio_files[index])
        
        # Keep track of this word as the previous word for the next iteration
        previous_word = word
  
    return matched_samples
