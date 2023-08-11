#!/usr/bin/python3
from models.state import State
import unittest
"""importing everything for the `TestState` class"""


class TestState(unittest.TestCase):
    """
    The TestState class contains unit tests for the State class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `State` object.
        """
        s = State()
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
        of a `State` object.
        """
        s = State()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `State`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = State()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `State` class.
        """
        s = State()
        created_at = s.created_at
        updated_at = s.updated_at
        s.name = "Addis Ababa"
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'State')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
        self.assertEqual(s.to_dict().get("name"),
                         "Addis Ababa")

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `State` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = State()
        s.name = "Addis Ababa"
        s2 = State(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.name, s2.name)
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
