from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "index  page"


@app.route("/hello")
def hello():

    return "hello world"
