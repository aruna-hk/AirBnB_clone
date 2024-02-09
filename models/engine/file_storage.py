#!/usr/bin/python3

import json
try:
    from . import base_model
except Exception as e:
    pass

class FileStorage:
    """ serialization and deserializtion class """

    __file_path = "file.json"
    __objects = {}
    __base = None

    @staticmethod
    def file_path(file_path="file.json"):
        """ sets file to store json representtion of objects """
        FileStorage.__file_path = file_path


    @staticmethod
    def objects(objects):
        FileStorage.__objects = objects



    def all(self):
        """ all objects getter as python objects """
        return self.__objects

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
