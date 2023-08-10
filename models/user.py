#!/usr/bin/python3
from models.base_model import BaseModel
"""importing everything for the User class"""


class User(BaseModel):
    """
    The class represents a user with attributes such
    as `email`, `password`, `first_name`, and `last_name`.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
