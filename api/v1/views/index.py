#!/usr/bin/python3
"""Set up and create initial files"""
from flask import jsonify, make_response
from api.v1.views import app_views
from models import storage

classes = {"Amenity": "amenities",
           "City": "cities",
           "Place": "places",
           "Review": "reviews",
           "State": "states",
           "User": "users"}


@app_views.route('/status', strict_slashes=False)
def view_status():
    """Return a JSON object"""
    response = jsonify({"status": "OK"})
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route('/stats', strict_slashes=False)
def storage_stats():
    """Provide a JSON response"""
    dict = {}
    for cls, name in classes.items():
        dict.update({name: storage.count(cls)})
    response = jsonify(dict)
    response.headers["Content-Type"] = "application/json"
    return response
