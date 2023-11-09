#!/usr/bin/env python3

"""This module implements the FileStorage class"""

import json
import uuid
# from models.base_model import BaseModel
from datetime import datetime

class FileStorage():
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Adds a new object to the dictionary""" 
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serializes objects and saves them to a JSON file"""
        json_object = {}
        
        for key in FileStorage.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserializes objects from a JSON file and loads them into the dictionary"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():

                    class_name = value["__class__"]
                    if class_name in globals():
                        obj_class = globals()[class_name]
                        del value["__class__"]
                        obj = obj_class(**value)
                        FileStorage.__objects[key] = obj
                    else:
                        from models.base_model import BaseModel
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
