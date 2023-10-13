#!/usr/bin/python3
"""This is the BaseModel python file"""

from datetime import datetime
import uuid

class BaseModel:
    """A class that defines all common attributes/methods for other classes"""
    
    def __init__(self,*args,**kwargs):
        """Initialises the attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current timestamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the BaseModel instance to a dictionary for serialization.

        Returns:
        A dictionary containing the instance attributes in a serialized format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
