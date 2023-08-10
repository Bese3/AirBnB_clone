#!/usr/bin/python3
from models.place import Place
from models.user import User
from models.city import City
import unittest
"""importing everything for the `TestBaseModel`"""


class TestPlace(unittest.TestCase):
    """
    The TestPlace class contains unit tests for the `Place` class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `Place` object.
        """
        s = Place()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        self.assertEqual(type(s.city_id), str)
        self.assertEqual(type(s.user_id), str)
        self.assertEqual(type(s.name), str)
        self.assertEqual(type(s.description), str)
        self.assertEqual(type(s.number_rooms), int)
        self.assertEqual(type(s.number_bathrooms), int)
        self.assertEqual(type(s.max_guest), int)
        self.assertEqual(type(s.price_by_night), int)
        self.assertEqual(type(s.latitude), float)
        self.assertEqual(type(s.longitude), float)
        self.assertEqual(type(s.amenity_ids), list)
        for i in s.amenity_ids:
            self.assertEqual(type(i), str)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a `Place` object.
        """
        s = Place()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `Place`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = Place()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `Place` class.
        """
        s = Place()
        c = City()
        u = User()
        created_at = s.created_at
        updated_at = s.updated_at
        s.city_id = c.id
        s.user_id = u.id
        s.name = "Intercontinential Hotel"
        s.description = "around Kazanchis"
        s.number_rooms = 100
        s.number_bathrooms = 100
        s.max_guest = 80
        s.price_by_night = 2000
        s.latitude = -21.88413
        s.longitude = -173.22488
        s.amenity_ids = [s.city_id, s.user_id]
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'Place')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
        self.assertEqual(s.to_dict().get("city_id"),
                         c.id)
        self.assertEqual(s.to_dict().get("user_id"),
                         u.id)
        self.assertEqual(s.to_dict().get("name"),
                         "Intercontinential Hotel")
        self.assertEqual(s.to_dict().get("description"),
                         "around Kazanchis")
        self.assertEqual(s.to_dict().get("number_rooms"),
                         100)
        self.assertEqual(s.to_dict().get("number_bathrooms"),
                         100)
        self.assertEqual(s.to_dict().get("max_guest"),
                         80)
        self.assertEqual(s.to_dict().get("price_by_night"),
                         2000)
        self.assertEqual(s.to_dict().get("latitude"),
                         -21.88413)
        self.assertEqual(s.to_dict().get("longitude"),
                         -173.22488)
        j = 0
        for i in s.to_dict().get("amenity_ids"):
            self.assertEqual(type(i), str)
            self.assertEqual(i, s.amenity_ids[j])
            j += 1

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `Place` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = Place()
        c = City()
        u = User()
        s.city_id = c.id
        s.user_id = u.id
        s.name = "Intercontinential Hotel"
        s.description = "around Kazanchis"
        s.number_rooms = 100
        s.number_bathrooms = 100
        s.max_guest = 80
        s.price_by_night = 2000
        s.latitude = -21.88413
        s.longitude = -173.22488
        s.amenity_ids = [s.city_id, s.user_id]
        s2 = Place(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.city_id, s2.city_id)
        self.assertEqual(s.user_id, s2.user_id)
        self.assertEqual(s.name, s2.name)
        self.assertEqual(s.description, s2.description)
        self.assertEqual(s.number_rooms, s2.number_rooms)
        self.assertEqual(s.number_bathrooms, s2.number_bathrooms)
        self.assertEqual(s.max_guest, s2.max_guest)
        self.assertEqual(s.price_by_night, s2.price_by_night)
        self.assertEqual(s.latitude, s2.latitude)
        self.assertEqual(s.longitude, s2.longitude)
        self.assertEqual(s.amenity_ids, s2.amenity_ids)
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
