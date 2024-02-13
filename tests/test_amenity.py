#!/usr/bin/python3
""" test amenity module"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """test amenity class """

    def setUp(self):
        """set up creation of amenity object """

        self.amenity = Amenity()

    def test_Amenity_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.amenity, Amenity), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.amenity.updated_at, datetime))
        self.assertTrue(isinstance(self.amenity.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.amenity.id, str))
        self.assertEqual(len(self.amenity.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.amenity.name = "kiptoo haron"

        self.assertTrue("name" in self.amenity.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = Amenity()

        self.assertFalse(obj2 == self.amenity)

    def test_amenity_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.amenity.to_dict()

        recreat = Amenity(**obj_dict)
        self.assertTrue(isinstance(recreat, Amenity))


if __name__ == "__main__":
    unittest.main()
