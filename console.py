#!/usr/bin/env python3

""" The console """

from models.base_model import BaseModel
from models.user import User
from models.city import City 
from models.place import Place 
from models.state import State 
from models.amenity import Amenitys 
from models import storage
import models
import cmd


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to Airbnb console. type 'help' for more info."
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        '''
        Exit command to exit the program
        '''
        return True

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        using : quit
        '''
        return True
    
    # def do_create(self, arg):
    #     '''
    #     Creates a new instance of BaseModel
    #     using : creates <class name>
    #     '''
    #     if not arg:
    #         print("** class name missing **")
    #     # elif  arg != BaseModel.__name__:
    #     elif arg not in globals():
    #         print("** class doesn't exist **")
    #     else:
    #         new_instance = BaseModel()
    #         new_instance.save()
    #         print(new_instance.id)
    
    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel
        using : creates <class name>
        '''
        if not arg:
            print("** class name missing **")
        # elif  arg != BaseModel.__name__:
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)
        
    
    def do_show(self, arg):
        '''
        Prints the string representation of an 
        instance based on the class name and id
        using : show <class name> <id>
        '''
        
        if len(arg) == 0:
            print("** class name missing **")
        else:
            parts = arg.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        using : destroy <class name> <id>
        '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            parts = arg.split()
            if parts[0] not in globals():
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                class_name = parts[0]
                obj_id = parts[1]
                key = f"{class_name}.{obj_id}"
                if key in storage.all():
                    del storage.all()[key]
                else:
                    print("** no instance found **")
    
    def do_all(self, arg):
        '''
        all Prints all string representation of all instances
        based or not on the class name and id
        using : all or all <class name> <id>
        '''
        parts = arg.split()
        if len(parts) < 1:
            print(storage.all())
        else:
            if parts[0] not in globals():
                print("** class doesn't exist **")
            else:
                #* add the class that you want to print 
                print(storage.all())
        
    def do_update(self, args):
        '''
            Updates an instance based on the class name
            using : update <class name> <id> <attribute name> "<attribute value>
        '''
        vargs = args.split()
        
        if len(vargs) < 1:
            print("** class name missing **")
        elif vargs[0] not in globals():
            print("** class doesn't exist **")
        elif len(vargs) < 2:
            print("** instance id missing **")
        elif f"{vargs[0]}.{vargs[1]}" not in storage.all():
            print("** no instance found **")
        elif len(vargs) < 3:
            print("** attribute name missing **")
        elif len(vargs) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(vargs[0], vargs[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, vargs[2], vargs[3])

    # def do_ma(self, args):
    #     print("Globals :",globals())
    #     print("--------")
    #     print("Subclasses :", BaseModel.__subclasses__())
    #     print("--------")
    #     print("Name :",BaseModel.__name__)
    #     print("--------")
    #     print("Modle :", models.__dict__)
#$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

if __name__ == "__main__":
    HBNBCommand().cmdloop()