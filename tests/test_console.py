#!/usr/bin/python3

import console
import os
import unittest
from unittest.mock import patch
# from io import stringIO
import sys

class TestHBNBCommand_prompting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", self.typing.prompt)

    # def test_empty_line(self):
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd(""))
    #         self.assertEqual("", output.getvalue().strip())