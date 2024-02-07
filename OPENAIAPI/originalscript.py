from openai import OpenAI
import subprocess
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Your objective is to write a script from the ground up according to whatever request is given. In these scripts, you can read, write, and execute whatever files you like. Your raw output will be executed as a script, so only output the generated script and no more."},
    {"role": "user", "content": "Write a simple python script that generates a .txt file with the word \"Hello\" written in it."}
  ]
)

#print(completion)
response_content = completion.choices[0].message.content
print(response_content)

# Specify the file path (change as needed)
file_path = "helloscript.py"

# Write the content to the .py file
with open(file_path, "w") as file:
    file.write(response_content)

# Execute the script
subprocess.run(["python", file_path])
print(f"File '{file_path}' created successfully.")