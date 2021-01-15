import requests

name = input('Enter your name: ')

while True:
    text = input('Enter your message: ')
    requests.post(
        'http://127.0.0.1:5000/send',
        json={'name': name, 'text': text}
    )
