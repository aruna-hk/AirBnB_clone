#!/usr/bin/python3
""" test basemodel module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """ test user class """

    def setUp(self):
        """ set up user object to test """

        self.user = User()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.user, User), True)
        dic_obj = self.user.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
