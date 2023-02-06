#!/usr/bin/python3

"""Module user
Contains class User that inherits from BaseModel"""
from models import base_model


class User(base_model.BaseModel):
    """Defines a user of AirBnB class which has a first & last name,
    email and password"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes just like it's parent class BaseModel does"""
        super().__init__(*args, **kwargs)
