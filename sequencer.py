from messenger import request
from clear import clear
import json
import subprocess
import os
import textwrap

output_dir = "output/"

print("Current working directory changed to", os.getcwd())
clear()
user_input = ""

def filename_return(response):
    filename_start_index = response.find('File name: ')+11
    filename_end_index = response.find('\n', filename_start_index+1)
    if((filename_start_index != -1) and (filename_end_index == -1)):
        filename_end_index = len(response)
    if(filename_start_index == -1):
        print('Error: Could not find file name. Here is the response:\n' + response)
        return 'NULL'
    filename = response[filename_start_index:filename_end_index]
    print('filename: ' + filename)
    return filename

def executor(response):
    
    unnamed_code_flag = 0
    filename = filename_return(response)

    code_start_index = response.find('Code:\n```python\n')+16
    code_end_index = response.find('```', code_start_index+1)
    if((code_start_index == -1) or (code_end_index == -1)):
        print('Error: Could not find code. Here is the response:\n' + response)
        code = ''
    else:
        code = response[code_start_index:code_end_index]
        print('code\n' + code)

        if(filename == 'NULL'):
            unnamed_code_flag = 1
        else:
            with open(output_dir + filename, 'w') as wizardcode:
                wizardcode.write(code)

    return [code, unnamed_code_flag]

def update_documentation(file_path, file_description):

    file_path_line = f"File name: {file_path}"
    file_description_line = f"Content: {file_description}"

    with open(output_dir + "user_documentation.txt", "r") as f:
        lines = f.readlines()

    filefound = False
    with open(output_dir + "user_documentation.txt", "w") as f:
        for line in lines:
            if ((line.strip("\n") != file_path_line) and (filefound == False)):
                f.write(line)
            if (line.strip("\n") == file_path_line):
                filefound = True
                print('filefound=true')
            if((filefound == True) and (line.strip("\n") == "******")):
                filefound = False
                f.write(file_path_line + file_description_line)

        f.truncate()

def fetcher(response):
    if(response.find('Fetch: None') == -1):
        fetch_start_index = response.find('Fetch:')+7
        fetch_end_index = response.find('\n', fetch_start_index)
        if((fetch_start_index == -1) and (fetch_end_index == -1)):
            print('Error: Could not find fetch path. Here is the response:\n' + response)
        
        fetch_filename = response[fetch_start_index:fetch_end_index]
        if((fetch_start_index != -1) and (fetch_end_index == -1))
            fetch_filename = response[fetch_start_index:]
        print('fetch: ' + fetch_filename)
        if(fetch_filename == 'user_documentation.tx'):
            fetch_filename = 'user_documentation.txt'
        with open(output_dir + fetch_filename, 'r') as fetch_file:
            toreturn = fetch_file.read()
        return [fetch_filename, toreturn]
    else:
        return ['None', 'No file requested']

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
overseer_initial = ['','']
overseer_initial[0] = postbox["01 Overseer"]["systemcontent"]
overseer_initial[1] = postbox["02 Overseer"]["systemcontent"]
while True:
    postbox["01 Overseer"]["systemcontent"] = overseer_initial[0]
    postbox["02 Overseer"]["systemcontent"] = overseer_initial[1]

    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)
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
            postbox[str(i).zfill(2) + ' Overseer']["systemcontent"] += selected_substring
        else:
            print(f"The string '{i:02d}:' was not found.")

    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)

    for i in range(1, 3):
        id = str(i).zfill(2)
        with open(file_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)

        overseer_instruction = request(id + ' Overseer', 'Update the to-do list with each conversation with ' + id + ' and output it in your To-do field', 1)
        to_do_end_index = overseer_instruction.find('Current instruction for you:\n')
        to_do = overseer_instruction[0:to_do_end_index]
        finalpass = False
        header_docs = ''
        overseer_instruction += 'Current documentation stored in user_documentation.txt:\nNo documentation written yet.\n'
        while(finalpass == False):
            wizardresponse = request(id, overseer_instruction + header_docs, 1)

            [code, unnamed_code_flag] = executor(wizardresponse)
            fetchcontent = fetcher(wizardresponse)
            fetch_file_name = fetchcontent[0]
            fetch_file_content = fetchcontent[1]

            fetch_start_index = wizardresponse.find('Fetch: ' + fetch_file_name)
            fetch_end_index = fetch_start_index + len('Fetch: ' + fetch_file_name) + 1
            clean_wizardresponse = wizardresponse[0:fetch_start_index] + wizardresponse[fetch_end_index:]
            overseer_instruction = request(id + ' Overseer', clean_wizardresponse + to_do, 1)

            finalpass = (overseer_instruction.find('SEND CODE') != -1)
            to_do_end_index = overseer_instruction.find('Current instruction for you:\n')
            to_do = overseer_instruction[0:to_do_end_index]
            postbox[id + ' Overseer']["systemcontent"] = overseer_initial[i-1] + to_do
            overseer_instruction += '\nContents of ' + fetch_file_name +'\n' + fetch_file_content

            # opening and printing docs
            with open(output_dir + 'user_documentation.txt', 'r') as docs_file:
                docs = docs_file.read()
        
            # checking if docs is empty and appending it to wizard input string
            if(docs == ''):
                docs = 'No documentation written yet.\n'
            header_docs = 'Current documentation stored in user_documentation.txt:\n' + docs + '\n'

            input_text = request("scribe", header_docs + wizardresponse, 1)
            file_name_start = input_text.find("File name: ") + len("File name: ")
            file_name_end = input_text.find("\n", file_name_start)
            file_name = input_text[file_name_start:file_name_end]
        
            content_start = input_text.find("Content: ") + len("Content: ")
            content = input_text[content_start:]


            update_documentation(file_name, content)

            if(unnamed_code_flag == 1):
                with open(output_dir + file_name, 'w') as wizardcode:
                    wizardcode.write(code)
    
    with open(output_dir + 'user_documentation.txt', 'r') as docs_file:
        docs = docs_file.read()
    postbox["00"]["usercontent"] = postbox["00"]["usercontent"] + '\n' + 'An iteration has been finished. Here is the documentation for it:\n' + docs
    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)