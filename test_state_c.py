#!/usr/bin/python3
""" console test """

import sys
import json
from io import StringIO
from models import user
from models import base_model
from models import place
from models import city
from models import state
from models import amenity
from models import review
import unittest
from unittest.mock import patch
import console

class test_console(unittest.TestCase):
    """ this class test console """

    def setUp(self):
        self.User = user.User
        self.BaseModel = base_model.BaseModel
        self.Place = place.Place
        self.City = city.City
        self.State = state.State
        self.Amenity = amenity.Amenity
        self.Review = review.Review

    def test_user_model(self):
        """test user creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first user """

            console.HBNBCommand().onecmd("User.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37) 
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key = "User." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.User(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second user """

            console.HBNBCommand().onecmd("User.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "User." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")


if __name__ == "__main__":
    unittest.main()
