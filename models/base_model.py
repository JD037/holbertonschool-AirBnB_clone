#!/usr/bin/python3
""" Module providing a defined BaseModel class """

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ BaseModel class for all the other classes """
    
    def __init__(self, *args, **kwargs):
        """ 
        Instantiate BaseModel with id, created_at, and updated_at.
        If available, kwargs should be used for instantiation. 
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ Provide an informal representation of BaseModel instances """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the instance's updated_at attribute """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save() 

    def to_dict(self):
        """ Return dictionary of instance attributes, including class name """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
