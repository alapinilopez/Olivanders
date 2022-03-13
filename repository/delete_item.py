from flask import current_app, g
import flask
from flask_pymongo import PyMongo
from app import db

from app import *
from flask_restful import Resource, Api

class Delete(Resource):
    def delete_item():
        delete = db.stock.delete_many({'name': "item name"})
        return delete.raw_result
