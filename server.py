import sys

sys.path.append('./')

from flask import Flask
from controllers import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

app.register_blueprint(speedtest.mod)