from openai import OpenAI
import json
import subprocess
client = OpenAI()

def request(id, systemcontent, usercontent, send):

    postbox_path = 'postbox.json'
    with open(postbox_path, 'r') as json_file:
            postbox = json.load(json_file)

    if(send == 1):
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": f"{systemcontent}"},
            {"role": "user", "content": f"{usercontent}"}
          ]
        )
        if(id == "01"):
            print(completion)
        postbox[id]["cachedmessage"] = completion.choices[0].message.content

        with open(postbox_path, 'w') as json_file:
            json.dump(postbox, json_file, indent=3)
        
        return postbox[id]["cachedmessage"]
    else:
        return postbox[id]["cachedmessage"]
