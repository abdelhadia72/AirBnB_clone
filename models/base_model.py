#!/usr/bin/env python3
''' Base module class'''

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        '''Initializes instances'''
        sformat = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, sformat)
                    setattr(self, key, value)
            self.id = kwargs.get('id')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''string representation of the object'''
        class_name = self.__class__.__name__
        dicts = self.__dict__
        id = self.id
        return ("[{}] ({}) ({})".format(class_name, id, dicts))

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

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
        storage.save()
