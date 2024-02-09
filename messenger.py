from openai import OpenAI
import json
import subprocess
client = OpenAI()

def request(id, usercontent, send):

    postbox_path = 'postbox.json'
    with open(postbox_path, 'r') as json_file:
        postbox = json.load(json_file)

    systemcontent = postbox[id]["systemcontent"]
    logmessages = postbox["logmessages"]
    firstmessage = {"role": "system", "content": f"{systemcontent}"}
    endmessage = {"role": "system", "content": f"{usercontent}"}
    pastmessages = [firstmessage]
    if logmessages != []:
        pastmessages.extend(logmessages)  # Extend instead of append

    pastmessages.append(endmessage)
    if(send == 1):
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=pastmessages
        )

        user_message = {"role": "user", "content": completion.choices[0].message.content}
        postbox["logmessages"] = logmessages + [user_message]  # Create a new list with the user message appended
        with open('conversation.txt', 'a') as conversation:
            conversation.write(id +': ' + completion.choices[0].message.content + '\n')

        with open(f'{id}_output.txt', 'a') as id_conversation:
            id_conversation.write(id +': ' + completion.choices[0].message.content + '\n')
            id_conversation.close()
        with open(f'{id}_input.txt', 'a') as id_conversation:
            id_conversation.write(id +': ' + usercontent + '\n')
            id_conversation.close()
        postbox[id]["cachedmessage"] = completion.choices[0].message.content

        with open(postbox_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)
        
        return completion.choices[0].message.content
    else:
        return postbox[id]["cachedmessage"]
