
from flask import jsonify
from flask_restful import Resource

class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        result = { 
            ' Info ': 'Commands List',
            'GET Employees': '/employees',
            'GET Employee 1': '/employees/1',
            'GET Tracks': '/tracks',
            'GET Track 1': '/tracks/1'
         }
        return jsonify(result)
