#!/usr/bin/python3
"""Prepare Flask functions."""
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
    """Provides a JSON response."""
    response = jsonify({"status": "OK"})
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route('/stats', strict_slashes=False)
def storage_stats():
    """Provides a JSON response."""
    dict = {}
    for cls, name in classes.items():
        dict.update({name: storage.count(cls)})
    response = jsonify(dict)
    response.headers["Content-Type"] = "application/json"
    return response
