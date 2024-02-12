#!/usr/bin/python3
""" test city model module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.city import City


class TestcityModel(unittest.TestCase):
    """test city model """

    def setUp(self):
        """init city object to test"""

        self.city = City()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.city, City), True)
        dic_obj = self.city.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
