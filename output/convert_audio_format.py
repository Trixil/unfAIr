
from pydub import AudioSegment
import os

def convert_to_mp3(wav_file_path, target_folder):
    audio = AudioSegment.from_wav(wav_file_path)
    mp3_file_path = os.path.join(target_folder, os.path.basename(wav_file_path).replace('.wav', '.mp3'))
    audio.export(mp3_file_path, format="mp3")

def convert_audio_files_in_dir(dir_path, target_format="mp3"):
    supported_formats = ["wav", "mp3"]
    if target_format not in supported_formats:
        raise ValueError(f"Unsupported target format: {target_format}. Choose from {supported_formats}")
    for file_name in os.listdir(dir_path):
        if not file_name.endswith('.' + target_format):
            current_file_path = os.path.join(dir_path, file_name)
            convert_to_mp3(current_file_path, dir_path)

convert_audio_files_in_dir('path_to_your_directory')
