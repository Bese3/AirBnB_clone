#!/usr/bin/python3
"""
This module unit tests the module models/amenity
"""
import unittest
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Tests all methods of Amenity
    """
    def test_instantiation(self):
        """Tests if instances of Amenity have none-empty attributes"""
        a = Amenity()
        a.name = "Splendid"
        self.assertIsNotNone(a)
        self.assertIsNotNone(a.id)
        self.assertIsNotNone(a.created_at)
        self.assertIsNotNone(a.updated_at)
        self.assertIsNotNone(a.name)
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of Amenity"""
        a = Amenity()
        a.name = "Splendid"
        self.assertEqual(a.__str__(), "[{}] ({}) {}".format(
            a.__class__.__name__, a.id, a.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        Amenity's save() is called"""
        a = Amenity()
        a.name = "Splendid"
        update_time = a.updated_at
        sleep(0.0001)
        a.save()
        self.assertNotEqual(update_time, a.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of Amenity and makes
        sure it returns the correct dictionary"""
        a = Amenity()
        a.name = "Splendid"
        created_at = a.created_at.isoformat()
        self.assertEqual(a.to_dict().get("__class__"), "Amenity")
        self.assertEqual(a.to_dict().get("created_at"), created_at)
        self.assertEqual(a.to_dict().get("updated_at"),
                         a.updated_at.isoformat())
        self.assertEqual(a.to_dict().get("name"), "Splendid")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of Amenity"""
        a1 = Amenity()
        a1.name = "Splendid"
        a2 = Amenity(**a1.to_dict())
        self.assertEqual(a1.to_dict(), a2.to_dict())
        self.assertFalse(a1 is a2)

        a1 = Amenity()
        sleep(0.003)
        a1.save()
        self.assertFalse(a1 is a2)
        a2 = Amenity(**a1.to_dict())
        self.assertEqual(a1.to_dict(), a2.to_dict())


if __name__ == '__main__':
    unittest.main()
