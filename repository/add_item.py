from email.mime import message
from flask import current_app, g
import flask
from flask_pymongo import PyMongo
from app import db

from app import *
from flask_restful import Resource, Api

class Insert(Resource):
    def add_one():
        db.stock.insert_one({'name': "item name", 'sell_in': int, 'quality': int})
        return flask.jsonify(message = "success")
