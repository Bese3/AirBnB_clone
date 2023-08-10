#!/usr/bin/python3
from models.city import City
import unittest
"""importing everything for the `TestCity`"""


class TestCity(unittest.TestCase):
    """
    The `TestCity` class contains unit tests for the `City` class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `City` object.
        """
        s = City()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        self.assertEqual("", s.state_id)
        self.assertEqual("", s.name)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a `City` object.
        """
        s = City()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `City`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = City()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `City` class.
        """
        s = City()
        created_at = s.created_at
        updated_at = s.updated_at
        s.state_id = s.id
        s.name = "Addis Ababa"
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'City')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
        self.assertEqual(s.to_dict().get("state_id"), s.id)
        self.assertEqual(s.to_dict().get("name"), "Addis Ababa")

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `City` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = City()
        s.state_id = s.id
        s.name = "Addis Ababa"
        s2 = City(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.to_dict().get("state_id"),
                         s2.to_dict().get("state_id"))
        self.assertEqual(s.to_dict().get("name"),
                         s2.to_dict().get("name"))
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
