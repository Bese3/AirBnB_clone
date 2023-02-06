#!/usr/bin/python3
"""
This module unit tests the module models/place
"""
import unittest
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests all methods of Place
    """
    def test_instantiation(self):
        """Tests if instances of Place have none-empty attributes"""
        p = Place()
        p.name = "1743 Berry St"
        p.description = "A lovely appartment for two"
        p.number_rooms = 2
        p.number_bathrooms = 1
        p.max_guest = 3
        p.price_by_night = 125
        p.latitude = 74.5082
        p.longitude = 12.3484
        self.assertIsNotNone(p)
        self.assertIsNotNone(p.id)
        self.assertIsNotNone(p.created_at)
        self.assertIsNotNone(p.updated_at)
        self.assertIsNotNone(p.name)
        self.assertIsNotNone(p.description)
        self.assertIsNotNone(p.number_rooms)
        self.assertIsNotNone(p.number_bathrooms)
        self.assertIsNotNone(p.max_guest)
        self.assertIsNotNone(p.price_by_night)
        self.assertIsNotNone(p.latitude)
        self.assertIsNotNone(p.longitude)

        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of Place"""
        p = Place()
        p.name = "Splendid"
        self.assertEqual(p.__str__(), "[{}] ({}) {}".format(
            p.__class__.__name__, p.id, p.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        Place's save() is called"""
        p = Place()
        p.name = "1743 Berry St"
        p.description = "A lovely appartment for two"
        p.number_rooms = 2
        p.number_bathrooms = 1
        p.max_guest = 3
        p.price_by_night = 125
        p.latitude = 74.5082
        p.longitude = 12.3484
        update_time = p.updated_at
        sleep(0.0001)
        p.save()
        self.assertNotEqual(update_time, p.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of Place and makes
        sure it returns the correct dictionary"""
        p = Place()
        p.name = "1743 Berry St"
        p.description = "A lovely appartment for two"
        p.number_rooms = 2
        p.number_bathrooms = 1
        p.max_guest = 3
        p.price_by_night = 125
        p.latitude = 74.5082
        p.longitude = 12.3484
        created_at = p.created_at.isoformat()
        self.assertEqual(p.to_dict().get("__class__"), "Place")
        self.assertEqual(p.to_dict().get("created_at"), created_at)
        self.assertEqual(p.to_dict().get("updated_at"),
                         p.updated_at.isoformat())
        self.assertEqual(p.to_dict().get("name"), "1743 Berry St")
        self.assertEqual(p.to_dict().get("description"), "A lovely "
                                                         "appartment for two")
        self.assertEqual(p.to_dict().get("number_rooms"), 2)
        self.assertEqual(p.to_dict().get("number_bathrooms"), 1)
        self.assertEqual(p.to_dict().get("max_guest"), 3)
        self.assertEqual(p.to_dict().get("price_by_night"), 125)
        self.assertEqual(p.to_dict().get("latitude"), 74.5082)
        self.assertEqual(p.to_dict().get("longitude"), 12.3484)

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of Place"""
        p1 = Place()
        p1.name = "1743 Berry St"
        p1.description = "A lovely appartment for two"
        p1.number_rooms = 2
        p1.number_bathrooms = 1
        p1.max_guest = 3
        p1.price_by_night = 125
        p1.latitude = 74.5082
        p1.longitude = 12.3484
        p2 = Place(**p1.to_dict())
        self.assertEqual(p1.to_dict(), p2.to_dict())
        self.assertFalse(p1 is p2)

        p1 = Place()
        sleep(0.003)
        p1.save()
        self.assertFalse(p1 is p2)
        p2 = Place(**p1.to_dict())
        self.assertEqual(p1.to_dict(), p2.to_dict())


if __name__ == '__main__':
    unittest.main()
