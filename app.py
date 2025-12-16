
import streamlit as st
import os
st.write("hello world")
from ollama import chat
from ollama import Client


client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + st.secrets["OLLAMA_API_KEY"]}
    # headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)

# messages = [
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
#  ]
# for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
#   print(part['message']['content'], end='', flush=True)

response = chat(
  model='gpt-oss:120b',
  messages=[{'role': 'user', 'content': 'Tell me about Canada.'}],
)
print(response.message.content)



# responses_result = client.responses.create(
#   model='qwen3:8b',
#   input='Write a short poem about the color blue',
# )
# print(responses_result.output_text)





# from ollama import chat
# from pydantic import BaseModel

# class Country(BaseModel):
#   name: str
#   capital: str
#   languages: list[str]

# response = chat(
#   model='gpt-oss',
#   messages=[{'role': 'user', 'content': 'Tell me about Canada.'}],
#   format=Country.model_json_schema(),
# )

# country = Country.model_validate_json(response.message.content)
# print(country)