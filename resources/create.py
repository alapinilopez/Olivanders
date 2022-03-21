from app import *
from errorhandler import not_found


def get_create_item():
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