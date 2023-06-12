#!/usr/bin/python3
"""Contains the FileStorage class model"""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ Adds a new object to the dictionary of objects """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes the objects to the JSON file """
        serialized_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ Deserializes the JSON file to objects, if file exists """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                
            for key in objects:
                class_name = objects[key]["__class__"]
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**objects[key])
