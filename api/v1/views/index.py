#!/usr/bin/python3
"""
index file
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """create a route /status on the object app_views
    that returns a JSON"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    retrieves the number of each objects by type
    """
    stats_dict = {}

    # Define the object types you want to count
    object_types = ['User', 'Place', 'City', 'State', 'Amenity', 'Review']

    # Retrieve the count for each object type
    for obj_type in object_types:
        count = storage.count(obj_type)
        stats_dict[obj_type] = count

    return jsonify(stats_dict)
