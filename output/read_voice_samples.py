import os

folder_path = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"

voice_samples = []

for file_name in os.listdir(folder_path):
    if file_name.endswith(".ogg"):
        voice_samples.append(file_name.split(".")[0])

print(voice_samples)
