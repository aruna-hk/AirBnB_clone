#!/usr/bin/python3
""" test city module"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """test city class """

    def setUp(self):
        """set up creation of city object """

        self.city = City()

    def test_City_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.city, City), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.city.updated_at, datetime))
        self.assertTrue(isinstance(self.city.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.city.id, str))
        self.assertEqual(len(self.city.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.city.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.city.name = "kiptoo haron"

        self.assertTrue("name" in self.city.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = City()

        self.assertFalse(obj2 == self.city)

    def test_city_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.city.to_dict()

        recreat = City(**obj_dict)
        self.assertTrue(isinstance(recreat, City))


if __name__ == "__main__":
    unittest.main()
