#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models
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
        try:
            if args == ['']:
                raise SyntaxError
            if args[0] not in self.__classes:
                raise NameError
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

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
        """`all`Usage: all or all <class>
        Display string representations of all instances of a given class."""

        args = args.split(" ")
        if args == ['']:
            for i in models.storage.all().values():
                print(i)
            return
        if args[0] not in self.__classes and args != ['']:
            print("** class doesn't exist **")
            return
        for i in models.storage.all().keys():
            if args[0] in i:
                print(models.storage.all()[i])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
