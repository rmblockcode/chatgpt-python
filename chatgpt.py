import os
import openai

openai.api_key = os.environ.get('API_KEY')

# while True:

#     prompt = input('\n Escribe un texto: ')

#     if prompt == 'salir':
#         break

#     completion = openai.Completion.create(
#         model="text-davinci-003", 
#         prompt=prompt,
#         max_tokens=2048)
    
#     print(completion.choices[0].text)

def chatgpt_request(prompt: str):
    completion = openai.Completion.create(
        model="text-davinci-003", 
        prompt=prompt,
        max_tokens=2048)
    
    return completion.choices[0].text