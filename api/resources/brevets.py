"""
Resource: Brevets
"""

from flask import Response, request
from flask_restful import Resource

from database.models import Brevet

# "your JSON inputs have to have the EXACT SAME field names!"
class BrevetsResource(Resource):

    # return all brevets
    def get(self):
        output_json = Brevet.objects().to_json()
        return Response(output_json, mimetype="application/json", status=200)

    # save brevets
    def post(self):
        input_json = request.json
        result = Brevet(**input_json).save()
        return {'_id': str(result.id)}, 200
