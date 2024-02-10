
import os

def locate_and_extract_samples(directory):
    try:
        files = os.listdir(directory)
        return [file for file in files if file.endswith(('.wav', '.mp3'))]
    except Exception as e:
        return str(e)

print(locate_and_extract_samples('C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09'))
