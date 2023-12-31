import os
import openai
from .environments import enviroments as env

env.get_data()

gpt_api_key = os.environ.get("API_KEY")
chat_gpt_model = os.environ.get("chat_gpt_model")
chatgpt_system = "You are a helpful assistant on a conversation. Answer should be not too long. Be ironic and acid"

openai.api_key = gpt_api_key

# Function to get GPT-4 response
def get_gpt4_response(prompt):
    if not gpt_api_key:
        return "API usage exceded"
    response = openai.chat.completions.create(
        model=chat_gpt_model,
        messages=[
            {"role": "system", "content": chatgpt_system},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content