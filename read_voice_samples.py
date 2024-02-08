import os

# Specify the directory path
directory = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"

# Get the list of file names in the directory
voice_samples = os.listdir(directory)

# Print the file names
print(voice_samples)
