import os

def collect_wav_files(directory):
    wav_files = []

    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    # Iterate over the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a .wav file
            if file.endswith('.wav'):
                # Capture the path of the file
                wav_files.append(os.path.join(root, file))
    
    return wav_files

directory = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"
wav_files = collect_wav_files(directory)

print(wav_files)
