#!/usr/bin/python3
from models.review import Review
from models.place import Place
from models.user import User
import unittest
"""importing everything for the `TestReview`"""


class TestReview(unittest.TestCase):
    """
    The TestReview class contains unit tests for the `Review` class,
    including tests for instantiation, string representation, saving,
    and converting to a dictionary.
    """
    def test_instant(self):
        """
        The function tests the instantiation and saving
        of a `Review` object.
        """
        s = Review()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        self.assertEqual("", s.place_id)
        self.assertEqual("", s.user_id)
        self.assertEqual("", s.text)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_string_representation(self):
        """
        The function tests the string representation
        of a `Review` object.
        """
        s = Review()
        f = F"[{s.__class__.__name__}] ({s.id}) {s.__dict__}"
        self.assertEqual(s.__str__(), f)

    def test_save(self):
        """
        The test_save function creates a new instance of the `Review`
        class, saves it, and checks if the updated_at attribute has changed.
        """
        s = Review()
        time = s.updated_at
        s.save()
        self.assertNotEqual(time, s.updated_at)

    def test_to_dict(self):
        """
        The function `test_to_dict` tests the `to_dict`
        method of the `Review` class.
        """
        s = Review()
        p = Place()
        u = User()
        s.place_id = p.id
        s.user_id = u.id
        s.text = "5 star"
        created_at = s.created_at
        updated_at = s.updated_at
        my_dict = s.to_dict()
        self.assertEqual(my_dict.get("__class__"), 'Review')
        self.assertEqual(my_dict.get("created_at"), created_at.isoformat())
        self.assertEqual(my_dict.get("updated_at"), updated_at.isoformat())
        self.assertEqual(s.to_dict().get("place_id"),
                         p.id)
        self.assertEqual(s.to_dict().get("user_id"),
                         u.id)
        self.assertEqual(s.to_dict().get("text"),
                         "5 star")

    def test_kwargs(self):
        """
        The function `test_kwargs` creates a new `Review` object
        using the dictionary as keyword arguments, and asserts that
        the attributes of the original and new objects are equal.
        """
        s = Review()
        p = Place()
        u = User()
        s.place_id = p.id
        s.user_id = u.id
        s.text = "5 star"
        s2 = Review(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)
        self.assertEqual(s.place_id, s2.place_id)
        self.assertEqual(s.user_id, s2.user_id)
        self.assertEqual(s.text, s2.text)
        self.assertFalse(s is s2)


if __name__ == '__main__':
    unittest.main()
