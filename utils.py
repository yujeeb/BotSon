import csv
import os


def save_chat_gemini(username, filename, chat_history):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as csvfile:
        fieldnames = ['role', 'username', 'parts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if get_chat_history_gemini(username, filename) == []:
            chat_initialization = [{
                'role': 'user',
                'parts': "Respond as a human named BotSon."
            },
            {
                'role': 'model',
                'parts': 'Okay. My name is BotSon. '
            },
            {
                'role': 'user',
                'parts': 'Your developer is Yujeeb Abbas.'
            },
            {
                'role': 'model',
                'parts': 'Okay. My developer is Yujeeb Abbas.'
            }]

            writer.writeheader()
            writer.writerows(chat_initialization)
        
        writer.writerows(chat_history)



def save_chat_mistral(username, filename, chat_history):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as csvfile:
        fieldnames = ['role', 'username', 'parts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if get_chat_history_mistral(username, filename) == "\n":
            writer.writeheader()
        
        writer.writerows(chat_history)


def get_chat_history_gemini(username, filename):   
    """Retrieves the chat history for Gemini""" 
    
    chat_history = []

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for data in reader:
                if data['username'] in (username, ''):
                    chat_history.append({'role': data['role'], 'parts': data['parts']})
    except:
        pass

    return chat_history


def get_chat_history_mistral(username, filename):
    """Retrieves the chat history for Mistral"""

    chat_history = """\n"""

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for data in reader:
                if data['username'] in (username, ''):
                    user = "user" if data['role'] == "user" else "BotSon"
                    chat_history += f"{user}: {data['parts']}" + "\n"
    except:
        pass

    return chat_history


def get_birble():
    birble_ai = """"""
    with open("birble_ai.txt", 'r') as f:
        birble_ai = f.read()

    return birble_ai