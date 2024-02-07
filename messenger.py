from openai import OpenAI
import json
import subprocess
client = OpenAI()

def request(id, usercontent, send):

    postbox_path = 'postbox.json'
    with open(postbox_path, 'r') as json_file:
        postbox = json.load(json_file)

    systemcontent = postbox[id]["systemcontent"]
    if(send == 1):
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": f"{systemcontent}"},
            {"role": "user", "content": f"{usercontent}"}
          ]
          
        )
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
        
        return postbox[id]["cachedmessage"]
    else:
        return postbox[id]["cachedmessage"]
