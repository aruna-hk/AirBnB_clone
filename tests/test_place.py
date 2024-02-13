#!/usr/bin/python3
""" test place module"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """test place class """

    def setUp(self):
        """set up creation of place object """

        self.place = Place()

    def test_Place_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.place, Place), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.place.updated_at, datetime))
        self.assertTrue(isinstance(self.place.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.place.id, str))
        self.assertEqual(len(self.place.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.place.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.place.name = "kiptoo haron"

        self.assertTrue("name" in self.place.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = Place()

        self.assertFalse(obj2 == self.place)

    def test_place_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.place.to_dict()

        recreat = Place(**obj_dict)
        self.assertTrue(isinstance(recreat, Place))


if __name__ == "__main__":
    unittest.main()
