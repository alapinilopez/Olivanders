import json

from bson.objectid import ObjectId
from bson import json_util
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request, Response
from crypt import methods
from resources.delete import delete
from resources.stock import get_stock
from resources.update import get_update
from resources.welcome import get_index
from resources.create import get_create_item

import sys
sys.path.append(".")


app = Flask(__name__)
app.config["MONGO_URI"] = db_uri
mongo = PyMongo(app)


@app.route("/", methods=["GET"])
def index():
    return get_index()


@app.route("/delete/", methods=["DELETE"])
def delete_item():
    return delete()


@app.route("/create",methods=["POST"])
def create():
    return get_create_item()


@app.route("/inventory", methods=["GET"])
def inventory():
    return get_stock()


@app.route("/update", methods=["PUT"])
def update_item():
    return get_update()


if __name__ == "__main__":
    app.run(debug=True)
