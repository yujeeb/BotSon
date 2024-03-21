import csv


def save_private_chat(filename, chat_history):
    with open(filename, 'w') as csvfile:
        fieldnames = ['role', 'username', 'parts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

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