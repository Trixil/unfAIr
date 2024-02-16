import json
import os

def clear():
    with open('postbox.json', 'r') as json_file:
        postbox = json.load(json_file)

    postbox["00"]["usercontent"] = "Your objective is to create a text to speech program that speaks in a character's voice by creating a voice model trained on voice samples located in Umineko/sound/voice/09. To accomplish this task, write the roles and instructions for 01 and 02 and clearly delineate them for easier parsing in this format: \"01: (role)\n Instructions: (instructions for 01)\".";
    for i in ["01", "02"]:
        postbox[i +" Overseer"]["systemcontent"] = f"Your name is {i} Overseer. You are collaborating with multiple LLMs to create requested software. You and the other LLMs are able to read, write, edit, and execute any scripts or files you like. You are given a \"To-do list\" which is a set of tasks for the LLM known as {i} to accomplish. In EVERY response you give, you must include \"To-do:\n(tasks and their progress)\", \"Current instruction for you:\n(immediate instruction for {i})\". In To-do, split up the tasks assigned to you into a series of many smaller tasks that build on each other. Include this same To-do list in every response of yours and simply update the completion progress on each task. You must output the up-to-date To-do list in every reponse. Every time {i} responds with code you asked for, make sure everything has been implemented for the current instruction. {i} does not have any memory except for the most updated documentation file; you must make everything explicit. Once you have marked every task in the to-do list as (Completed), write \"SEND CODE\" at the top of your response. {i} cannot execute code.";

    postbox["01"]["usercontent"] = "";
    postbox["02"]["usercontent"] = "";
    postbox["01 Overseer"]["usercontent"] = "";
    postbox["02 Overseer"]["usercontent"] = "";
    postbox["scribe"]["usercontent"] = "";
    postbox["logmessages"] = [];

    postbox["00"]["cachedmessage"] = "";
    postbox["01 Overseer"]["cachedmessage"] = "";
    postbox["02 Overseer"]["cachedmessage"] = "";
    postbox["scribe"]["cachedmessage"] = "";

    with open('postbox.json', 'w') as json_file:
        json.dump(postbox,json_file, indent=3)

    open('output/user_documentation.txt', 'w').close()

    open('conversation.txt', 'w').close()
    open('00_input.txt', 'w').close()
    open('01_input.txt', 'w').close()
    open('02_input.txt', 'w').close()
    open('scribe_input.txt', 'w').close()
    open('01 Overseer_input.txt', 'w').close()
    open('02 Overseer_input.txt', 'w').close()

    open('01_output.txt', 'w').close()
    open('02_output.txt', 'w').close()
    open('00_output.txt', 'w').close()
    open('scribe_output.txt', 'w').close()
    open('01 Overseer_output.txt', 'w').close()
    open('02 Overseer_output.txt', 'w').close()


    
    # List of files and directories to keep
    keep_list = ['__pycache__', 'cachedrequests', 'misc', 'clear.py', 'sequencer.py', 'features.txt', 'messenger.py', 'postbox.json', 'user_documentation.txt']

    # Get the current directory
    print(os.path)
    # Get the list of files and directories in the current directory
    files = os.listdir('output')

    for file in files:
        if(file != 'user_documentation.txt'):
            file_path = os.path.join('output', file)
            os.remove(file_path)

clear()