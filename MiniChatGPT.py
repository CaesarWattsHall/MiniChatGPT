# This program uses the openai library to interact with the GPT-3 API. 
# You’ll need to have an OpenAI API key and have it set up with the openai_secret_manager to use this program. 
# You can then run the program and type in your prompts to chat with the chatbot. \
# Type “quit” to exit the program.
#
# By: Caesar R. Watts-Hall
# Date: June 05, 2023

import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

import openai
openai.api_key = secrets["api_key"]

def chat(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text'].strip()

while True:
    prompt = input("User: ")
    if prompt.lower() == "quit":
        break
    response = chat(prompt)
    print(f"Chatbot: {response}")
