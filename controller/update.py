import json
import sys
sys.path.append(".")
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request, Response


from uri import db_uri

from flask_restful import Resource

class Update(Resource):
    def get(self, id, name, sell_in, quality):
        id = json.loads(request.data.decode("UTF-8"))
        name = request.json["name"]
        sell_in = request.json["sell_in"]
        quality = request.json["quality"]
        if name and sell_in and quality and id:
            mongo.db.stock.update_one(
                {"_id": ObjectId(id["_id"]) if "$oid" in id else ObjectId(id)}, {
                    "$set": {"name": name,
                    "sell_in": sell_in,
                    "quality": quality}
                })
            response_update = jsonify({"message": "Item" + id["_id"] + "has been updated!"})
            response_update.status_code = 200
            return response_update
        else:
            return  not_found()