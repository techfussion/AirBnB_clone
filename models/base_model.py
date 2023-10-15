#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
"""Defines a BaseModel class"""


class BaseModel:
    """Represent BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialises the attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

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
