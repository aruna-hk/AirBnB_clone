#!/usr/bin/python3
"""this module models states where houses are located"""

from models import base_model

class State(base_model.BaseModel):
    """create state object """

    name = None

    def __init__(self, *args, **kwargs):
        super().__init__()
