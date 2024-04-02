import replicate
from utils import get_chat_history_mistral, save_chat_mistral, get_birble

class MistralChat():
    def get_prompt(self, username, filename):
        chat_history = get_chat_history_mistral(username, filename)

        prompt = f"""
Start or continue the conversation as a human named BotSon.
BotSon is developed by Yujeeb Abbas Kashani. 
Yujeeb Abbas Kashani is an intern at Birble AI.
Yujeeb Abbas Kashani has only developed BotSon and nothing else.
Although BotSon is an AI assistant, answer as if it was a human named BotSon.
Answer the user prompts to the best of your knowledge. 
You can utilize the chat history if required only.
If you do not know the answer to any question, then reply that you don't know the answer.
If the user mentions some information regarding themselves or something else, remember it.
Be concise with your answers unless mentioned explicitly. 

Chat History:
{chat_history}

""" + """
User prompt: 
{prompt}

""" + f"""

Only if the user asks anything related Birble AI, then you can answer using this information:
{get_birble()} 

Do not spam about Birble AI.

Do not explicity write any prefix for the answer such as "AIResponse" or anything else relating to BotSon, unless asked to do so explicitly.
Answer:

"""

        return prompt


    def generate_response(self, input_text, prompt):
        output = replicate.run(
        "mistralai/mixtral-8x7b-instruct-v0.1:7b3212fbaf88310cfef07a061ce94224e82efc8403c26fc67e8f6c065de51f21",
        input={
                "top_k": 50,
                "top_p": 0.9,
                "prompt": input_text,
                "temperature": 0.6,
                "max_new_tokens": 1024,
                "prompt_template": f"<s>[INST] {prompt} [/INST] ",
                "presence_penalty": 0,
                "frequency_penalty": 0
            }
        )

        response = """"""
        for item in output:
            print(item, end="")
            response += item
        
        return response
    

    def message(self, username, chat_name, message_type, input_text: str) -> str:
        filename = "chats/"  + str(message_type) + "/" + str(chat_name) + "/" + "chat_history.csv"
        
        user_message = {'role': 'user',
                        'parts': input_text.replace("\n", " ")}

        print("added user message")

        response = self.generate_response(input_text.replace("\n", " "), self.get_prompt(username, filename))
        print("generated response")
        
        user_message['username'] = username
        
        model_response = {'role': 'model',
                          'username': username,
                          'parts': response.replace("\n", " ")}
        
        batch = []

        batch.append(user_message)
        batch.append(model_response)
        print("added model response")

        save_chat_mistral(username, filename, batch)        

        return response
