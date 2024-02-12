#!/usr/bin/python3
""" test state module """

import unittest
import os
import json
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    """ test state model """
    def setUp(self):
        """set up state model to test """

        self.state = State()

    def test_base_object(self):
        """test object creat is instance of basemodel"""
        self.assertTrue(isinstance(self.state, State), True)
        dic_obj = self.state.to_dict()
        self.assertTrue(isinstance(dic_obj, dict))


if __name__ == "__main__":
    unittest.main()
