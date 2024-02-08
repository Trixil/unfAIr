import os
import mutagen

directory_path = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"

def enumerate_audio_files(directory_path):
    audio_files_data = { "filenames": [], "metadata": [] } # To store filenames and metadata of audio files

    for filename in os.listdir(directory_path):
        if filename.endswith((".mp3", ".wav", ".flac")):
            audio_files_data["filenames"].append(filename)

            file_path = os.path.join(directory_path, filename)
            file_metadata = mutagen.File(file_path, easy=True)

            audio_files_data["metadata"].append(dict(file_metadata))

    return audio_files_data

enumerate_audio_files(directory_path)
