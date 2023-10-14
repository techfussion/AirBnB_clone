#!/usr/bin/python3
"""The user class that inherits from the basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class that manages the details of the user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
