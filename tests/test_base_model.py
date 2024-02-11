#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUP(self):
        self.model1 = BaseModel()

    def test_object_created(self):
        self.assertTrue(isinstance(self.my_model1, self.BaseModel), True)

if __name__ == "__main__":
    unittest.main()
