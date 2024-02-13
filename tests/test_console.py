#!/usr/bin/python3
""" console testing
    console accepts command and dispatch to stdout if necessary
"""

import os
from io import StringIO
import console
import unittest
import json
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from unittest.mock import patch


class TestConsole(unittest.TestCase):

    """ TestConsole class,
        test the functionality of console, as a command processor
        objects creation using the creat command
        creat:
                BaseModel, user, place, city, state, amenity and review
                creats object and store there ids
        object destruction using destroy
        displaying objects using show, and all
        object update
        and object count

        each method test each model exclusively and completely
    """

    def setUp(self):
        """ import console from consol """
        self.console = console.HBNBCommand
        with open("file.json", "w") as file:
            json.dump({}, file)

    def test_user_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test user
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat User")

        id1 = f.getvalue()[:-1]
        key1 = "User." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "User." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("User.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("User.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            userobj = User(**obj_dict)
            user_string = str(userobj)
            self.assertEqual(user_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            userobj1 = User(**obj_dict1)
            userobj2 = User(**obj_dict2)
            user_string = str(userobj1) + '\n' + str(userobj2) + '\n'
            self.assertEqual(user_string, output)

        self.console().onecmd("User.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("User.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("User.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_BaseModel_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test BaseModel
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat BaseModel")

        id1 = f.getvalue()[:-1]
        key1 = "BaseModel." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "BaseModel." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("BaseModel.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("BaseModel.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            BaseModelobj = BaseModel(**obj_dict)
            BaseModel_string = str(BaseModelobj)
            self.assertEqual(BaseModel_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            BaseModelobj1 = BaseModel(**obj_dict1)
            BaseModelobj2 = BaseModel(**obj_dict2)
            string = str(BaseModelobj1) + '\n' + str(BaseModelobj2) + '\n'
            self.assertEqual(string, output)

        self.console().onecmd("BaseModel.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("BaseModel.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("BaseModel.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_Place_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test Place
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat Place")

        id1 = f.getvalue()[:-1]
        key1 = "Place." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "Place." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("Place.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("Place.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            Placeobj = Place(**obj_dict)
            Place_string = str(Placeobj)
            self.assertEqual(Place_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            Placeobj1 = Place(**obj_dict1)
            Placeobj2 = Place(**obj_dict2)
            Place_string = str(Placeobj1) + '\n' + str(Placeobj2) + '\n'
            self.assertEqual(Place_string, output)

        self.console().onecmd("Place.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("Place.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Place.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_City_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test City
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat City")

        id1 = f.getvalue()[:-1]
        key1 = "City." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "City." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("City.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("City.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            Cityobj = City(**obj_dict)
            City_string = str(Cityobj)
            self.assertEqual(City_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            Cityobj1 = City(**obj_dict1)
            Cityobj2 = City(**obj_dict2)
            City_string = str(Cityobj1) + '\n' + str(Cityobj2) + '\n'
            self.assertEqual(City_string, output)

        self.console().onecmd("City.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("City.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("City.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_State_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test State
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat State")

        id1 = f.getvalue()[:-1]
        key1 = "State." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "State." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("State.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("State.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            Stateobj = State(**obj_dict)
            State_string = str(Stateobj)
            self.assertEqual(State_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            Stateobj1 = State(**obj_dict1)
            Stateobj2 = State(**obj_dict2)
            State_string = str(Stateobj1) + '\n' + str(Stateobj2) + '\n'
            self.assertEqual(State_string, output)

        self.console().onecmd("State.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("State.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("State.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_Review_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test Review
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat Review")

        id1 = f.getvalue()[:-1]
        key1 = "Review." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "Review." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("Review.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("Review.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            Reviewobj = Review(**obj_dict)
            Review_string = str(Reviewobj)
            self.assertEqual(Review_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            Reviewobj1 = Review(**obj_dict1)
            Reviewobj2 = Review(**obj_dict2)
            Review_string = str(Reviewobj1) + '\n' + str(Reviewobj2) + '\n'
            self.assertEqual(Review_string, output)

        self.console().onecmd("Review.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("Review.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Review.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)

    def test_Amenity_creat_update_destroy_count(self):
        """ object creation takes two forms
            creat <objecttype>
            or
            <objecttype>.creat()
            this function test Amenity
                creat, count, update, destroy, show, all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("creat Amenity")

        id1 = f.getvalue()[:-1]
        key1 = "Amenity." + id1

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.creat()")

        id2 = f.getvalue()[:-1]
        key2 = "Amenity." + id2
        self.assertFalse(id1 == id2)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 2)

        key = "name"
        value = "kiptoo haron"

        with patch("sys.stdout", new=StringIO()) as f:
            update_str = "\"{}\", \"{}\", \"{}\"".format(id1, key, value)
            self.console().onecmd("Amenity.update({})".format(update_str))

        out = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1][key], value)

        update_dict = {"age": 23, "school": "cuk"}
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "\"{}\", {})".format(id1, update_dict)
            self.console().onecmd("Amenity.update({})".format(cmd))

        with open("file.json", "r") as file:
            jstr = json.load(file)
            self.assertEqual(jstr[key1]['age'], 23)
            self.assertEqual(jstr[key1]['school'], "cuk")

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict = jstr[key1]
            Amenityobj = Amenity(**obj_dict)
            Amenity_string = str(Amenityobj)
            self.assertEqual(Amenity_string, output)

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.all()")

        output = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
            obj_dict1 = jstr[key1]
            obj_dict2 = jstr[key2]
            Amenityobj1 = Amenity(**obj_dict1)
            Amenityobj2 = Amenity(**obj_dict2)
            Amenity_string = str(Amenityobj1) + '\n' + str(Amenityobj2) + '\n'
            self.assertEqual(Amenity_string, output)

        self.console().onecmd("Amenity.destroy(\"{}\")".format(id1))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 1)
        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.show(\"{}\")".format(id1))

        output = f.getvalue()[:-1]

        self.assertEqual(output, "** no instance found **")

        self.console().onecmd("Amenity.destroy(\"{}\")".format(id2))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console().onecmd("Amenity.count()")

        count = f.getvalue()[:-1]

        self.assertTrue(int(count) == 0)


if __name__ == "__main__":
    unittest.main()
