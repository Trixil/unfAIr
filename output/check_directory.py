
import os, glob

def check_directory_and_list_files(path):
    if os.path.exists(path):
        if os.listdir(path): # if directory is not empty
            files = glob.glob(path+'/*.ogg') # list all .ogg files
            return files
        else:
            return 'Directory exists but is empty.'
    else:
        return 'Path does not exist.'

path = 'C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09'
check_directory_and_list_files(path)
