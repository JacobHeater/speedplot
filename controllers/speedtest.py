from flask import Blueprint, render_template

mod = Blueprint('speedtest', __name__, url_prefix='/speedtest')

@mod.route('/')
def index():
    return render_template('speedtest/speedtest.html')