#!/usr/bin/env python3

import json
import uuid
# from models.base_model import BaseModel
from datetime import datetime

class FileStorage():
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        ''' Return __object'''
        return FileStorage.__objects
    
    def new(self, obj):
        ''' sets the key'''
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj
        #! remove me
        # print("key : ",key,"\nvalue : ", obj)
    
    
    def save(self):
        json_object = {}
        
        for key in FileStorage.__objects:
            # print("The key is: ",key)
            # print("info", FileStorage.__objects[key].to_dict())
            json_object[key] = FileStorage.__objects[key].to_dict()
            # att

        
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)
    
    # def reload(self):
    #     print("Okay I'm running -00")
    #     """Deserialize the JSON file __file_path to __objects, if it exists."""
    #     try:
    #         print("Okay I'm running 00")
    #         with open(FileStorage.__file_path, 'r') as f:
    #             dict_obj = json.load(f)
    #             # load data to dicts
    #             for value in dict_obj.values():
    #                 # value is {}
    #                 print("Okay I'm running 01") 
    #                 print("VALUE IS IS IS ",value)
    #                 class_name = value["__class__"]
    #                 # print("I'M THAT CLASS ",class_name)
    #                 del value["__class__"]  
    #                 # print("my type is : ", type(eval(class_name(**value))))
    #                 print("my type is : ", type(value))
    #                 # FileStorage.new(eval(class_name(**value)))
    #                 print("Okay I'm running 02")
    #                 # print("EV_CLASS_NAME",eval(class_name)(**value))
    #     except FileNotFoundError:
    #         return
    
    def reload(self):
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



    
# # #! remove me 
# class Home():
#     def __init__(self, one, two):
#         self.one = one,
#         self.two = two,
#         self.id = "234klj"

#     def __str__(self):
#         return f"{self.one}, {self.two} we are done"
    
    
#     def __init__(self, *args, **kwargs):
#         '''Initializes instances'''
#         if kwargs:
#             for key, value in kwargs.items():
#                 if key != '__class__':
#                     if key in ('created_at', 'updated_at'):
#                         value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
#                     setattr(self, key, value)
#             self.id = kwargs.get('id')
#         else:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
    
#     def __str__(self):
#         '''string representation of the object'''
#         return ("[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__))
        
#     def save(self):
#         '''Updates the "updated_at" attribute with the current time'''
#         self.updated_at = datetime.now()
        
#     def to_dict(self):
#         '''Converts the object's attributes to a dictionary'''
#         dict = self.__dict__.copy()
#         dict['__class__'] = self.__class__.__name__
#         dict['created_at'] = self.created_at.isoformat()
#         dict['updated_at'] = self.updated_at.isoformat()
#         return (dict)
        

#     def save(self):
#         """ updates with the current datetime """
#         self.updated_at = datetime.now()
#         # models.storage.save()



# dd = FileStorage()
# ss = Home("wa7d", "joj")
# print(dd.new(ss))
# print(dd.save())
# print(dd.reload())
# print("+++++++++++++++++++++90")