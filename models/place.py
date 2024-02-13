#!/usr/bin/python3
""" models place/location"""
from models import base_model


class Place(base_model.BaseModel):
    """ create a place object
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ place model init method """

        super().__init__(*args, **kwargs)
