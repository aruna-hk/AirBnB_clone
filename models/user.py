#!/usr/bin/python3
""" this module define a user"""

from models import base_model

class User(base_model.BaseModel):
    """ class user, defines a user """

    email = None
    password = None
    first_name = None
    last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
