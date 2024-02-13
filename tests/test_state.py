#!/usr/bin/python3
""" test state module"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """test state class """

    def setUp(self):
        """set up creation of state object """

        self.state = State()

    def test_State_created(self):
        """ test object is instance of base_model"""

        self.assertTrue(isinstance(self.state, State), True)

    def test_time_instance(self):
        """ test updated at and created at are instance of time"""

        self.assertTrue(isinstance(self.state.updated_at, datetime))
        self.assertTrue(isinstance(self.state.created_at, datetime))

    def test_id_is_str(self):
        """test obj id is str of len 36"""

        self.assertTrue(isinstance(self.state.id, str))
        self.assertEqual(len(self.state.id), 36)

    def test_to_dict(self):
        """ check to_dict function"""

        object_dict = self.state.to_dict()
        self.assertTrue(isinstance(object_dict, dict))

    def test_dynamic_update(self):
        """test dynamic update"""

        self.state.name = "kiptoo haron"

        self.assertTrue("name" in self.state.to_dict())

    def test_object_from_same_class_unequal(self):
        """test obj == obj2"""

        obj2 = State()

        self.assertFalse(obj2 == self.state)

    def test_state_reconstruction(self):
        """ reconstructing object with dictionary """

        obj_dict = self.state.to_dict()

        recreat = State(**obj_dict)
        self.assertTrue(isinstance(recreat, State))


if __name__ == "__main__":
    unittest.main()
