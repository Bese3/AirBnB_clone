#!/usr/bin/python3
"""
This module unit tests the module models/state
"""
import unittest
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests all methods of User
    """
    def test_instantiation(self):
        """Tests if instances of User have none-empty attributes"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        self.assertIsNotNone(u)
        self.assertIsNotNone(u.id)
        self.assertIsNotNone(u.created_at)
        self.assertIsNotNone(u.updated_at)
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of User"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        self.assertEqual(u.__str__(), "[{}] ({}) {}".format(
            u.__class__.__name__, u.id, u.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when User's save() is
        called"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        update_time = u.updated_at
        sleep(0.0001)
        u.save()
        self.assertNotEqual(update_time, u.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of User and makes
        sure it returns the correct dictionary"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        created_at = u.created_at.isoformat()
        self.assertEqual(u.to_dict().get("__class__"), "User")
        self.assertEqual(u.to_dict().get("created_at"), created_at)
        self.assertEqual(u.to_dict().get("updated_at"),
                         u.updated_at.isoformat())
        self.assertEqual(u.to_dict().get("email"), "alanwalker@ubi.com")
        self.assertEqual(u.to_dict().get("password"), "as34b2")
        self.assertEqual(u.to_dict().get("first_name"), "Alan")
        self.assertEqual(u.to_dict().get("last_name"), "Walker")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of User"""
        u1 = User()
        u1.email = "alanwalker@ubi.com"
        u1.password = "as34b2"
        u1.first_name = "Alan"
        u1.last_name = "Walker"
        u2 = User(**u1.to_dict())
        self.assertEqual(u1.to_dict(), u2.to_dict())
        self.assertFalse(u1 is u2)

        u1 = User()
        sleep(0.003)
        u1.save()
        self.assertFalse(u1 is u2)
        u2 = User(**u1.to_dict())
        self.assertEqual(u1.to_dict(), u2.to_dict())


if __name__ == '__main__':
    unittest.main()
