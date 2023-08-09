#!/usr/bin/python3
import models
import unittest
import os
import json
"""importing everything for `TestFileStorage` class"""


class TestFileStorage(unittest.TestCase):
    """
    The TestFileStorage class contains unit tests
    for the FileStorage class in a Python program.
    """

    def setUp(self):
        """
        The setUp function initializes variables for storage,
        BaseModel, and file_name.
        """
        self.storage = models.storage
        self.BaseModel = models.base_model.BaseModel
        self.file_name = "file.json"

    def test_FileStorage_instantiation_no_args(self):
        """
        The function tests if the instantiation of the FileStorage
        class is successful without any arguments.
        """
        self.assertTrue("FileStorage" in str(type(self.storage)))

    def test_FileStorage_instantiation_with_arg(self):
        """
        The function tests the instantiation of the FileStorage
        class with an argument.
        """
        with self.assertRaises(TypeError):
            file = self.storage(None)

    def test_all(self):
        """
        The function tests if the type of the returned value
        from models.storage.all() is a dictionary.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """
        The function tests if the type of the returned value
        from the `all()` method of `self.storage` is a dictionary.
        """
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """
        The function `test_new` tests if a new instance of
        `BaseModel` is correctly added to the storage.
        """
        bm = self.BaseModel()
        self.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, self.storage.all().keys())
        self.assertIn(bm, self.storage.all().values())

    def test_save(self):
        """
        The function `test_save` tests if a BaseModel object
        is saved correctly by checking if its ID is present in a file.
        """
        bm = self.BaseModel()
        self.storage.new(bm)
        self.storage.save()
        text = ""
        try:
            with open(self.file_name, mode="r", encoding="utf-8") as f:
                text = f.read()
                self.assertIn("BaseModel." + bm.id, text)
        except FileNotFoundError:
            pass

    def test_reload(self):
        """
        The function `test_reload` tests the `reload` method
        of a storage object by comparing the reloaded data
        with the data read from a file.
        """
        bm = self.BaseModel()
        self.storage.new(bm)
        bm.save()
        text = ""
        try:
            with open(self.file_name, mode="r", encoding="utf-8") as f:
                text = json.loads(f.read())
        except FileNotFoundError:
            pass
        self.assertEqual(self.storage.reload(), text)

    def test_reload_with_arg(self):
        """
        The function `test_reload_with_arg` tests that calling
        the `reload` method of the `storage` object with a `None`
        argument raises a `TypeError`.
        """
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
