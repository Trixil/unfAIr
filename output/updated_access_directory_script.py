
import os
import glob

def get_ogg_file_count(directory_path):
    if os.path.exists(directory_path): 
        ogg_files = glob.glob(os.path.join(directory_path, "*.ogg"))
        return len(ogg_files)

    return None

print(get_ogg_file_count('C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09'))  # replace with the actual directory path
