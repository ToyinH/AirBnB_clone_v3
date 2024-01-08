#!/usr/bin/python3
"""
State endpoint
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route("/cities/<city_id>/places", methods=['GET', 'POST'],
                 strict_slashes=False)
def get_place(city_id):
    """Get place with city id"""
    if request.method == 'GET':
        city = storage.get(City, city_id)
        if city:
            places = storage.all(Place)
            p_with_id = [place for place in places.values()
                         if place.city_id == city_id]
            return jsonify(list(map(lambda x: x.to_dict(), p_with_id)))
        else:
            abort(404)
    elif request.method == 'POST':
        post = request.get_json()
        if post:
            city = storage.get(City, city_id)
            if city:
                if "user_id" not in post:
                    return "Missing user_id", 400
                if not storage.get(User, post.get("user_id")):
                    abort(404)
                if "name" not in post:
                    return "Missing name", 400
                post["city_id"] = city_id
                new_place = Place(**post)
                new_place.save()
                return new_place.to_dict(), 201
            else:
                abort(404)
        else:
            return "Not a JSON", 400


@app_views.route("/places/<place_id>", methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def places(place_id):
    """Places"""
    if request.method == 'GET':
        places_all = storage.all(Place)
        places_list = []
        place = storage.get(Place, place_id)
        return jsonify(place.to_dict()) if place else (abort(404))
    elif request.method == 'DELETE':
        place = storage.get(Place, place_id)
        if place:
            storage.delete(place)
            storage.save()
            return jsonify({})
        else:
            abort(404)
    elif request.method == 'PUT':
        place = storage.get(Place, place_id)
        if place:
            put = request.get_json()
            if put:
                for k, v in put.items():
                    if k not in ["id", "created_at", "updated_at"]:
                        setattr(place, k, v)
                    place.save()
                    return place.to_dict()
            else:
                return "Not a JSON", 400
        else:
            abort(404)
