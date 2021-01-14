from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/")
def messagebox_hello():
    return 'Hi, there! \nIt\'s MessageBox'


@app.route("/status")
def status():
    return json.dumps({'status': True, 'name': 'MessageBox', 'time': str(datetime.now())})


if __name__ == '__main__':
    app.run(debug=True)
