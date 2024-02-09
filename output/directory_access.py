import os

def list_ogg_files(directory):
    # List all files in the directory
    files_in_directory = os.listdir(directory)
    
    # Filter out the '.ogg' files
    ogg_files = [file for file in files_in_directory if file.endswith('.ogg')]
    
    return ogg_files

# test the function
print(list_ogg_files('09'))
