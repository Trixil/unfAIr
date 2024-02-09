import os

# Specify the directory path
directory = "/path/to/directory"

# Read all the files in the directory
files = os.listdir(directory)

# Process each file in the directory
for file in files:
    file_path = os.path.join(directory, file)
    
    # Customize your file processing logic here
    # ...

    # Example: print the file name
    print(file)

