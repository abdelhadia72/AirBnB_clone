#!/usr/bin/python3

""" The console handle all commands for Hbnb"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models import storage
import models
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command for hbnb'''
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
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        '''
        all Prints all string representation of all instances
        based or not on the class name and id
        using : all or all <class name> <id>
        '''
        # all User
        parts = arg.split()
        if len(parts) < 1:
            print(storage.all())
        else:
            if parts[0] not in globals():
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    if parts[0] == key.split('.')[0]:
                        print(storage.all()[key])

    def do_update(self, args):
        '''
            Updates an instance based on the class name
            using : update <class name> <id> \
<attribute name> <attribute value>
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
                if vargs[2] in ("created_at", "updated_at", "id"):
                    print("** can't update **")
                    return
                obj = storage.all()[key]
                setattr(obj, vargs[2], vargs[3])

    def do_counter(self, arg):
        ''' count how many obj we have'''
        count = 0
        for value in storage.all():
            class_name = value.split(".")[0]
            if class_name == arg:
                count += 1
        return count

    def default(self, arg):
        '''
        handle daynamic commands
        using : <class name>.<method name>(<args>)
        '''
        try:
            names, args = arg.strip(')').split('(')
            class_name, method_name = names.split('.')
            if (method_name == "count"):
                print(self.do_counter(class_name))
            else:
                fun = f"do_{method_name}"
                method_name = getattr(self, fun, None)
                if len(args) == 0:
                    method_name(class_name)
                else:
                    args = args.replace('"', "")
                    args = args.replace(" ", "")
                    args = args.replace(",", " ")
                    args = f"{class_name} {args}"
                    method_name(args)
        except Exception:
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()


# TODO
# Check on the calss name if it exset
# Target the dict name and deal with it in the else
# User.all("38f22813-2753-4d42-b37c-57a17f1e4f88"
# , {'first_name': "John", "age": 89})
# User.update("b1cf4150-92b5-48c7-9da7-ac23b00d679a", {'first_name': "John", "age": 89})
# {'if method_name  == "update" and type(eval(args.split(",", 1)[1])) == dicfirst_name': "John", "age": 89}

    # def default(self, arg):
    #     '''
    #     handle daynamic commands
    #     using : <class name>.<method name>(<args>)
    #     '''
    #     try:
    #         names, args = arg.strip(')').split('(')
    #         class_name, method_name = names.split('.')
    #         if (method_name == "count"):
    #             print(self.do_counter(class_name))
    #         else:
    #             fun = f"do_{method_name}"
    #             method_name = getattr(self, fun, None)
    #             if len(args) == 0:
    #                 method_name(class_name)
    #             else:
    #                 if method_name  == "update" and type(eval(args.split(",", 1)[1])) == dict:
    #                     data_obj = (args.split(",", 1)[1])
    #                     key = f"{class_name}.{eval(args.split(',', 1)[0])}"
    #                     obj = storage.all()[key]
    #                     for key, value in eval(data_obj).items():
    #                         setattr(obj, key, value)
    #                     print("ELIF")
                        
    #                 else:
    #                     args = args.replace('"', "")
    #                     args = args.replace(" ", "")
    #                     args = args.replace(",", " ")
    #                     args = f"{class_name} {eval(args)}"
    #                     method_name(args)
    #                     print("ELSE")
                        
    #     except Exception:
    #         print("it's me error")
    #         return
