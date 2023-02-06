#!/usr/bin/python3

"""Module amenity
Contains class Place that inherits from BaseModel"""
from models import base_model


class Place(base_model.BaseModel):
    """Defines a place for rent"""
    city_id = ""
    state_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
