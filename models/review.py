#!/usr/bin/python3

"""Module review
Contains class Amenity that inherits from BaseModel"""
from models import base_model


class Review(base_model.BaseModel):
    """Defines the review a user makes for a place"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
