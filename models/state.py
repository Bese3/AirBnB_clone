#!/usr/bin/python3

"""Module state
Contains class State that inherits from BaseModel"""
from models import base_model


class State(base_model.BaseModel):
    """Defines a state where AirBnB places can be found"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
