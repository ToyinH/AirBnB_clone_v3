#!/usr/bin/python3
"""
API Blueprint
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
<<<<<<< HEAD
from api.v1.views.amenities import *
from api.v1.views.places import *


# from api.v1.views.amenities import *
# from api.v1.views.users import *
=======
from api.v1.views.users import *

# from api.v1.views.amenities import *

# from api.v1.views.places import *
>>>>>>> b06e8823f72500932f8e4c84d972338d287cec29
# from api.v1.views.places_reviews import *
# from api.v1.views.places_amenities import *

