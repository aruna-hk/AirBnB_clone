#!/usr/bin/python3
""" storage engine module"""


import inspect
import json
try:
    from . import base_model
except Exception as e:
    pass


class FileStorage:
    """ serialization and deserializtion class """

    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def file_path(file_path="file.json"):
        """ sets file to store json representtion of objects """
        FileStorage.__file_path = file_path

    def objects(self, objects):
        """ sets private variable objects"""

        for key, value in objects.items():
            objects[key] = objects[key].to_dict()

        self.__objects = objects

    def all(self):
        """ all objects getter as python objects """

        recreated_objects = {}
        caller_module = inspect.getmodule(inspect.stack()[1][0])
        if caller_module:
            for key, value in self.__objects.items():
                class_name = value["__class__"]
                model = getattr(caller_module, class_name)
                recreated_objects[key] = model(**value)
        return recreated_objects

    def save(self):
        """serializes objects to  file"""

        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """deserializes json object t pyobj form file"""
        try:
            file = open(self.__file_path, "r")
            self.__objects = json.load(file)
            file.close()
        except Exception as e:
            pass

    def new(self, obj):
        """add objects to objects dictionary"""

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        dic = obj.to_dict()
        self.__objects[key] = dic
