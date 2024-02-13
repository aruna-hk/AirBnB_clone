#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model1 = BaseModel()

    def test_object_created(self):
        self.assertTrue(isinstance(self.model1, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
