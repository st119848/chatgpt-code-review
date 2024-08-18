import openai
openai.api_type = "azure"
openai.api_key = "ollama"
openai.api_base = "http://localhost:11434/v1"
# openai.api_version = "2023-05-15"
# create a chat completion
chat_completion = openai.ChatCompletion.create(engine="llama3.1:8b", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)