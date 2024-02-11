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
        #testing user.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_user
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("User.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("User.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("User.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("User.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("User.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("User.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")

    def test_BaseModel_model(self):
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
        obj_key = "BaseModel." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
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
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing BaseModel.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_BaseModel
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("BaseModel.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("BaseModel.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")


    def test_City_model(self):
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
        obj_key = "City." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.City(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second City """

            console.HBNBCommand().onecmd("City.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "City." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing City.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_City
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("City.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("City.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("City.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("City.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("City.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("City.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")


    def test_Amenity_model(self):
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
        obj_key = "Amenity." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.Amenity(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Amenity """

            console.HBNBCommand().onecmd("Amenity.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "Amenity." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing Amenity.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_Amenity
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Amenity.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Amenity.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Amenity.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Amenity.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("Amenity.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("Amenity.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")


    def test_Place_model(self):
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
        obj_key = "Place." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.Place(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second Place """

            console.HBNBCommand().onecmd("Place.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "Place." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing Place.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_Place
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Place.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Place.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Place.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Place.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("Place.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("Place.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")


    def test_State_model(self):
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
        obj_key = "State." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.State(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second State """

            console.HBNBCommand().onecmd("State.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "State." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing State.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_State
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("State.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("State.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("State.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("State.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("State.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("State.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")

    def test_Review_model(self):
        """test Review creation"""

        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:

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
        dict2 = recreated_obj.to_dict()
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:

            console.HBNBCommand().onecmd("Review.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "Review." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')


        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Review.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Review.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Review.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("Review.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("Review.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
        console.HBNBCommand().onecmd("Review.destroy({})".format(uid2))       
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.count()")
        out = f.getvalue()
        self.assertEqual(out, "0\n")




       

if __name__ == "__main__":
    unittest.main()
