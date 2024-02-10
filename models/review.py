#!/usr/bin/python3

"""Module for Review  class that contain all Reviewes in system"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Review  class contains Review data"""

    place_id = ""
    user_id = ""
    text = ""
