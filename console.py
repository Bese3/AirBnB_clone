#!/usr/bin/python3
import cmd
"""importing everything for `HBNBCommand` class"""


class HBNBCommand(cmd.Cmd):
    """
    The `HBNBCommand` class is a command-line interface that
    allows users to interact with a process and execute commands
    such as quitting or handling the end of file signal.
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
