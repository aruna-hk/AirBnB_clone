#!/usr/bin/python3
""" console test """

import sys
import os
import json
from io import StringIO
from models import base_model
import unittest
from unittest.mock import patch
import console

class test_console(unittest.TestCase):
    """ this class test console """

    def setUp(self):
        self.BaseModel = base_model.BaseModel

    def test_BaseModel_creat(self):
        """test BaseModel creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first BaseModel """

            console.HBNBCommand().onecmd("BaseModel.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37) 
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key1 = "BaseModel." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.BaseModel(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second BaseModel """

            console.HBNBCommand().onecmd("BaseModel.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "BaseModel." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("BaseModel.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")

  
        os.remove("file.json")

    def test_base_update(self):

        """test base model update """

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.creat()") 
        with open("file.json", "r") as file:
            jstr = json.load(file)

        dict_ = eval(repr(jstr))
        print(dict_)
        ukey = "name"
        uvalue = "kiptoo"
        key = "\"" + dict_["__class__"] + "." +  dict_[id] + "\""
        print(key)
        console.HBNBCommand().onecmd("BaseModel.update({}, {}, {}".format(key, ukey, uvalue))

if __name__ == "__main__":
    unittest.main()
