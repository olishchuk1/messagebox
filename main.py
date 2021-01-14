from datetime import datetime

db = [
    {
        'text': 'Привет',
        'time': datetime.now(),
        'name': 'Nick'
    },
    {
        'text': 'Привет, Nick',
        'time': datetime.now(),
        'name': 'Jane'
    }
]


def print_message(message):
    print(f'{message["time"]} {message["name"]}\n{message["text"]}')


def print_messages(db):
    for message in db:
        print_message(message)


def send_message(name, text):
    message = {
        'text': text,
        'time': datetime.now(),
        'name': name
    }
    db.append(message)


def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


if __name__ == '__main__':
    send_message('Nick', 'Привет')

    messages = get_messages(datetime.min)
    print_messages(messages)

    send_message('Nick', 'Привет2')

    messages = get_messages(messages[-1]['time'])
    print_messages(messages)

    messages = get_messages(messages[-1]['time'])
    print_messages(messages)
