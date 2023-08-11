#!/usr/bin/python3
from models.base_model import BaseModel
"""importing everything for `Review` class"""


class Review(BaseModel):
    """
     The Review class represents a review for a place,
     with attributes for the place ID, user ID, and
     text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
