#!/usr/bin/python3

import unittest

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        from models import base_model
        self.BaseModel = base_model.BaseModel
        self.my_model1 = self.BaseModel()

    def tearDown(self):
        del self.my_model1
        del self.BaseModel

    def test_object_created(self):
        self.assertTrue(isinstance(self.my_model1, self.BaseModel), True)

if __name__ == "__main__":
    unittest.main()
