
import streamlit as st
import os
st.write("hello world")
from ollama import chat
from ollama import Client
from ollama import generate


client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + st.secrets["OLLAMA_API_KEY"]}
    # headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)




###check:

response = client.chat(
  model='qwen3',
  messages=[{'role': 'user', 'content': 'How many letter r are in strawberry?'}],
  stream=False,
)

# print('Thinking:\n', response.message.thinking)
print('Answer:\n', response.message.content)





# response = chat(
#   model='gpt-oss:120b',
#   messages=[{'role': 'user', 'content': 'Tell me about Canada.'}],
# )
# print(response.message.content)


text = """
Ollama lets users run large language models on local machines.
This approach emphasizes privacy and control, as data does not leave the user's environment.
Developers can leverage various open-source models through a simple interface, improving efficiency and reducing costs.
"""


# prompt = f"Summarize the following text in one sentence:\n\"\"\"\n{text}\n\"\"\""
# result = generate(model='gpt-oss:120', prompt=prompt)
# print("Summary:", result['response'])
# st.print("Summary:", result['response'])



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