from resources.items import Inventario
from resources.welcome import Root
from flask_restful import Resource, Api

from flask import Flask
app = Flask(__name__)
api = Api(app)


api.add_resource(Root, "/")

api.add_resource(Inventario, "/inventory")

if __name__ == '__main__':
    app.run(debug=True)