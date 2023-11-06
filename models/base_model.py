#!/usr/bin/env python

import uuid
from datetime import datetime


class BaseModel():
    def __init__(self):
        '''Initializes instances'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        '''string representation of the object'''
        return ("[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__))
        
    def save(self):
        '''Updates the "updated_at" attribute with the current time'''
        self.updated_at = datetime.now()
        
    def to_dict(self):
        '''Converts the object's attributes to a dictionary'''
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return (dict)
        
