#!/usr/bin/python3
"""this module models states where houses are located"""

from models import base_model


class State(base_model.BaseModel):
    """create state object """

    name = ''

    def __init__(self, *args, **kwargs):
        """ location , State initializer"""

        super().__init__(*args, **kwargs)
