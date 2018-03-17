from flask import Flask
from flask_restful import Resource, Api
from znany_data_source import get_medical_institutions


app = Flask(__name__)
api = Api(app)


class Data(Resource):
    def get(self, doctor_speciality, location):
        return get_medical_institutions(doctor_speciality, location)


api.add_resource(Data, '/api/<string:doctor_speciality>/<string:location>')

if __name__ == '__main__':
    app.run(debug=True)
