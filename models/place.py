#!/usr/bin/python3
from models.base_model import BaseModel
"""importing everything for `Place` class"""


class Place(BaseModel):
    """
    The class "Place" represents a place with
    various attributes such as city_id, user_id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
