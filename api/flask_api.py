"""
Brevets RESTful API
"""
import os
from flask import Flask
from flask_restful import Api
from mongoengine import connect

import logging

# TODO: finish resources.brevet before i do this part
# from resources.brevet import Brevet
from resources.brevets import Brevets

# Connect MongoEngine to mongodb
connect(host=f"mongodb://{os.environ['MONGODB_HOSTNAME']}:27017/brevetsdb")

# Start Flask app and Api here:
app = Flask(__name__)
api = Api(app)

# Bind resources to paths here:
# api.add_resource(Brevet)                  # TODO: get urls from flask_brevets.py
# api.add_resource(Brevets, "/api/______")  # TODO: get urls from flask_brevets.py

if __name__ == "__main__":
    # Run flask app normally
    # Read DEBUG and PORT from environment variables.

    # print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=os.environ["PORT"], host="0.0.0.0")
