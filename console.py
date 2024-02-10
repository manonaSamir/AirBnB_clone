#!/usr/bin/python3

"""This module for the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models

class HBNBCommand(cmd.Cmd):
    """"command interpreter """
    intro = "welcome air-bnb project \n"
    prompt = "(hbnb) "
    app_command = ["User", "State", "City", "Amenity",
                   "Place", "Review", "BaseModel", "Count"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True
    
    def emptyline(self):
       """Do nothing when empty line is entered.\n"""
       pass
    
    def do_create(self, line):
        """create new instance"""

        if not line:
            print("** class name missing **")
        elif line not in self.app_command:
            print("** class doesn't exist **")
        else:
            obj = eval(f"{line}()")
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
       based on the class name and id"""
        
        arg = line.split(" ", 1)                
        if (len(arg) > 1  and "\"" in arg[1]):
            arg[1] = arg[1].strip('\"')
        
        if not line:
            print("** class name missing **")
            return

        elif arg[0] not in self.app_command:
            print("** class doesn't exist **")
        
        elif len(arg) == 1:
            print("** instance id missing **")

        elif arg[0]+'.'+arg[1] not in models.storage\
                ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            print(models.storage._FileStorage__objects[arg[0]+'.'+arg[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = line.split(" ", 1)
        ids = arg[1].strip('\"')
        if not line:
            print("** class name missing **")
            return

        elif arg[0] not in self.app_command:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")

        elif arg[0]+'.'+ids not in models.storage\
                ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[arg[0]+'.'+ids]
            models.storage.save()

    def do_all(self, line):
        """ Prints all string representation of all
        instances based or not on the class name."""
        arg = line.split(" ", 1)
        if arg[0] not in self.app_command:
            print("** class doesn't exist **")
        else:
            list_objs = []
            for key, obj in models.storage._FileStorage__objects.items():
                if arg[0] == key.split('.')[0]:
                    list_objs.append(str(obj))
            if len(list_objs) > 0:
                print(list_objs)

    def do_update(self, line):
        """ Updates an instance based on the class
        name and id by adding or updating attribute"""
        arg = line.split()
        # TODO Update date time
        if not line:
            print("** class name missing **")
            return
        if arg[0] not in self.app_command:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif arg[0]+'.'+arg[1] not in models.storage\
                ._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[arg[0]+'.'+arg[1]]
            if arg[2] in obj.__dict__.keys():
                try:
                    if arg[3].isdigit():
                        arg[3] = int(arg[3])
                    elif arg[3].replace('.', '', 1).isdigit():
                        arg[3] = float(arg[3])
                except AttributeError:
                    pass
                if arg[3].startswith('"'):
                    arg[3] = line.split('"')[1]
                setattr(obj, arg[2], arg[3])
            else:
                try:
                    if arg[3].isdigit():
                        arg[3] = int(arg[3])
                    elif arg[3].replace('.', '', 1).isdigit():
                        arg[3] = float(arg[3])
                except AttributeError:
                    pass
                if arg[3].startswith('"'):
                    arg[3] = line.split('"')[1]
                setattr(obj, arg[2], arg[3])
            obj = eval(f"{arg[0]}()")
            obj.save()

    def count(self, line):
        """Counts the number of a class."""
        arg = line.split()
        objects = [key for key in models.storage.all() if key.startswith(arg[0])]
        print(len(objects))

    def fun_update(self, cls_name, obj_attr):
        """ Updates an instance based on the class
        name and id by adding or updating attribute"""
        args = obj_attr.split(',')
        if "{" in args[1]:
            arg_dict = obj_attr.split("{")[1]
            arg_dict = "{" + arg_dict
            dictionary = eval(arg_dict)
            for key, val in dictionary.items():
                obj = models.storage._FileStorage__objects[cls_name +
                                                    '.'+args[0].strip('" ')]
                if key in obj.__dict__.keys():
                    try:
                        if val.isdigit():
                            val = int(val)
                        elif val.replace('.', '', 1).isdigit():
                            val = float(val)
                    except AttributeError:
                        pass
                else:
                    try:
                        if val.isdigit():
                            val = int(val)
                        elif val.replace('.', '', 1).isdigit():
                            val = float(val)
                    except AttributeError:
                        pass
                setattr(obj, key, val)
                obj = eval(f"{cls_name}()")
                obj.save()

        else:
            obj_id = args[0].strip('" ')
            if len(args[0]) < 1:
                print("** instance id missing **")
            elif cls_name+'.'+obj_id not in models.storage\
                    ._FileStorage__objects.keys():
                print("** no instance found **")
            elif len(args[1]) < 1:
                print("** attribute name missing **")
            elif len(args[2]) < 1:
                print("** value missing **")
            else:
                obj = models.storage._FileStorage__objects[cls_name+'.'+obj_id]
                if args[1].strip('" ') in obj.__dict__.keys():
                    try:
                        if args[2].isdigit():
                            args[2] = int(args[2])
                        elif args[2].replace('.', '', 1).isdigit():
                            args[2] = float(args[2])
                    except AttributeError:
                        pass
                    setattr(obj, args[1].strip('" '), args[2].strip('" '))
                else:
                    try:
                        if args[2].isdigit():
                            args[2] = int(args[2])
                        elif args[2].replace('.', '', 1).isdigit():
                            args[2] = float(args[2])
                    except AttributeError:
                        pass
                    setattr(obj, args[1].strip('" '), args[2].strip('" '))
                obj = eval(f"{cls_name}()")
                obj.save()

    def default(self, line):
        """retrieve all instances of a class by.all()"""
        args = line.split(".")

        try:
            cls_name = args[0]
            function = args[1].split("(")[0]
            obj_id = args[1].split("(")[1][0:-1]
        except IndexError:
            return cmd.Cmd.default(self, line)
        functions = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "update": self.fun_update,
            "destroy": self.do_destroy
        }
        if (cls_name not in self.app_command
                or function not in functions.keys()):
            return cmd.Cmd.default(self, line)
        else:
            if function == "update":
                self.fun_update(cls_name, obj_id)
            else:
                functions[function](f"{cls_name} {obj_id}")

        def emptyline(self):
            """Do nothing when empty line is entered."""
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
