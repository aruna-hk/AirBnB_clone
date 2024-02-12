#!/usr/bin/python3
""" console test """

import sys
import os
import json
from io import StringIO
from models import base_model
from models import user
from models import city
from models import place
from models import state
from models import amenity
from models import review
import unittest
from unittest.mock import patch
import console


class test_console(unittest.TestCase):
    """ this class test console """

    def setUp(self):
        self.BaseModel = base_model.BaseModel
        self.User = user.User
        self.City = city.City
        self.Place = place.Place
        self.State = state.State
        self.Amenity = amenity.Amenity
        self.Review = review.Review

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
        dict2 = recreated_obj.to_dict()
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
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("BaseModel.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_User_creat(self):
        """test User creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first User """

            console.HBNBCommand().onecmd("User.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37)
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key1 = "User." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.User(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second User """

            console.HBNBCommand().onecmd("User.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "User." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("User.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_City_creat(self):
        """test City creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first City """

            console.HBNBCommand().onecmd("City.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37)
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key1 = "City." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.City(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second City """

            console.HBNBCommand().onecmd("City.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "City." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("City.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_Place_creat(self):
        """test Place creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first Place """

            console.HBNBCommand().onecmd("Place.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37)
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key1 = "Place." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.Place(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Place """

            console.HBNBCommand().onecmd("Place.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "Place." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.count()")
        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("Place.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_State_creat(self):
        """test State creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first State """

            console.HBNBCommand().onecmd("State.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37)
        with open("file.json", "r") as file:
            jstr = json.load(file)

        dic = eval(repr(jstr))
        obj_key1 = "State." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.State(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second State """

            console.HBNBCommand().onecmd("State.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "State." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.count()")
        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("State.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_Amenity_creat(self):
        """test Amenity creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first Amenity """

            console.HBNBCommand().onecmd("Amenity.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37)
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key1 = "Amenity." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.Amenity(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Amenity """

            console.HBNBCommand().onecmd("Amenity.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "Amenity." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.count()")
        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("Amenity.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")

    def test_Review_creat(self):
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
        obj_key1 = "Review." + captured_id1[:-1]
        obj_dict1 = dic[obj_key1]
        recreated_obj = self.Review(**obj_dict1)
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Review """

            console.HBNBCommand().onecmd("Review.creat()")
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)

        obj_key2 = "Review." + captured_id2[:-1]
        obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key1]) + '\n' + str(obj_dict2[obj_key2]) + '\n'

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        with patch('sys.stdout', new=StringIO()) as f:
            """ no id """
            console.HBNBCommand().onecmd("Review.destroy()")
        captured = f.getvalue()
        self.assertEqual(captured, "** instance id missing **\n")
        os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
