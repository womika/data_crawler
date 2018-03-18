"""
Api endpoint: /api/{body_part}/{location}

location => default=warszawa
body_part => head, limb, chest, back
"""
import asyncio
from functools import wraps

from flask import Flask, make_response
from flask_restful import Api, Resource

from symptoms_map import MAPPER
from znany_data_source import get_medical_institutions


async def get_instituion(speciality, location):
    return get_medical_institutions(speciality, location)


app = Flask(__name__)
api = Api(app)

default_location = 'warszawa'


class Data(Resource):
    def get(self, body_part, location=None):
        location = location or default_location
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        institutions = loop.run_until_complete(
            asyncio.gather(
                *list(
                    get_instituion(*args)
                    for args in zip(MAPPER[body_part], (location for _ in MAPPER[body_part]))
                )
            )
        )
        loop.close()
        return institutions, {'Access-Control-Allow-Origin': '*'}


api.add_resource(Data, '/api/<string:body_part>/<string:location>')

if __name__ == '__main__':
    app.run(debug=True)
