import flask
import pymongo
import mongoengine


from flask_restful import Resource

class Inventory(Resource):
    def get_all_items():
        find_all = db.Flask.find()
        return Flask.jsonify([item for item in find_all])
