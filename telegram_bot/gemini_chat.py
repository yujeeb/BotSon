import google.generativeai as genai


class GeminiChat():
    def __init__(self):
        self.chat_history = []
        genai.configure(api_key="AIzaSyDdgYXrJe6ZMqpQz3SVwz1JqzcH1xZd8MA")
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=self.chat_history)


    def message(self, input_text: str) -> str:
        response = self.chat.send_message(input_text)
        # print(response.text)
        return response.text


    def get_chat_history(self):
        print(self.chat.history)


# g = GeminiChat()
# print(g.message("What is solar system?"))
# print(g.message("What is NASA?"))
# g.get_chat_history()