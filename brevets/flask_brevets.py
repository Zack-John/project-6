"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import os
import logging
import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations

import requests # the library we use to send requests to API (not to be confused with flask.request!)


# Set up Flask app
app = flask.Flask(__name__)
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)


##################################################
################### API Callers ##################
##################################################

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api"

def get_brevet():
    """
    Obtains the newest document in the "brevets" collection in database
    by calling the RESTful API.
    Returns start_time, brevet_dist, and controls (list of dictionaries) as a tuple.
    """

    brevets = requests.get(f"{API_URL}/brevets").json()
    brevet = brevets[-1]

    return brevet["start_time"], brevet["brevet_dist"], brevet["controls"]


def insert_brevet(start_time, brevet_dist, controls):
    """
    Inserts a new to-do list into the database by calling the API.
    Inputs a start_time, brevet_dist and controls (list of dictionaries)
    """

    _id = requests.post(f"{API_URL}/brevets", json={"start_time": start_time, "brevet_dist": brevet_dist, "controls": controls}).json()
    return _id


##################################################
################## Flask routes ################## 
##################################################

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")

    # get values from webpage
    km = request.args.get('km', 999, type=float)
    brevet_dist = request.args.get('brevet_dist', 999, type=float)
    start_time = request.args.get('start_time', type=str)

    # convert start_time string --> arrow object
    start_time_arrow = arrow.get(start_time, 'YYYY-MM-DD[T]HH:mm')

    open_time = acp_times.open_time(km, brevet_dist, start_time_arrow).format('YYYY-MM-DDTHH:mm')    
    close_time = acp_times.close_time(km, brevet_dist, start_time_arrow).format('YYYY-MM-DDTHH:mm')

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


@app.route("/insert_brevet", methods=["POST"])
def insert():
    """
    /insert_brevet : inserts a brevet into the database.
    Accepts POST requests ONLY!
    JSON interface: gets JSON, responds with JSON
    """
    try:
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.get_json()
        
        # Because input_json is a dictionary, we can do this:
        start_time = input_json["start_time"]   # Should be a string
        brevet_dist = input_json["brevet_dist"] # Should be a string
        controls = input_json["controls"]       # Should be a list of dictionaries

        if (not controls):
            return flask.jsonify(result={},
                        message="Cannot insert empty brevet!", 
                        status=0, 
                        mongo_id='None')

        if (not start_time):
            return flask.jsonify(result={},
                        message="No start time provided!", 
                        status=0, 
                        mongo_id='None')

        else:
            brev_id = insert_brevet(start_time, brevet_dist, controls)
            return flask.jsonify(result={},
                            message="Inserted!", 
                            status=1,
                            mongo_id=brev_id)

    except:
        # The reason for the try and except is to ensure Flask responds with a JSON.
        # If Flask catches your error, it means you didn't catch it yourself,
        # And Flask, by default, returns the error in an HTML.
        # We want /insert to respond with a JSON no matter what!
        return flask.jsonify(result={},
                        message="Oh no! Server error!", 
                        status=0, 
                        mongo_id='None')


@app.route("/fetch_brevet")
def fetch():
    """
    /fetch_brevet : fetches the newest brevet from the database.
    Accepts GET requests ONLY!
    JSON interface: gets JSON, responds with JSON
    """
    try:
        start_time, brevet_dist, controls = get_brevet()
        return flask.jsonify(
                result={"start_time": start_time, "brevet_dist": brevet_dist, "controls": controls}, 
                status=1,
                message="Successfully fetched a brevet!")
    except:
        return flask.jsonify(
                result={}, 
                status=0,
                message="Something went wrong, couldn't fetch any lists!")


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


##################################################
################# Start Flask App ################ 
##################################################

if __name__ == "__main__":
    app.run(port=port_num, host="0.0.0.0")
