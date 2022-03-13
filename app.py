import configparser

from resources.welcome import Root
from flask_restful import Resource, Api
import os

from repository.stock import Inventory


from flask import Flask
app = Flask(__name__)
api = Api(app)


api.add_resource(Root, "/")
api.add_resource(Inventory, "/inventory")


if __name__ == '__main__':
    app.run(debug=True)
    app.config["DEBUG"] = True

    app.run()