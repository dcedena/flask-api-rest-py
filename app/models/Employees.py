from flask import request, jsonify
from flask_restful import Resource
from db import db

class Employees(Resource):
    def __init__(self):
        self.db1 = db()
        self.conn = self.db1.get_connect().connect()

    def get(self):
        query = self.conn.execute("SELECT * FROM employees")  # Esta línea ejecuta un query y retorna un json como resultado
        # return {'employees': [i for i in query.cursor.fetchall()]}  # Se obtiene la primera columna que es EmployeeId
        result = {'employees': [dict(zip(tuple (query.keys()), i)) for i in query.cursor.fetchall()]}
        return jsonify(result)

    def post(self):
        last_name = request.json['LastName']
        first_name = request.json['FirstName']
        title = request.json['Title']
        reports_to = request.json['ReportsTo']
        birth_date = request.json['BirthDate']
        hire_date = request.json['HireDate']
        address = request.json['Address']
        city = request.json['City']
        state = request.json['State']
        country = request.json['Country']
        postal_code = request.json['PostalCode']
        phone = request.json['Phone']
        fax = request.json['Fax']
        email = request.json['Email']
        query = self.conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                                  '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                                  '{13}')".format(last_name,first_name,title,
                                                  reports_to, birth_date, hire_date, address,
                                                  city, state, country, postal_code, phone, fax,
                                                  email))
        return {'status': 'Nuevo empleado añadido'}

