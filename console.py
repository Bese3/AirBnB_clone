#!/usr/bin/python3

"""Defines the HBnB console."""

import re
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console program for this AirBnB clone starts here"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review",
    }

    def emptyline(self):
        """Empty line + Enter will just return the prompt without any error.
        i.e. the prompt will not execute the previous command"""
        pass

    def default(self, line):
        """
        The function takes a line of input, splits it
        into class and function parts, and then calls
        the appropriate function based on the input.
        """
        dot_split = line.split('.', maxsplit=1)
        my_class = dot_split[0]
        if my_class in self.__classes:
            my_func = dot_split[1].replace("()", "")
            if my_func == "all":
                self.do_all(my_class)
                return
            if my_func == "create":
                self.do_create(my_class)
                return
            if my_func == "count":
                self.do_count(my_class)
                return
            my_dict = long_parse(my_func)
            for i in my_dict.values():
                if type(i) is not dict:
                    for j in i:
                        my_class += " " + j
                else:
                    my_class += " " + i
            for i in my_dict.keys():
                if "show" == i:
                    self.do_show(my_class)
                if "update" == i:
                    self.do_update(my_class)
                if "destroy" == i:
                    self.do_destroy(my_class)
        else:
            return super().default(line)

    def do_quit(self, arg):
        """Exit the HBNB console: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console: EOF
        """
        print("")
        return True

    def do_create(self, args):
        """`create` creates a new instance of a class and saves it,
         printing the ID of the new instance."""
        args = args.split(" ")
        if args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """`show` Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance."""
        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            if args[0] + "." + eval(args[1]) not in\
                 models.storage.all().keys():
                print("** no instance found **")
                return
            print(models.storage.all()[args[0] + "." + eval(args[1])])
        except Exception:
            if args[0] + "." + args[1] not in models.storage.all().keys():
                print("** no instance found **")
                return
            print(models.storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, args):
        """`destroy` Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            if args[0] + "." + eval(args[1]) not in\
                 models.storage.all().keys():
                print("** no instance found **")
                return
            del models.storage.all()[args[0] + "." + eval(args[1])]
            models.storage.save()
        except Exception:
            if args[0] + "." + args[1] not in models.storage.all().keys():
                print("** no instance found **")
                return
            del models.storage.all()[args[0] + "." + args[1]]
            models.storage.save()

    def do_all(self, args):
        """`all`Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class."""

        args = args.split(" ")
        if args == ['']:
            objs = [i.__str__() for i in models.storage.all().values()]
            print(objs)
            return
        if args[0] not in self.__classes and args != ['']:
            print("** class doesn't exist **")
            return
        objs = [i.__str__() for i in models.storage.all().values() if
                i.to_dict()["__class__"] == args[0]]
        print(objs)

    def do_update(self, args):
        """`update`
        update <class name> <id> <attribute name> "<attribute value>"
        Updates current instance of a class."""
        args = args.split(" ")
        if len(args) == 1 and args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            if args[0] + "." + eval(args[1]) not in\
                 models.storage.all().keys():
                print("** no instance found **")
                return
            obj = models.storage.all()[args[0] + "." + eval(args[1])]
        except Exception:
            if args[0] + "." + args[1] not in models.storage.all().keys():
                print("** no instance found **")
                return
            obj = models.storage.all()[args[0] + "." + args[1]]
        # print(type(eval(args[2])))
        if args[2][0] == "{":
            i = 2
            my_dict = ""
            while i < len(args):
                my_dict += args[i]
                if i != len(args) - 1:
                    my_dict += " "
                i += 1
            for key, value in eval(my_dict).items():
                setattr(obj, key, value)
            obj.save()
            return
        try:
            if str(int(args[3])) == args[3]:
                setattr(obj, args[2].replace("\"", ""), int(args[3]))
                obj.save()
                return
        except (ValueError, TypeError):
            try:
                if str(float(args[3])) == args[3]:
                    setattr(obj, args[2].replace("\"", ""), float(args[3]))
                    obj.save()
                    return
            except (ValueError, TypeError):
                """handling Double Quotes in arguments"""
                if args[3][0] == "\"":
                    value = ""
                    i = 3
                    while i < len(args):
                        value += args[i].replace("\"", "")
                        if i != len(args) - 1:
                            value += " "
                        i += 1
                    args[3] = value
                setattr(obj, args[2].replace("\"", ""), (args[3]))
                obj.save()

    def do_count(self, args):
        """`count` Usage count <class_name> or <class_name>.count()
        Example: count User or User.count()"""

        args = args.split(" ")
        if args == ['']:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        BaseModel_obj = 0
        User_obj = 0
        State_obj = 0
        City_obj = 0
        Amenity_obj = 0
        Place_obj = 0
        Review_obj = 0
        for i in models.storage.all().values():
            if type(i) is BaseModel:
                BaseModel_obj += 1
            if type(i) is User:
                User_obj += 1
            if type(i) is State:
                State_obj += 1
            if type(i) is City:
                City_obj += 1
            if type(i) is Amenity:
                Amenity_obj += 1
            if type(i) is Place:
                Place_obj += 1
            if type(i) is Review:
                Review_obj += 1
        print(eval(args[0] + "_obj"))


def long_parse(args):
    """
    The function `long_parse` takes a string argument
    and parses it to create a dictionary with three
    key-value pairs.
    """
    args = args.replace(")", "")
    args = args.split("(")
    curly = re.search(r"\{(.*?)\}", args[len(args) - 1])
    if curly is None:
        my_arg = args[1].split(", ")
        args = args[0]
        id = ""
        attr = ""
        value = ""
        new_list = [id, attr, value]
        i = 0
        while i < len(my_arg):
            if my_arg[i]:
                new_list[i] = my_arg[i].replace("\"", "")
            else:
                break
            i += 1
        result = {args: new_list}
        return result
    my_arg = args[1].split(", ")
    i = 2
    while i < len(my_arg):
        my_arg[1] += ", " + my_arg[i]
        i += 1
    my_arg = [my_arg[0].replace("\"", ""), my_arg[1]]
    args = args[0]
    result = {args: my_arg}
    return result


if __name__ == '__main__':
    HBNBCommand().cmdloop()
