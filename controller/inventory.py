from flask_restful import Resource

class Inventory(Resource):
    def get(self):
        items = mongo.db.stock.find()
        response_items = json_util.dumps(items)
        return Response(response_items, mimetype="application/json")