#!/usr/bin/python3
""" models amenities provided by different houses"""

from models import base_model

class Amenity(base_model.BaseModel):
    name = None
    def __init__(self, *args, **kwargs):
        super().__init__()
