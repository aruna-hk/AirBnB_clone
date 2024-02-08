#!/usr/bin/python3

from models import base_model

class Review(base_model.BaseModel):
    place_id = "" #string - empty string: it will be the Place.id
    user_id = "" #string - empty string: it will be the User.id
    text = "" # string - empty string
