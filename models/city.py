#!/usr/bin/python3
""" Module for City class """

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel

    Attributes:
        state_id (str): Will be the State.id
        name (str): Name of the city
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize City instance

        Args:
            *args (tuple): Non-keyworded variable length argument
            **kwargs (dict): Arbitrary keyworded variable length arguments
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
        