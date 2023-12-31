import os

secret_key = "secret_key"

def get_data():
    os.environ['API_KEY'] = 'sk-apikey'
    os.environ['chat_gpt_model'] = "gpt-3.5-turbo"