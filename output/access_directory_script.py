import os

# Function to access a specific directory
def access_directory(directory_path):
    try:
        os.chdir(directory_path)
        print(f"Directory {directory_path} accessed successfully")
    except FileNotFoundError:
        print("The directory does not exist")

# Test accessing the specific directory
access_directory("C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09")
