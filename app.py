import configparser

from repository.read import Inventory
from resources.welcome import Root
from repository.add_item import Insert

from flask_restful import Api
from repository.uri import db_uri
import os
from flask_pymongo import PyMongo



from flask import Flask
app = Flask(__name__)
api = Api(app)


api.add_resource(Root, "/")
api.add_resource(Inventory, "/inventory")
api.add_resource(Insert, "/add-item")

mongodb_client = PyMongo(app, db_uri)
db = mongodb_client.db

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == '__main__':
    app.run(debug=True)
    app.config["DEBUG"] = True
    app.config["MONGO_URI"] = db_uri

    app.run()