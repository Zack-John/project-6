# UOCIS322 - Project 6 #
Brevet time calculator with MongoDB, and a RESTful API!

Read about MongoEngine and Flask-RESTful here: [http://docs.mongoengine.org/](http://docs.mongoengine.org/), [https://flask-restful.readthedocs.io/en/latest/](https://flask-restful.readthedocs.io/en/latest/).

## Before you begin
Add a `.env` file to the main directory and specify your container API_PORT and BREVETS_PORT numbers there!
(Note that the default values, 5000 and 5000, will work!)

## Overview

This app is a RUSA ACP controle time calculator, built with Flask + AJAX, MongoDB and a RESTful API to communicate between the app and database!
> That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

### ACP controle times algorithm

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders).

I have essentially replaced the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).

## How to Use

### Building and Serving

Build / serve the docker image / container by running `docker compose up --build -d` from the main directory (where `docker-compose.yml` is located).

### Using the App

Once the containers are running, you can access the app via a web browser by navigating to `localhost:5002` (by default).

You can then set the brevet length and start date/time with the input boxes at the top of the page.

Once the brevet length and start are specified, simply fill in the desired distances for each checkpoint in either miles or km. The webpage will automatically populate checkpoint open and close times.

To store your brevet info in the database, click the `Submit` button. To retrive the info you've stored, click the `Display` button. 

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani. Updated again by Zack Johnson :)
