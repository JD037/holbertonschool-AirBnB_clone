#!/usr/bin/python3
""" Module for Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel

    Attributes:
        name (str): Name of the amenity. It's an empty string by default.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity instance

        Args:
            *args (tuple): Non-keyworded variable length argument
            **kwargs (dict): Arbitrary keyworded variable length arguments
        """
        super().__init__(*args, **kwargs)
