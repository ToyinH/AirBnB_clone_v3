#!/usr/bin/python3
"""
API endpoint
"""


from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown(exception):
    """Remove current session"""
    storage.close()


if __name__ == '__main__':
    """Main function"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
