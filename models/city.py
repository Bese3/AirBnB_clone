#!/usr/bin/python3

"""Module city
Contains class City that inherits from BaseModel"""
from models import base_model


class City(base_model.BaseModel):
    """Defines a city where AirBnB places can be found in a State"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
