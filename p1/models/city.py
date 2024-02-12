#!/usr/bin/python3
"""this module models city where houses are loacted"""

from models import base_model


class City(base_model.BaseModel):
    """create state object """
    state_id = None
    name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
