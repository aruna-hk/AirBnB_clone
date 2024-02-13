#!/usr/bin/python3
""" this module define a user"""

from models import base_model


class User(base_model.BaseModel):
    """ class user, defines a user """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ creat user, init method """

        super().__init__(*args, **kwargs)
