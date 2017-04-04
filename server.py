from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell_world():
    return 'Hello, world!'

@app.route('/speedtest')
def speed_test():
    return 'TODO: speed test here...'