#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""
a base class model for other projects
"""


class BaseModel:
    """
    The `BaseModel` class is a base class that provides common
    functionality for creating and updating objects, as well as
    converting objects to dictionaries and string representations.
    """
    def __init__(self):
        """
        The above function initializes an object with a unique
        ID and timestamps for creation and update.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        The function updates the "updated_at" attribute of
        an object with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        The function `to_dict` converts an object's attributes
        into a dictionary,including the object's class name
        and creation/update timestamps.
        """
        my_dict = self.__dict__
        my_dict.update([("__class__", self.__class__.__name__),
                        ("created_at", self.created_at.isoformat()),
                        ("updated_at", self.updated_at.isoformat())])
        return my_dict

    def __str__(self):
        """
        The above function returns a string representation of an object,
        including its class name, id, and attributes.
        """
        return F"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
