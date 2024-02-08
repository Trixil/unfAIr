import os

directory_path = "C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09"

def access_directory(directory_path):
    try:
        os.listdir(directory_path) 
        print("Directory accessed successfully.")
        task_status = "Completed"
    except Exception as e:
        print("Could not access the directory. Error - ", str(e))
        task_status = "In Progress"

access_directory(directory_path)
