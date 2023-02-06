#!/usr/bin/python3
"""
This module unit tests the module models/user
"""
import unittest
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """
    Tests all methods of City
    """
    def test_instantiation(self):
        """Tests if instances of City have none-empty attributes"""
        c = City()
        c.name = "New England"
        self.assertIsNotNone(c)
        self.assertIsNotNone(c.id)
        self.assertIsNotNone(c.created_at)
        self.assertIsNotNone(c.updated_at)
        self.assertIsNotNone(c.name)
        c.save()
        self.assertNotEqual(c.created_at, c.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of State"""
        c = City()
        c.name = "New England"
        self.assertEqual(c.__str__(), "[{}] ({}) {}".format(
            c.__class__.__name__, c.id, c.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        City's save() is called"""
        c = City()
        c.name = "New England"
        update_time = c.updated_at
        sleep(0.0001)
        c.save()
        self.assertNotEqual(update_time, c.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of City and makes
        sure it returns the correct dictionary"""
        c = City()
        c.name = "New England"
        created_at = c.created_at.isoformat()
        self.assertEqual(c.to_dict().get("__class__"), "City")
        self.assertEqual(c.to_dict().get("created_at"), created_at)
        self.assertEqual(c.to_dict().get("updated_at"),
                         c.updated_at.isoformat())
        self.assertEqual(c.to_dict().get("name"), "New England")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of BaseModel"""
        c1 = City()
        c1.name = "New England"
        c2 = City(**c1.to_dict())
        self.assertEqual(c1.to_dict(), c2.to_dict())
        self.assertFalse(c1 is c2)

        c1 = City()
        sleep(0.003)
        c1.save()
        self.assertFalse(c1 is c2)
        c2 = City(**c1.to_dict())
        self.assertEqual(c1.to_dict(), c2.to_dict())


if __name__ == '__main__':
    unittest.main()
