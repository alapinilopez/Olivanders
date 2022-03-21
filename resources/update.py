from app import *
from errorhandler import not_found

def get_update(_id):
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