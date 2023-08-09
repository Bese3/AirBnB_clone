#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
a base class model for other projects
"""


class BaseModel:
    """
    The `BaseModel` class is a base class that provides common
    functionality for creating and updating objects, as well as
    converting objects to dictionaries and string representations.
    """
    def __init__(self, *args, **kwargs):
        """
        The above function initializes an object with a unique
        ID and timestamps for creation and update.
        """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for i, j in zip(kwargs.keys(), kwargs.values()):
                if i != "__class__":
                    if i == "created_at" or i == "updated_at":
                        j = datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, i, j)

    def save(self):
        """
        The function updates the "updated_at" attribute of
        an object with the current datetime.
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        The function `to_dict` converts an object's attributes
        into a dictionary,including the object's class name
        and creation/update timestamps.
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects

    def __str__(self):
        """
        The above function returns a string representation of an object,
        including its class name, id, and attributes.
        """
        return F"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
