#!/usr/bin/python3
""" console test """

import sys
import json
from io import StringIO
from models import review
import unittest
from unittest.mock import patch
import console

class test_console(unittest.TestCase):
    """ this class test console """

    def setUp(self):
        self.Review = review.Review

    def test_Review_model(self):
        """test Review creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first Review """

            console.HBNBCommand().onecmd("Review.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37) 
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key = "Review." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.Review(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Review """

            console.HBNBCommand().onecmd("Review.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "Review." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n' 

        """ test Review.all() """

        with patch('sys.stdout', "r") as f:
            console.HBNBCommand().onecmd("User.all()")
#        captured = f.getvalue()
 #       print(captured)
       

if __name__ == "__main__":
    unittest.main()
