#!/usr/bin/python3
"""
State endpoint
"""
from . import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State


@app_views.route("/states", methods=['GET', 'POST'], strict_slashes=False)
@app_views.route("/states/<state_id>", methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def states(state_id=None):
    """Retrive states"""
    states_all = storage.all(State)
    if request.method == 'GET':
        states_list = []
        if state_id:
            state = next((state for state in states_all.values()
                          if state.id == state_id), None)
            return jsonify(state.to_dict()) if state else (abort(404))
        else:
            for v in states_all.values():
                states_list.append(v.to_dict())
            return jsonify(states_list)
    elif request.method == 'DELETE':
        state = next((state for state in states_all.values()
                      if state.id == state_id), None)
        if state:
            storage.delete(state)
            storage.save()
            return jsonify({})
        else:
            abort(404)
    elif request.method == 'POST':
        post = request.get_json()
        if post:
            name = post.get("name")
            if name:
                new_state = State(**post)
                new_state.save()
                return new_state.to_dict(), 201
            else:
                return "Missing name", 404
        else:
            return "Not a JSON", 404
    elif request.method == 'PUT':
        state = next((state for state in states_all.values()
                      if state.id == state_id), None)
        if state:
            put = request.get_json()
            if put:
                for k, v in put.items():
                    if k not in ["id", "created_at", "updated_at"]:
                        setattr(state, k, v)
                        state.save()
                        return state.to_dict()
            else:
                return "Not a JSON", 404
        else:
            abort(404)
