
import os

def get_ogg_files(directory_path):
    """
    Check if a directory exists and if any .ogg files are present in the directory.
    If there are .ogg files, the function returns a list of their absolute paths.
    """
    # Check if the directory exists.
    if not os.path.exists(directory_path):
        return None
    
    # Initialize an empty list to hold the .ogg files.
    ogg_files = []
    
    # Loop through every file in the directory.
    for file in os.listdir(directory_path):
        # Check if the file ends with .ogg.
        if file.endswith('.ogg'):
            # If it does, get the absolute path of the file and append it to the ogg_files list.
            ogg_files.append(os.path.abspath(os.path.join(directory_path, file)))
            
    # Return the list of .ogg files.
    return ogg_files
