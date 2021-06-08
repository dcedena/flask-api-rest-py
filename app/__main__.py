from flask import Flask#, request, jsonify
from flask_restful import Api
from models.Employees import Employees
from models.EmployeeData import EmployeeData
from models.Tracks import Tracks
from models.TrackData import TrackData
from models.Home import Home

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Employees, '/employees')
api.add_resource(Tracks, '/tracks')
api.add_resource(TrackData, '/tracks/<track_id>')
api.add_resource(EmployeeData, '/employees/<employee_id>')

if __name__ == '__main__':
     app.run(port='5000', debug=True)
