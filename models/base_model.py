#!/usr/bin/python3
""" Module providing a defined BaseModel class """

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel class for all the other classes """
    
    def __init__(self):
        """ Instantiate BaseModel with id, created_at, and updated_at """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Provide an informal representation of BaseModel instances """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the instance's updated_at attribute """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return dictionary of instance attributes, including class name """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
