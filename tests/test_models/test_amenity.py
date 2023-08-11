#!/usr/bin/python3
from models.amenity import Amenity
import unittest
"""importing everything for the `TestAmenity` class"""


class TestAmenity(unittest.TestCase):
    """
    The TestAmenity class contains unit tests for the `Amenity` class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `Amenity` object.
        """
        s = Amenity()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        self.assertEqual("", s.name)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a `Amenity` object.
        """
        s = Amenity()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `Amenity`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = Amenity()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `Amenity` class.
        """
        s = Amenity()
        created_at = s.created_at
        updated_at = s.updated_at
        s.name = "Addis Ababa"
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'Amenity')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
        self.assertEqual(s.to_dict().get("name"),
                         "Addis Ababa")

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `Amenity` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = Amenity()
        s.name = "Addis Ababa"
        s2 = Amenity(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.name, s2.name)
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
