from flask import Flask

app = Flask(__name__)


@app.route('/')  # decorator associates index() fxn with root URL of app
def index():
    return 'Hello, Flask!'

