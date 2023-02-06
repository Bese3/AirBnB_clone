#!/usr/bin/python3
"""
This module unit tests the module models/state
"""
import unittest
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests all methods of State
    """
    def test_instantiation(self):
        """Tests if instances of State have none-empty attributes"""
        s = State()
        s.name = "New Hampshire"
        self.assertIsNotNone(s)
        self.assertIsNotNone(s.id)
        self.assertIsNotNone(s.created_at)
        self.assertIsNotNone(s.updated_at)
        self.assertIsNotNone(s.name)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of State"""
        s = State()
        s.name = "New Hampshire"
        self.assertEqual(s.__str__(), "[{}] ({}) {}".format(
            s.__class__.__name__, s.id, s.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        State's save() is called"""
        s = State()
        s.name = "New Hampshire"
        update_time = s.updated_at
        sleep(0.0001)
        s.save()
        self.assertNotEqual(update_time, s.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of State and makes
        sure it returns the correct dictionary"""
        s = State()
        s.name = "New Hampshire"
        created_at = s.created_at.isoformat()
        self.assertEqual(s.to_dict().get("__class__"), "State")
        self.assertEqual(s.to_dict().get("created_at"), created_at)
        self.assertEqual(s.to_dict().get("updated_at"),
                         s.updated_at.isoformat())
        self.assertEqual(s.to_dict().get("name"), "New Hampshire")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of State"""
        s1 = State()
        s1.name = "New Hampshire"
        s2 = State(**s1.to_dict())
        self.assertEqual(s1.to_dict(), s2.to_dict())
        self.assertFalse(s1 is s2)

        s1 = State()
        sleep(0.003)
        s1.save()
        self.assertFalse(s1 is s2)
        s2 = State(**s1.to_dict())
        self.assertEqual(s1.to_dict(), s2.to_dict())


if __name__ == '__main__':
    unittest.main()
