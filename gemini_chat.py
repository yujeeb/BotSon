import google.generativeai as genai
from utils import save_private_chat, get_chat_history
import os
from constants import GEMINI_API_KEY


class GeminiChat():
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        PROMPT = "Respond as a human named BotSon."
        self.messages = [{
            'role': 'user',
            'parts': PROMPT
        },
        {
            'role': 'model',
            'parts': 'Okay. My name is BotSon.'
        },
        {
            'role': 'user',
            'parts': 'Your developer is Yujeeb Abbas.'
        },
        {
            'role': 'model',
            'parts': 'Okay. My developer is Yujeeb Abbas.'
        }]


    def message(self, username, chat_name, message_type, input_text: str) -> str:
        filename = "chats/"  + str(message_type) + "/" + str(chat_name) + ".csv"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.messages += get_chat_history(username, filename)
        user_message = {'role': 'user',
                        'parts': input_text.replace("\n", " ")}
        
        self.messages.append(user_message)
        print("added user message")
        
        response = self.model.generate_content(self.messages)

        self.messages[-1]['username'] = username
        
        model_response = {'role': 'model',
                          'username': username,
                          'parts': response.text.replace("\n", " ")}
        
        self.messages.append(model_response)
        print("added model response")

        print(self.messages)

        save_private_chat(filename, self.messages)        

        return response.text