from messenger import request
import json
import subprocess

def executor(code):
    print('current code: ' + code)
    start_index = 0

    end_index = len(code)

    if(code.find("```python\n") != -1):
        start_index = code.find("```python\n") + 9
        end_index = code.rfind("```")-3
    code = code[start_index: end_index].strip()
    start_quote = code.find('#') 
    end_quote = code.find('\n', start_quote + 1)
    if(start_quote != -1 & end_quote != -1):
        extracted_string = code[start_quote+2:end_quote]
        print('extracted_string is ' + extracted_string)
        with open(extracted_string, 'w') as docs_file:
            docs_file.write(code)
    

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

while True:
    instructions = request("00", postbox["00"]["systemcontent"], postbox["00"]["usercontent"], 1)
    print(instructions)

    postbox_dict = postbox

    # Get the number of items in the dictionary (which represents the JSON object)
    wizardcount = len(postbox_dict) - 2

    for i in range(1, wizardcount + 1):
        start_index = instructions.find(str(i).zfill(2))
        end_index = instructions.find(str(i+1).zfill(2)) if i < wizardcount else len(instructions)
    
        # Extract the substring starting from the position of "01:"
        if start_index != -1:
            selected_substring = instructions[start_index+3:end_index].strip()
            postbox[str(i).zfill(2)]["usercontent"] = selected_substring
            print(f"Substring for Wizard {i}:\n{selected_substring}\n")
        else:
            print(f"The string '{i:02d}:' was not found.")

    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)

    codelist = []
    for i in range(1, wizardcount + 1):

        with open('user_documentation.txt', 'r') as docs_file:
            docs = docs_file.read()
        print('docs:' + docs)
        if(docs == ''):
            message = 'No documentation written yet.\n'
        header_docs = 'Current documentation stored in user_documentation.txt:\n' + docs + '\n'
        id = str(i).zfill(2)

        postbox[id]["usercontent"] = header_docs + postbox[id]["usercontent"]
        with open(file_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)

        code = request(id, postbox[id]["systemcontent"], postbox[id]["usercontent"], 1)
        executor(code)
        postbox["scribe"]["usercontent"] = header_docs + postbox[id]["usercontent"]
        with open(file_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)
        docs = request("scribe", postbox["scribe"]["systemcontent"], postbox["scribe"]["usercontent"], 1)
    
        with open('user_documentation.txt', 'w') as docs_file:
            docs_file.write(docs)

        print(docs)

    postbox["00"]["usercontent"] = postbox["00"]["usercontent"] + '\n' + 'An iteration has been finished. Here is the documentation for it:\n' + docs
    with open(file_path, 'w') as json_file:
        json.dump(postbox, json_file, indent=3)

