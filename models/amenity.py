#!/usr/bin/python3

"""Module for Amenity class that contain all Amenities in system"""

from models.base_model import BaseModel


class Amenity (BaseModel):
    """Amenity  class contains Amenity data"""

    name: str = ""
