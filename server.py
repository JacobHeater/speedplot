import sys

sys.path.append('./')

from flask import Flask
from controllers import speedtest, main

app = Flask(__name__)


app.register_blueprint(speedtest.mod)
app.register_blueprint(main.mod)