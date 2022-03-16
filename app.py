import json
from repository.connect import *
from bson.objectid import ObjectId
from bson import json_util
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request, Response
from crypt import methods
import sys
sys.path.append(".")


app = Flask(__name__)
app.config["MONGO_URI"] = db_uri
mongo = PyMongo(app)


@app.route("/")
def index():
    return "Welcome to Olivanders!"


@app.route("/delete/", methods=["DELETE"])
def delete_item():
    id = json.loads(request.data.decode("UTF-8"))
    mongo.db.stock.delete_one({"_id": ObjectId(id["_id"])})
    response_delete = jsonify({"message": "item" + id["_id"] + "deleted!"})
    return response_delete


@app.route("/create", methods=["POST"])
def create_item():
    name = request.json["name"]
    sell_in = request.json["sell_in"]
    quality = request.json["quality"]

    if name and sell_in and quality:
        id = mongo.db.stock.insert(
            {"name": name, "sell_in": sell_in, "quality": quality}
        )
        response_insert = jsonify({
            "id": str(id),
            "name": name,
            "sell_in": sell_in,
            "quality": quality
        })
        response_insert.status_code = 201
        return response_insert
    else:
        return not_found


@app.route("/inventory", methods=["GET"])
def get_items():
    items = mongo.db.stock.find()
    response_items = json_util.dumps(items)
    return Response(response_items, mimetype="application/json")


@app.route("/update", methods=["PUT"])
def update_item(_id):
    name = request.json["name"]
    sell_in = request.json["sell_in"]
    quality = request.json["quality"]
    if name and sell_in and quality and _id:
        mongo.db.stock.update_one(
            {"_id": ObjectId(_id["$oid"]) if "$oid" in _id else ObjectId(_id)}, {
                "$set": {"name": name,
                "sell_in": sell_in,
                "quality": quality}
            })
        response_update = jsonify({"message": "Item" + _id + "has been updated!"})
        response_update.status_code = 200
        return response_update
    else:
        return  not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response_error = jsonify(message)
    response_error.status_code = 404
    return response_error


if __name__ == "__main__":
    app.run(debug=True)
