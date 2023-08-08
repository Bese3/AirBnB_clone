#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    def test_instant(self):
        s = BaseModel()
        self.assertNotEqual(None, s)
        self.assertNotEqual(None, s.id)
        self.assertNotEqual(None, s.created_at)
        self.assertNotEqual(None, s.updated_at)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)
