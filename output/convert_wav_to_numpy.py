
def main(input_directory, output_directory):
    '''
    This function uses wav_to_numpy() to convert all .wav files in a directory into numpy arrays and saves them in a specified directory
    Input: input_directory - string - path of the directory containing .wav files
           output_directory - string - path of the directory where numpy arrays should be saved
    Output: None
    '''
    # making sure that the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # converting all .wav files in the directory
    for file_name in os.listdir(input_directory):
        # only process .wav files
        if file_name.endswith('.wav'):
            wav_data = wav_to_numpy(input_directory + '/' + file_name)
            if wav_data is not None:
                # saving numpy array to the output directory
                np.save(output_directory + '/' + file_name.replace('.wav', '.npy'), wav_data)
