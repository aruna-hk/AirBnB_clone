#!/usr/bin/python3
""" test basemodel module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test basemodel class """

    def setUp(self):
        """set up creation of basemodel object """

        self.model1 = BaseModel()

    def test_object_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.model1, BaseModel), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.model1.updated_at, datetime))
        self.assertTrue(isinstance(self.model1.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.model1.id, str))
        self.assertEqual(len(self.model1.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.model1.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.model1.name = "kiptoo haron"

        self.assertTrue("name" in self.model1.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = BaseModel()

        self.assertFalse(obj2 == self.model1)

    def test_basemodel_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.model1.to_dict()

        recreat = BaseModel(**obj_dict)
        self.assertTrue(isinstance(recreat, BaseModel))


if __name__ == "__main__":
    unittest.main()
