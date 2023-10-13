#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import storage
"""Defines a BaseModel class"""


class BaseModel:
    """Represent BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialises the attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        strptime_format = "%Y-%m-%dT%H:%M:%S.5f"
                        setattr(self, key,
                                datetime.strptime(value, strptime_format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new()

    def __str__(self):
        """Return string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
            Returns a dictionary conataining all keys/values of instance

            Args:
                none

            Return:
               dictionary:  __dict__ -> Object containing all set instance
                            __class__ -> With class name as value
                            created_at/updated_at -> return in ISO format
        """
        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()

        return new_dict
