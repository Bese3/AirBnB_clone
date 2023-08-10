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
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = list(str)
