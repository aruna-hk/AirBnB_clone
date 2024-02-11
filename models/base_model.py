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
                if ((key == "updated_at") or (key == "created_at")):
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """ return string repreentation of object"""

        strr = "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)
        return strr

    def save(self):
        """modify objects file, and updated updated_at time"""

        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """ bundle objects attributes in a dictionary including class name"""

        obj_att = self.__dict__
        obj_att["__class__"] = self.__class__.__name__
        if (type(obj_att["created_at"]) is not str):
            obj_att["created_at"] = obj_att["created_at"].isoformat()
        if (type(obj_att["updated_at"]) is not str):
            obj_att["updated_at"] = obj_att["updated_at"].isoformat()

        return obj_att
