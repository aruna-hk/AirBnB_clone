#!/usr/bin/python3
""" test basemodel module """

import unittest
import os
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test base_mode class"""

    def setUp(self):
        """creat base model object to test"""

        self.model1 = BaseModel()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.model1, BaseModel), True)
        dic_obj = self.model1.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
