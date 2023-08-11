#!/usr/bin/python3
from models.base_model import BaseModel
"""importing everything for `City` class"""


class City(BaseModel):
    """
    The City class is a subclass of BaseModel
    and represents a city with a state ID and a name.
    """
    state_id = ""
    name = ""
