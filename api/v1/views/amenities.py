#!/usr/bin/python3
"""
Amenity endpoint
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=['GET', 'POST'], strict_slashes=False)
@app_views.route("/amenities/<amenity_id>", methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def amenity(amenity_id=None):
    """Retrive amenities"""
    amenities_all = storage.all(Amenity)
    if request.method == 'GET':
        amenities_list = []
        if amenity_id:
            amenity = storage.get(Amenity, amenity_id)
            return jsonify(amenity.to_dict()) if amenity else (abort(404))
        else:
            for v in amenities_all.values():
                amenities_list.append(v.to_dict())
            return jsonify(amenities_list)
    elif request.method == 'DELETE':
        amenity = storage.get(Amenity, amenity_id)
        if amenity:
            storage.delete(amenity)
            storage.save()
            return jsonify({})
        else:
            abort(404)
    elif request.method == 'POST':
        post = request.get_json()
        if post:
            if "name" in post:
                new_amenity = Amenity(**post)
                new_amenity.save()
                return new_amenity.to_dict(), 201
            else:
                return "Missing name", 400
        else:
            return "Not a JSON", 400
    elif request.method == 'PUT':
        amenity = storage.get(Amenity, amenity_id)
        if amenity:
            put = request.get_json()
            if put:
                for k, v in put.items():
                    if k not in ["id", "created_at", "updated_at"]:
                        setattr(amenity, k, v)
                amenity.save()
                return amenity.to_dict()
            else:
                return "Not a JSON", 400
        else:
            abort(404)
