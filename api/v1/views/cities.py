#!/usr/bin/python3
"""
Cities API actions
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.cities import City


@app_views.route("/states/<state_id>/cities", methods=['GET', 'POST'], strict_slashes=False)
@app_views.route("/cities/<city_id>", methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def cities(city_id=None):
    """Retrive cities"""
    cities_all = storage.all(City)
    if request.method == 'GET':
        cities_list = []
        if city_id:
            city = storage.get(City, city_id)
            return jsonify(city.to_dict()) if city else (abort(404))
        else:
            for value in states_all.values():
                cities_list.append(value.to_dict())
            return jsonify(cities_list)
    elif request.method == 'DELETE':
        city = storage.get(City, city_id)
        if city:
            storage.delete(city)
            storage.save()
            return jsonify({})
        else:
            abort(404)
    elif request.method == 'POST':
        post = request.get_json()
        if post:
            if "name" in post:
                new_city = City(**post)
                new_city.save()
                return new_city.to_dict(), 201
            else:
                return "Missing name", 400
        else:
            return "Not a JSON", 400
    elif request.method == 'PUT':
        city = storage.get(City, city_id)
        if city:
            put = request.get_json()
            if put:
                for key, value in put.items():
                    if key not in ["id", "created_at", "updated_at"]:
                        setattr(state, key, value)
                    city.save()
                    return city.to_dict()
            else:
                return "Not a JSON", 400
        else:
            abort(404)
