#!/usr/bin/python3
"""
This module unit tests the module models/base_model
"""
import unittest
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests all methods of BaseModel
    """
    def test_instantiation(self):
        """Tests if instances of BaseModel have none-empty attributes"""
        m = BaseModel()
        self.assertIsNotNone(m)
        self.assertIsNotNone(m.id)
        self.assertIsNotNone(m.created_at)
        self.assertIsNotNone(m.updated_at)
        m.save()
        self.assertNotEqual(m.created_at, m.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of BaseModel"""
        m = BaseModel()
        self.assertEqual(m.__str__(), "[{}] ({}) {}".format(
            m.__class__.__name__, m.id, m.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        BaseModel's save() is called"""
        m = BaseModel()
        update_time = m.updated_at
        sleep(0.0001)
        m.save()
        self.assertNotEqual(update_time, m.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of BaseModel and makes
        sure it returns the correct dictionary"""
        m = BaseModel()
        created_at = m.created_at.isoformat()
        self.assertEqual(m.to_dict().get("__class__"), "BaseModel")
        self.assertEqual(m.to_dict().get("created_at"), created_at)
        self.assertEqual(m.to_dict().get("updated_at"),
                         m.updated_at.isoformat())

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of BaseModel"""
        m1 = BaseModel()
        m2 = BaseModel(**m1.to_dict())
        self.assertEqual(m1.to_dict(), m2.to_dict())
        self.assertFalse(m1 is m2)

        m1 = BaseModel()
        sleep(0.003)
        m1.save()
        self.assertFalse(m1 is m2)
        m2 = BaseModel(**m1.to_dict())
        self.assertEqual(m1.to_dict(), m2.to_dict())


if __name__ == '__main__':
    unittest.main()
