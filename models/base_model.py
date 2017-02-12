#!/usr/bin/python3
"""
This is module base_model
This module defines one class
"""
from datetime import datetime
import uuid
import json
from models import storage


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Creates a BaseModel object
        Arguments:
            if any should be a dictionary containing following keys
            id: a string, unique user id
            created_at: a datetime object
            updated_at: a datetime object
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime(*(kwargs['created_at']))
            self.updated_at = datetime(*(kwargs['updated_at']))
        elif args:
            if len(args) != 3:
                pass
            self.id = args[0]
            self.created_at = datetime(*(args[1]))
            self.updated_at = datetime(*(args[2]))
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())
            storage.new(self)

    def __str__(self):
        """fancy printing"""
        return ("[{}] ({}) {}".format(
                            self.__class__.__name__, self.id, self.__dict__))

    def __setattr__(self, name, value):
        """
        Forbids update of instance variables

        Arguments:
        name: name
        value: value
        """
        if hasattr(self, name):
            return
        self.__dict__[name] = value

    def save(self):
        """Updates the object and saves it to file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """Prepares serialization"""
        self.__dict__.update({"__class__": "BaseModel"})
        return self.__dict__
