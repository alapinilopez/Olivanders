
from services.db import items

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Olivanders!</h1>"

@app.route("/inventory")
def inventory():
    return items()