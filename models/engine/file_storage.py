#!/usr/bin/python3
"""
Contains the FileStorage class model


"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    # Add a class dictionary to map class names to classes
    __class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for k, v in objs.items():
                cls = getattr(models, v['__class__'])
                self.new(cls(**v))
        except FileNotFoundError:
            pass
