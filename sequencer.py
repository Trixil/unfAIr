from messenger import request
from clear import clear
import json
import subprocess
import os
import textwrap

clear()
user_input = ""
def executor(code):
    start_index = code.find('Code:\n')

    end_index = len(code)
    
    code = code[start_index:end_index]

    if(code.find("```python\n") != -1):
        start_index = code.find("```python\n") + 9
        end_index = code.rfind("```")-3
    code = code[start_index: end_index].strip()
    start_quote = code.find('#') 
    end_quote = code.find('\n', start_quote + 1)

    if(start_quote != -1 & end_quote != -1):
        extracted_string = code[start_quote+2:end_quote]
        with open(extracted_string, 'w') as docs_file:
            docs_file.write(code)

def update_documentation(file_path, file_description):

    file_path_line = f"File name: {file_path}\n"
    file_description_line = f"Content: {file_description}\n"

    with open("user_documentation.txt", "r") as f:
        lines = f.readlines()

    filefound = False
    with open("user_documentation.txt", "r+") as f:
        for line in lines:
            if ((line.strip("\n") != file_path_line) & (filefound == False)):
                f.write(line)
            if (line.strip("\n") == file_path_line):
                filefound = True
                print('filefound=true')
            if((filefound == True) & (line.strip("\n") == "******")):
                filefound = False
                f.write(file_path_line + file_description_line)

        f.truncate()

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file '{file_path}'.")
        return None

# Specify the file path
file_path = "postbox.json"

# Read the JSON file
postbox = read_json_file(file_path)

iteration = 1
while True:
    instructions = request("00", postbox["00"]["usercontent"], 1)
    postbox_dict = postbox

    # Get the number of items in the dictionary (which represents the JSON object)
    wizardcount = len(postbox_dict) - 2

    for i in range(1, wizardcount + 1):
        start_index = instructions.find(str(i).zfill(2))
        end_index = instructions.find(str(i+1).zfill(2)) if i < wizardcount else len(instructions)
    
        # Extract the substring starting from the position of "01:"
        if start_index != -1:
            selected_substring = instructions[start_index+3:end_index].strip()
            postbox[str(i).zfill(2) + ' Overseer']["usercontent"] = selected_substring
            print(f"Substring for Wizard {i}:\n{selected_substring}\n")
        else:
            print(f"The string '{i:02d}:' was not found.")

    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)

    for i in range(1, 3):
        id = str(i).zfill(2)
        postbox[id + ' Overseer']["systemcontent"] += postbox[id + ' Overseer']["usercontent"]
        with open(file_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)

        overseer_instruction = request(id + ' Overseer', 'Update the to-do list with each conversation with ' + id + ' and output it in your To-do field', 1)
        finalpass = False
        while(finalpass == False):
            wizardresponse = request(id, overseer_instruction, 1)
            fetch_index = wizardresponse.find('Fetch:')
            fetchpath = wizardresponse[fetch_index+7:wizardresponse.find('\n', fetch_index)]

            overseer_instruction = request(id + ' Overseer', wizardresponse, 1)
            finalpass = (overseer_instruction.find('Completed: Yes') or overseer_instruction.find('Completed: YES'))
            if(fetchpath != 'None'):
                with open(fetchpath, 'r') as code_file:
                    requested_code = code_file.read()
                    overseer_instruction += '\nContents of ' + fetchpath +'\n' + requested_code

        code = wizardresponse
        # opening and printing docs
        with open('user_documentation.txt', 'r') as docs_file:
            docs = docs_file.read()
        
        # checking if docs is empty and appending it to wizard input string
        if(docs == ''):
            docs = 'No documentation written yet.\n'
        header_docs = 'Current documentation stored in user_documentation.txt:\n' + docs + '\n'

        input_text = request("scribe", header_docs + code, 1)
        file_name_start = input_text.find("File name: ") + len("File name: ")
        file_name_end = input_text.find("\n", file_name_start)
        file_name = input_text[file_name_start:file_name_end]
        
        content_start = input_text.find("Content: ") + len("Content: ")
        content = input_text[content_start:]

        with open('user_documentation.txt', 'a') as docs_file:
            docs_file.write(input_text)
            docs_file.close()
        update_documentation(file_name, content)
    
    
    with open('user_documentation.txt', 'r') as docs_file:
        docs = docs_file.read()
    postbox["00"]["usercontent"] = postbox["00"]["usercontent"] + '\n' + 'An iteration has been finished. Here is the documentation for it:\n' + docs
    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)