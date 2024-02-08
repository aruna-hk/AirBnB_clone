#!/usr/bin/python3

"""
    base module - creates base attributes to be inherited by all
    other objects
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ define common attributes for other classes """

    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0): 
            self.id, self.created_at = str(uuid4()), datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == "__class__"):
                    pass
                if (key == "updated_at" or key == "created_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """ return string repreentation of object"""

        strr = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__) 
        return strr

    def save(self):
        """modify objects file, and updated updated_at time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ bundle objects attributes in a dictionary including class name"""

        obj_attributes = self.__dict__
        obj_attributes["__class__"] = self.__class__.__name__
        for k, v in obj_attributes.items():
            if (k == "created_at" or k == "updated_at"):
                obj_attributes[k] = v.isoformat()
        return obj_attributes

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
