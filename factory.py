from ast import Delete, Index
from flask import Flask
from flask_restful import Api

from controller.create import Create
from controller.inventory import Inventory
from controller.update import Update

def create_app():
    app = Flask(__name__)
    api = Api(app, catch_all_404s = True)
    api.add_resource("/", Index)
    api.add_resource("/create", Create)
    api.add_resource("/inventory", Inventory)
    api.add_resource("/update", Update)
    api.add_resource("/delete", Delete)
    return app