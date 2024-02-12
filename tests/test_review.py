#!/usr/bin/python3
""" test reviw module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.review import Review


class Testreview(unittest.TestCase):
    """ test review class"""

    def setUp(self):
        """ startup init review to test """

        self.review = Review()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.review, Review), True)
        dic_obj = self.review.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
