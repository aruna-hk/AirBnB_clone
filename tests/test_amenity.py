#!/usr/bin/python3
""" test basemodel module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """test amenity model"""

    def setUp(self):
        """ init amenity object to test """

        self.amenity = Amenity()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.amenity, Amenity), True)
        dic_obj = self.amenity.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
