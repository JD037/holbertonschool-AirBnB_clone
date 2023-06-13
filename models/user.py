#!/usr/bin/python3
"""
This module defines the User class.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class for AirBnB clone.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
