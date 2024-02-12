#!/usr/bin/python3
""" test place model module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.place import Place


class Testplacemodel(unittest.TestCase):
    """ test base model class"""

    def setUp(self):
        """set up place object to test"""
        self.place = Place()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.place, Place), True)
        dic_obj = self.place.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
