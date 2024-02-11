#!/usr/bin/python3
""" models place/location"""
from models import base_model

class Place(base_model.BaseModel):
    """ create a place object """
    city_id = None # string - empty string: it will be the City.id
    user_id = None  #empty string: it will be the User.id
    name = None #string - empty string
    description = None # string - empty string
    number_rooms = None # integer - 0
    number_bathrooms = None # integer - 0
    max_guest = 0 # integer 0
    price_by_night = 0 # integer - 0
    latitude = 0 # float - 0.0
    longitude = 0.0 #float - 0.0
    amenity_ids = [] # list of string - empty list: it will be the list of Amenity.id later

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
