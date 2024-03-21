import csv
import os


def save_chat(username, filename, chat_history):
    with open(filename, 'a') as csvfile:
        fieldnames = ['role', 'username', 'parts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if get_chat_history(username, filename) == []:
            chat_initialization = [{
                'role': 'user',
                'parts': "Respond as a human named BotSon."
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

            writer.writeheader()
            writer.writerows(chat_initialization)
        
        writer.writerows(chat_history)


def get_chat_history(username, filename):    
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