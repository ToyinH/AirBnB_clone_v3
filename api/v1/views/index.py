#!/usr/bin/python3
"""
index file
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """create a route /status on the object app_views
    that returns a JSON"""
    return jsonify({"status": "OK"})
