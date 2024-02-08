import os

def directory_iterator(path):
    for filename in os.listdir(path):
        print(filename)
        
directory_iterator("C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09")
