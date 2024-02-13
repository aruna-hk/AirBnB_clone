#!/usr/bin/python3
""" storage engine moddules
    serializes and deserialzes objects using json
"""


import inspect
import json
import sys


class FileStorage:
    """ serialization and deserializtion class
        to json and from json file
    """

    __file_path = "file.json"
    __objects = {}

    def objects(self, objects):
        """ sets private variable objects"""

        for key, value in objects.items():
            objects[key] = objects[key].to_dict()

        self.__objects = objects

    def all(self):
        """ all objects getter as python objects """

        recreated_objects = {}
        for key, value in self.__objects.items():
            cls = value["__class__"]
            if (cls == "BaseModel"):
                model = sys.modules['models.base_model'].BaseModel
            else:
                mod = sys.modules['models.{}'.format(cls.lower())]
                model = getattr(mod, cls)
            recreated_objects[key] = model(**value)
        return recreated_objects

    def save(self):
        """save json representation of python objects
           in a file
        """

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
