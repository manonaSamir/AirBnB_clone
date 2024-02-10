#!/usr/bin/python3

"""This module convert the dictionary representation to a JSON string"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns list of data."""
        return FileStorage.__objects

    def new(self, obj):
        """create new object dict."""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                obj_file = json.loads(data)
            for key, val in obj_file.items():
                FileStorage.__objects[key] =\
                    eval(f"{key.split('.')[0]}(**obj_file[key])")
        except FileNotFoundError:
            pass
