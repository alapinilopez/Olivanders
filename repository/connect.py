from http import client
import pymongo
from uri import db_uri

uri = db_uri

def connection():
    global collection, db
    try:
        client = pymongo.MongoClient(db_uri)
        client.server_info()
        db = client.olivanders
        collection = db.stock
    except:
        exit()
    else:
        return True

connection()