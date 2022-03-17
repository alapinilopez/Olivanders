from flask_restful import Resource

class Delete(Resource):
    def get(self):
        id = json.loads(request.data.decode("UTF-8"))
        mongo.db.stock.delete_one({"_id": ObjectId(id["_id"])})
        response_delete = jsonify({"message": "item" + id["_id"] + "deleted!"})
        return response_delete