# script2.py

import os

# Read the content of user_documentation.txt
with open('user_documentation.txt', 'r') as file:
    content = file.read()

# Get the filenames and their location from the content
filenames = [line.split()[0] for line in content.split('\n') if line.startswith('-')]

# Print the filenames and their location
for filename in filenames:
    print(filename)

# Save the filenames and their location to a script file
script_code = '\n'.join(filenames)
with open('script2_output.py', 'w') as file:
    file.write(script_code)

# Execute the script file
os.system('python script2_output.py')