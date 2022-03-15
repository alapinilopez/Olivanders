from flask import g
from flask_pymongo import PyMongo

from flask_restful import Resource

class Insert(Resource):
    def add_one():
        g.db.stock.insert_one({'name': "item name", 'sell_in': int, 'quality': int})
        return g.flask.jsonify(message = "success")
