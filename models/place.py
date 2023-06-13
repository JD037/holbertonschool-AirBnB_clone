#!/usr/bin/python3
""" Module for Place class """

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class inherits from BaseModel

    Attributes:
        city_id (str): Will be the City.id
        user_id (str): Will be the User.id
        name (str): Name of the place
        description (str): Description of the place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum guests
        price_by_night (int): Price by night
        latitude (float): The latitude
        longitude (float): The longitude
        amenity_ids (list of str): Will be the list of Amenity.id later
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        """
        Initialize Place instance

        Args:
            *args (tuple): Non-keyworded variable length argument
            **kwargs (dict): Arbitrary keyworded variable length arguments
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        