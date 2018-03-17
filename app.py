"""
Api endpoint: /api/{body_part}/{location}

location => default=warszawa
body_part => head, limb, chest, back
"""
from flask import Flask, make_response
from flask_restful import Resource, Api
from znany_data_source import get_medical_institutions
from functools import wraps
from symptoms_map import MAPPER

app = Flask(__name__)
api = Api(app)

default_location = 'warszawa'

class Data(Resource):
    def get(self, body_part, location=None):
        location = location or default_location
        institutions = []
        for speciality in MAPPER[body_part]:
            institutions.extend(get_medical_institutions(speciality, location))
        return institutions, {'Access-Control-Allow-Origin': '*'}


api.add_resource(Data, '/api/<string:body_part>/<string:location>')

if __name__ == '__main__':
    app.run(debug=True)
