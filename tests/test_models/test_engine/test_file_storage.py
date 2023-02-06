#!/usr/bin/python3

"""Module test_file_storage
Contains unittest TestFileStorage
"""
import unittest
import os
import models


class TestFileStorage(unittest.TestCase):
    """Tests the module models/engine/file_storage.py"""
    def setUp(self):
        """Sets up instance variables to be used throughout the tests"""
        self.storage = models.storage
        self.BaseModel = models.base_model.BaseModel
        self.file_name = "file.json"

    def test_non_existent_file(self):
        """Tests if FileStorage handles non-existent object storage file
        works correctly"""
        file_exists = False

        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                file_exists = True
                file_contents = f.read()
            os.remove(self.file_name)

        self.storage.reload()
        bm = self.BaseModel()
        bm.save()
        all_objs = self.storage.all()
        self.assertTrue(bm in all_objs.values())
        self.assertTrue(len(all_objs.keys()) == 1)

        if file_exists:
            with open(self.file_name, "w") as f:
                f.write(file_contents)
        else:
            os.remove(self.file_name)

    def test_empty_file(self):
        """Tests if FileStorage handles empty object storage file works
        correctly"""

        file_contents = ""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                file_contents = f.read()
            with open(self.file_name, "w") as f:
                f.seek(0)
                f.write("")

        self.storage.reload()
        bm = self.BaseModel()
        bm.save()
        all_objs = self.storage.all()
        self.assertTrue(bm in all_objs.values())
        self.assertTrue(len(all_objs.keys()) == 1)

        with open(self.file_name, "w") as f:
            f.write(file_contents)


if __name__ == '__main__':
    unittest.main()
