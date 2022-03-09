from controller.items import items
from controller.welcome import welcome
from flask_restful import Resource, Api

from flask import Flask
app = Flask(__name__)
api = Api(app)

@app.route("/")
def welcome():
    return welcome

@app.route("/inventory")
def inventory():
    return items()

if __name__ == '__main__':
    app.run(debug=True)