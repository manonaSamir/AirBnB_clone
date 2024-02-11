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
import ast


class HBNBCommand(cmd.Cmd):
    """"command interpreter """
    # intro = "welcome air-bnb project \n"
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
        if (len(arg) > 1 and "\"" in arg[1]):
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
        sw = 0
        arg = line.split()
        if line == "":
            print("** class name missing **")
        elif arg[0] not in self.app_command:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            dict_objects = models.storage.all()
            for key, obj in dict_objects.items():
                if key == in_key:
                    del dict_objects[key]
                    sw = 1
                    models.storage.save()
                    models.storage.reload()
                    return
            if sw == 0:
                print("** no instance found **")      

    def do_all(self, line):
        """ Prints all string representation of all
        instances based or not on the class name."""
        arg = line.split(" ", 1)
        list_objs = []
        if arg[0] not in self.app_command and arg[0] != "":
            print("** class doesn't exist **")
        elif line == "":
            for key, obj in models.storage.all().items():
                list_objs.append(str(obj))
            if len(list_objs) > 0:
                print(list_objs)
        else:
            
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
        objects = [key for key in models.storage.all()
                   if key.startswith(arg[0])]
        print(len(objects))

    def fun_update(self, cls_name, obj_attr):
        """ Updates an instance based on the class
          name and id by adding or updating attributes """
        args = obj_attr.split(',')
        obj_id = args[0].strip('" ')
        if len(args) < 2:
            print("** attribute missing **")
        else:
            obj = models.storage._FileStorage__objects.get(
                cls_name + '.' + obj_id)
            if obj:
                if "{" in args[1]:
                    attribute_dict = ast.literal_eval(','.join(args[1:]))
                    if isinstance(attribute_dict, dict):
                        for key, value in attribute_dict.items():
                            setattr(obj, key.strip('" ')
                                    .replace("'", ""), value)
                        obj.save()
                else:
                    try:
                        obj_id = args[0].strip('" ')
                        if len(args) < 2:
                            data = args[1].split(':')
                            if data[1].isdigit():
                                data[1] = int(data[1])
                            elif data[1].replace('.', '', 1).isdigit():
                                data[1] = float(data[1])
                            setattr(obj, data[0].strip('" ')
                                    .replace("'", ""), data[1].strip('" '))
                        else:
                            if args[2].startswith('"'):
                                args[2] = args[2].split('"')[1]
                            setattr(obj, args[1], args[2])
                    except AttributeError:
                        pass
                    obj.save()
            else:
                print("** no instance found **")

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
