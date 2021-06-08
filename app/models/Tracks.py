from flask import request, jsonify
from flask_restful import Resource
from db import db

class Tracks(Resource):
    def __init__(self):
        self.db1 = db()
        self.conn = self.db1.get_connect().connect()

    def get(self):
        query = self.conn.execute("SELECT * FROM tracks;")
        result = {'tracks': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
