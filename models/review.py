#!/usr/bin/python3
from models.base_model import BaseModel
""" A Review class that inherits from BaseModel"""


class Review(BaseModel):
    """Representation of Review class"""

    place_id = ""
    user_id = ""
    text = ""
