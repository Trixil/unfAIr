import os

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

file_path = "path/to/text_file.txt" # replace with the actual file path
text = read_text_file(file_path)
print(text)
