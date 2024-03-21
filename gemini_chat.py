import google.generativeai as genai
from utils import save_chat, get_chat_history
import os
from constants import GEMINI_API_KEY


class GeminiChat():
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')


    def message(self, username, chat_name, message_type, input_text: str) -> str:
        filename = "chats/"  + str(message_type) + "/" + str(chat_name) + ".csv"
        
        chat_history = get_chat_history(username, filename)
        
        user_message = {'role': 'user',
                        'parts': input_text.replace("\n", " ")}
        
        chat_history.append(user_message)
        print("added user message")

        response = self.model.generate_content(chat_history)
        print("generated response")
        
        user_message['username'] = username
        
        model_response = {'role': 'model',
                          'username': username,
                          'parts': response.text.replace("\n", " ")}
        
        batch = []

        batch.append(user_message)
        batch.append(model_response)
        print("added model response")

        # print(chat_history)

        save_chat(username, filename, batch)        

        return response.text