from flask_restful import Resource, Api

inventory = [ {"name": "Aged_brie", "quality": 3, "sell_in": 4 },   
{"name": "Sulfuras", "quality": 80, "sell_in": 0 }, 
{"name": "Aged_brie", "quality": 12, "sell_in": 0 }, 
{"name": "Conjured", "quality": 6, "sell_in": 10 } ]

class Inventario(Resource):

    def get(self):
        return inventory

    def post(self):
        pass