#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""importing everything for `HBNBCommand` class"""


class HBNBCommand(cmd.Cmd):
    """
    The `HBNBCommand` class is a command-line interface that
    allows users to interact with a process and execute commands
    such as quitting or handling the end of file signal.
    """
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

    def do_quit(self, *args):
        """`quit` command quits the process at hand"""
        return True

    def do_EOF(self, *args):
        """`EOF` is used to handle the end of file (EOF) signal."""
        print("")
        return True

    def emptyline(self):
        """
        The function "emptyline" does nothing and serves as a placeholder.
        """
        pass

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
        """`show` Usage: show <class> <id>
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
        if args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
            return
        print(models.storage.all()[args[0] + "." + args[1]])

    def do_destroy(self, args):
        """`do_destroy` Usage: destroy <class> <id>
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
        if args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = models.storage.all()[args[0] + "." + args[1]]
        try:
            if str(int(args[3])) == args[3]:
                setattr(obj, args[2], int(args[3]))
                obj.save()
                return
        except ValueError:
            try:
                if str(float(args[3])) == args[3]:
                    setattr(obj, args[2], float(args[3]))
                    obj.save()
                    return
            except ValueError:
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
                setattr(obj, args[2], (args[3]))
                obj.save()

    def default(self, line):
        """
        The function takes a line of input, splits it
        into class and function parts, and then calls
        the appropriate function based on the input.
        """
        dot_split = line.split('.')
        my_class = dot_split[0]
        if my_class in self.__classes:
            my_func = dot_split[1].replace("()", "")
            if my_func == "all":
                self.do_all(my_class)
            if my_func == "create":
                self.do_create(my_class)
            my_func = my_func.split(' ')
            i = 1
            while i < len(my_func):
                if i != len(my_func):
                    my_class += " "
                my_class += my_func[i]
                i += 1
            if my_func[0] == "show":
                self.do_show(my_class)
            if my_func[0] == "destroy":
                self.do_destroy(my_class)
            if my_func[0] == "update":
                self.do_update(my_class)
        else:
            return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
