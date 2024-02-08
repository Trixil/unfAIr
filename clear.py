import json
import os

def clear():
    with open('postbox.json', 'r') as json_file:
        postbox = json.load(json_file)

    postbox["00"]["usercontent"] = "Your objective is to create a text to speech program that speaks in a character's voice with voice samples located in C:/Program Files (x86)/Steam/steamapps/common/Umineko/sound/voice/09. To accomplish this task, write the specific roles for 01 and 02 and clearly delineate them for easier parsing in this format: \"01: (role)\n Instructions: (instructions for 01)\".";
    postbox["01"]["usercontent"] = "";
    postbox["02"]["usercontent"] = "";
    postbox["scribe"]["usercontent"] = "";

    postbox["00"]["cachedmessage"] = "";
    postbox["01"]["cachedmessage"] = "";
    postbox["02"]["cachedmessage"] = "";
    postbox["scribe"]["cachedmessage"] = "";

    with open('postbox.json', 'w') as json_file:
        json.dump(postbox,json_file, indent=3)

    open('user_documentation.txt', 'w').close()

    open('00_output.txt', 'w').close()
    open('01_output.txt', 'w').close()
    open('02_output.txt', 'w').close()
    open('scribe_output.txt', 'w').close()
    '''
    # List of files and directories to keep
    keep_list = ['__pycache__', 'cachedrequests', 'misc', 'clear.py', 'sequencer.py', 'features.txt', 'messenger.py', 'postbox.json', 'user_documentation.txt']

    # Get the current directory
    current_dir = os.getcwd()

    # Get the list of files and directories in the current directory
    items = os.listdir(current_dir)

    # Iterate over the items in the directory
    for item in items:
        # Check if the item is not in the keep list
        if item not in keep_list:
            # If it's a file, delete it
            if os.path.isfile(item):
                os.remove(item)
                print(f"Deleted file: {item}")
            # If it's a directory, recursively delete it
            elif os.path.isdir(item):
                for root, dirs, files in os.walk(item, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                        print(f"Deleted file: {os.path.join(root, name)}")
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                        print(f"Deleted directory: {os.path.join(root, name)}")
                os.rmdir(item)
                print(f"Deleted directory: {item}")


    '''