#!/usr/bin/python3
""" test user module"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """test user class """

    def setUp(self):
        """set up creation of user object """

        self.user = User()

    def test_User_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.user, User), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.user.updated_at, datetime))
        self.assertTrue(isinstance(self.user.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.user.id, str))
        self.assertEqual(len(self.user.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.user.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.user.name = "kiptoo haron"

        self.assertTrue("name" in self.user.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = User()

        self.assertFalse(obj2 == self.user)

    def test_user_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.user.to_dict()

        recreat = User(**obj_dict)
        self.assertTrue(isinstance(recreat, User))


if __name__ == "__main__":
    unittest.main()
