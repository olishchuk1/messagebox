import time

from flask import Flask, request, abort
import json

app = Flask(__name__)

db = [
    {
        'text': 'Привет',
        'time': time.time(),
        'name': 'Nick'
    },
    {
        'text': 'Привет, Nick',
        'time': time.time(),
        'name': 'Jane'
    }
]


@app.route("/")
def messagebox_hello():
    return 'Hi, there! \nIt\'s MessageBox'


@app.route("/status")
def status():
    return json.dumps({'status': True, 'name': 'MessageBox', 'time': str(time.time())})


@app.route("/send", methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name == '' or text == '':
        return abort(400)

    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:100]}


if __name__ == '__main__':
    app.run(debug=True)
