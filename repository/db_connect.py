from importlib.resources import Resource
import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
import pymongo
from uri import db_uri


class Connection():
    def connection():
        global collection, db
    
        try:
            client = pymongo.MongoClient()
            client.server_info()
            db = client.Flask
            collection = db.stock
        except:
            print("El servidor está caído o la URI es incorrecta")
            exit()
        else:
            return True

# connection()