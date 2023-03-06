"""
Resource: Brevets

MongoEngine queries:
Brevet.objects() : similar to find_all. Returns a MongoEngine query
Brevet(...).save() : creates new brevet
Brevet.objects.get(id=...) : similar to find_one

Two options when returning responses:

return Response(json_object, mimetype="application/json", status=200)
return python_dict, 200

Why would you need both?
Flask-RESTful's default behavior:
Return python dictionary and status code,
it will serialize the dictionary as a JSON.

MongoEngine's objects() has a .to_json() but not a .to_dict(),
So when you're returning a brevet / brevets, you need to convert
it from a MongoEngine query object to a JSON and send back the JSON
directly instead of letting Flask-RESTful attempt to convert it to a
JSON for you.
"""

from flask import Response, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet


# TODO:
class Brevets(Resource):    # class 'Brevets' inherits from class 'Resource'

    # he did an example of these with a dict instead of database stuff 
    # in morning lab if i want to see them in more depth!

    # return all brevets
    def get(self):
        output_json = Brevet.objects().to_json()
        return Response(output_json, mimetype="application/json", status=200)


    def post(self):
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.json

        # Because input_json is a dictionary, we can do this:
        length = input_json["length"]           # Should be a string
        start_time = input_json["start_time"]   # Should be a datetime object (could possibly do string?)
        checkpoints = input_json["checkpoints"] # Should be a list of dictionaries

        # create the new brevet!
        result = Brevet(length=length, start_time=start_time, checkpoints=checkpoints).save()

        # dont technically need to return anything, but its standard practice
        # to return the id of the object we just created
        return {'_id': str(result.id)}, 200



    # def ...
