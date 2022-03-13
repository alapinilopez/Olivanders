from audioop import add
from email import parser
import string
from flask_restful import marshal_with, reqparse, Resource, Api, fields, g
import json

parser = reqparse.RequestParser()
def add_one():
    parser.add_argument("name", type = string)
    parser.add_argument("sell in", type = int)
    parser.add_argument("quality", type = int)


class Create(Resource):

    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }
    
    @marshal_with(resource_fields)
    def get(self):
        return (add_one)
    


