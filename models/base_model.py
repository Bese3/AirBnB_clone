#!/usr/bin/python3

"""
This module contains the class BaseModel. Description of th class can be found
in the class's docstring
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel object, either from kwargs which contains the
        object's information or by creating anew one if kwargs is empty
        """
        if kwargs == {}:
            self.id = str(uuid4())  # Generate a unique ID for the instance
            # Save the time the object was created
            self.created_at = datetime.now()
            # Updated every time the object is updated. Initialized to current
            # time when object is created
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for i, j in zip(kwargs.keys(), kwargs.values()):
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    self.__setattr__(i, datetime.fromisoformat(j))
                    continue
                self.__setattr__(i, j)

    def __str__(self):
        """Overriding the __str__ method to display a
        custom string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves this object to the storage and updates @updated_at to the
        current date & time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        dict_repr = {}
        dict_repr.update(self.__dict__)
        dict_repr.update([("__class__", self.__class__.__name__),
                          ("created_at", self.created_at.isoformat()),
                          ("updated_at", self.updated_at.isoformat())])
        return dict_repr
