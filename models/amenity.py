#!/usr/bin/python3
""" models amenities provided by different houses"""

from models import base_model


class Amenity(base_model.BaseModel):
    """ amenity model
        name - global class variable"""

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
