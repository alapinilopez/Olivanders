def get_stock():
    items = mongo.db.stock.find()
    response_items = json_util.dumps(items)
    return Response(response_items, mimetype="application/json")