#!/usr/bin/python3

"""
This module for defines all common attributes/methods for other classes
"""

import datetime
import uuid
import models

class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

        else:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    time = datetime.datetime.fromisoformat(val)
                    setattr(self, key, time)
                else:
                    setattr(self, key, val)

    def __str__(self):
        """represents the class objects as a string"""
        return f"[{self.__class__.__name__}]\
       ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute
       updated_at with the current datetime """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
       all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
