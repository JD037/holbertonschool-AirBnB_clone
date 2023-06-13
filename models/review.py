#!/usr/bin/python3
""" Module for Review class """

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel

    Attributes:
        place_id (str): Will be the Place.id
        user_id (str): Will be the User.id
        text (str): Review text
    """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize Review instance

        Args:
            *args (tuple): Non-keyworded variable length argument
            **kwargs (dict): Arbitrary keyworded variable length arguments
        """
        super().__init__(*args, **kwargs)
