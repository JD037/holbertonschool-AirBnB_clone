#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for AirBnB clone.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a State instance.
        """
        super().__init__(*args, **kwargs)
