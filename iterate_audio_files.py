port os

directory = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"
audio_files = []

for filename in os.listdir(directory):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        audio_files.append(filename)

with open(os.path.join(directory, "audio_files.txt"), "w") as file:
    for audio_file in audio_files:
        file.write(audio_file + "\n")
