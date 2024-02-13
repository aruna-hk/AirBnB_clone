#!/usr/bin/python3
""" models user reviews """
from models import base_model


class Review(base_model.BaseModel):
    """ user review class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Review init method"""

        super().__init__(*args, **kwargs)
