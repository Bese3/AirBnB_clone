#!/usr/bin/python3
from models.user import User
import unittest
"""importing everything for `TestUser` class"""


class TestUser(unittest.TestCase):
    """
    The TestUser class contains unit tests for the User class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `User` object.
        """
        s = User()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        self.assertEqual(type(s.email), str)
        self.assertEqual(type(s.first_name), str)
        self.assertEqual(type(s.last_name), str)
        self.assertEqual(type(s.password), str)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a `User` object.
        """
        s = User()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `User`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = User()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `User` class.
        """
        s = User()
        created_at = s.created_at
        updated_at = s.updated_at
        my_dict = s.to_dict()
        s.email = "AirBnB@gmail.com"
        s.first_name = "AirBnB"
        s.password = "AirBnB123"
        self.assertEqual(my_dict.get("__class__"), 'User')
        self.assertEqual(my_dict.get("created_at"),
                         created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"),
                         updated_at.isoformat())
        self.assertEqual(s.to_dict().get("email"),
                         "AirBnB@gmail.com")
        self.assertEqual(s.to_dict().get("first_name"),
                         "AirBnB")
        self.assertEqual(s.to_dict().get("password"),
                         "AirBnB123")

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `User` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = User()
        s.email = "AirBnB@gmail.com"
        s.first_name = "AirBnB"
        s.password = "AirBnB123"
        s2 = User(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.to_dict().get("email"),
                         s2.to_dict().get("email"))
        self.assertEqual(s.to_dict().get("first_name"),
                         s2.to_dict().get("first_name"))
        self.assertEqual(s.to_dict().get("password"),
                         s2.to_dict().get("password"))
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
