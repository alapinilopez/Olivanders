from flask import current_app, g
import flask
from flask_pymongo import PyMongo
from app import db

from app import *
from flask_restful import Resource, Api

class Inventory(Resource):
    def get_all_items():
        find_all = db.Flask.find()
        return flask.jsonify([item for item in find_all])
