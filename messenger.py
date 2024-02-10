from ast import Assign
from openai import OpenAI
import json
import subprocess
client = OpenAI()

def request(id, usercontent, send):

    postbox_path = 'postbox.json'
    with open(postbox_path, 'r') as json_file:
        postbox = json.load(json_file)

    systemcontent = postbox[id]["systemcontent"]
    logmessages = postbox.get("logmessages", [])  # Initialize as an empty list if logmessages not present
    print(logmessages)
    systemmessage = {"role": "system", "content": f"{systemcontent}"}
    endmessage = {"role": "system", "content": f"{usercontent}"}

    message_request = logmessages[:]  # Copy logmessages to avoid modifying original list
    message_request.append(endmessage)
    message_request.append(systemmessage)  # Add systemmessage to request

    if send == 1:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=message_request
        )

        user_message = {"role": "user", "content": completion.choices[0].message.content}
        # Update logmessages without including systemmessage
        postbox["logmessages"] = logmessages + [user_message]
        with open('conversation.txt', 'a',encoding="utf-8") as conversation:
            conversation.write(id +':\n' + completion.choices[0].message.content + '\n')

        with open(f'{id}_output.txt', 'a',encoding="utf-8") as id_conversation:
            id_conversation.write(id +':\n' + completion.choices[0].message.content + '\n')
            id_conversation.close()
        with open(f'{id}_input.txt', 'a',encoding="utf-8") as id_conversation:
            id_conversation.write(id +':\n' + usercontent + '\n')
            id_conversation.close()
        postbox[id]["cachedmessage"] = completion.choices[0].message.content

        with open(postbox_path, 'w',encoding="utf-8") as json_file:
            json.dump(postbox, json_file, indent=3)
        
        return completion.choices[0].message.content
    else:
        return postbox[id]["cachedmessage"]
