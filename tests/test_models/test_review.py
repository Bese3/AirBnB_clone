#!/usr/bin/python3
"""
This module unit tests the module models/review
"""
import unittest
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Tests all methods of Review
    """
    def test_instantiation(self):
        """Tests if instances of Review have none-empty attributes"""
        r = Review()
        r.text = "This place was wonderful!"
        self.assertIsNotNone(r)
        self.assertIsNotNone(r.id)
        self.assertIsNotNone(r.created_at)
        self.assertIsNotNone(r.updated_at)
        self.assertIsNotNone(r.text)
        r.save()
        self.assertNotEqual(r.created_at, r.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of Review"""
        r = Review()
        r.text = "This place was wonderful!"
        self.assertEqual(r.__str__(), "[{}] ({}) {}".format(
            r.__class__.__name__, r.id, r.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        Review's save() is called"""
        r = Review()
        r.text = "This place was wonderful!"
        update_time = r.updated_at
        sleep(0.0001)
        r.save()
        self.assertNotEqual(update_time, r.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of Review and makes
        sure it returns the correct dictionary"""
        r = Review()
        r.text = "This place was wonderful!"
        created_at = r.created_at.isoformat()
        self.assertEqual(r.to_dict().get("__class__"), "Review")
        self.assertEqual(r.to_dict().get("created_at"), created_at)
        self.assertEqual(r.to_dict().get("updated_at"),
                         r.updated_at.isoformat())
        self.assertEqual(r.to_dict().get("text"), "This place was wonderful!")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of Review"""
        r1 = Review()
        r1.text = "This place was wonderful!"
        r2 = Review(**r1.to_dict())
        self.assertEqual(r1.to_dict(), r2.to_dict())
        self.assertFalse(r1 is r2)

        r1 = Review()
        sleep(0.003)
        r1.save()
        self.assertFalse(r1 is r2)
        r2 = Review(**r1.to_dict())
        self.assertEqual(r1.to_dict(), r2.to_dict())


if __name__ == '__main__':
    unittest.main()
