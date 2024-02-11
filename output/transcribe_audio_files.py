
import speech_recognition as sr
import ogg.vorbis 
import os 

def transcribe_audio_file(file_path):
    """Function to transcribe an audio file and timestamp each word """
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Exception Handling for file access issues
    try:
        file_checker = os.path.splitext(file_path)[1]
        if file_checker != '.ogg':
            raise Exception('File is not of .ogg type')
        
        # Reading Audio file as source
        # Listening the audio file and store in audio_text variable
        with ogg.vorbis.open(file_path, 'rb') as source:
            audio_text = r.listen(source)

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except PermissionError:
        print(f"You do not have permission to access the file {file_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred with the file {file_path}: {str(e)}")
        return None

    # Recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # Using google speech recognition
        print('Converting Audio Transcriptions from Google Speech Recognition')
        transcriptions = r.recognize_google(audio_text, show_all=True)
        print('Transcription completed')
        return transcriptions
    except sr.RequestError as e:
        print("Could not request results; check your internet connection")
        return None
        
