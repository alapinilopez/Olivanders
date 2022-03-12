import configparser
# from resources.items import Inventario
# from repository.read import Inventario, Inventory
from resources.welcome import Root
from flask_restful import Resource, Api
from repository.uri import db_uri
import os
from flask_pymongo import PyMongo



from flask import Flask
app = Flask(__name__)
api = Api(app)


api.add_resource(Root, "/")
# api.add_resource(Inventory, "/inventory")

mongodb_client = PyMongo(app, "mongodb+srv://lapini:I5UuQdlUknxgTxQ7@cluster0.uyd5x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == '__main__':
    app.run(debug=True)
    app.config["DEBUG"] = True
    app.config["MONGO_URI"] = "mongodb+srv://lapini:I5UuQdlUknxgTxQ7@cluster0.uyd5x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    app.run()