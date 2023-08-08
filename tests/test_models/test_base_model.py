#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
"""importing everything for the `TestBaseModel`"""


class TestBaseModel(unittest.TestCase):
    """
    The TestBaseModel class contains unit tests for the BaseModel class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a BaseModel object.
        """
        s = BaseModel()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a BaseModel object.
        """
        s = BaseModel()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the BaseModel
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = BaseModel()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `BaseModel` class.
        """
        s = BaseModel()
        created_at = s.created_at
        updated_at = s.updated_at
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'BaseModel')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
