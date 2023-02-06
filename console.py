#!/usr/bin/python3

"""Module console.py
The program starts here. Run this script to interact with the program"""

import cmd
import models


# noinspection PyMethodMayBeStatic
class HBNBCommand(cmd.Cmd):
    """The console program for this AirBnB clone starts here"""
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """Empty line + Enter will just return the prompt without any error.
        i.e. the prompt will not execute the previous command"""
        return False

    def do_quit(self, arg):
        """Exit the HBNB console:  quit"""
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console:  EOF"""
        return True

    def postloop(self):
        """Print a new line when program exits"""
        print()

    def do_create(self, arg):
        """Create a new instance with the argument as the class name
        Create a new instance of BaseModel: create BaseModel"""
        arg = [s for s in arg.split()]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            bm = self.storage.all_models.get(arg[0])()
            bm.save()
            print(bm.to_dict().get("id"))

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the classname and id
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-1234-1234"""
        arg = [s for s in arg.split()]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[1] not in [x.to_dict()["id"] for x in
                            self.storage.all().values() if
                            x.to_dict()["__class__"] == arg[0]]:
            print("** no instance found **")
        else:
            print([i for i in self.storage.all().values() if
                   arg[1] == i.to_dict()["id"]][0])

    def do_destroy(self, arg):
        """Deletes the object with the matching id
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 121212"""
        arg = [s for s in arg.split()]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[1] not in [x.to_dict()["id"] for x in
                            self.storage.all().values() if
                            x.to_dict()["__class__"] == arg[0]]:
            print("** no instance found **")
        else:
            self.storage.destroy(arg[1])

    def do_all(self, arg):
        """Prints all string representation of all instances based on or not
        on the class name
        Usage: all <class_name>
               all
        Example: all BaseModel"""
        arg = [s for s in arg.split()]

        if arg:
            if arg[0] not in self.storage.all_models.keys():
                print("** class doesn't exist **")
                return False
            else:
                #  Put all objects with matching class names in all_objs
                all_objs = [x.__str__() for x in self.storage.all().values() if
                            x.to_dict()["__class__"] == arg[0]]
        else:
            #  Put all objects in the file storage in all_objs since no
            #  class specifier was issued
            all_objs = [x.__str__() for x in self.storage.all().values()]

        print(all_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute, and saves it to the file storage (currently the
        JSON file
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        Example: update BaseModel 128vfb43 email "anderson@mail.com" """
        self.storage.reload()
        arg = [s for s in arg.split()]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[1] not in [x.to_dict()["id"] for x in
                            self.storage.all().values() if
                            x.to_dict()["__class__"] == arg[0]]:
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            #  Get the object to update by matching the class name and the
            #  id arguments using list comprehension
            obj_to_update = [x for x in list(self.storage.all().values()) if
                             x.to_dict()["__class__"] == arg[0] and
                             x.to_dict()["id"] == arg[1]][0]

            #  Check if the <attribute_value> is an int. If it throws a
            #  ValueError exception, it's not an int; it's a string or a float
            try:
                if str(int(arg[3])) == arg[3]:
                    setattr(obj_to_update, arg[2], int(arg[3]))
                    obj_to_update.save()
            except ValueError:
                #  Check if arg[3] (attribute_value) is a float. If it's
                #  not, it'll throw a ValueError.
                try:
                    if str(float(arg[3])) == arg[3]:
                        setattr(obj_to_update, arg[2], float(arg[3]))
                        obj_to_update.save()
                except ValueError:
                    #  arg[3] (attribute_value) is neither a float nor an
                    #  int; it must be a string hence add the attribute as a
                    #  string. Strip quotations if it has any
                    setattr(obj_to_update, arg[2],
                            str(arg[3]).strip('\"').strip('\''))
                    obj_to_update.save()

    def default(self, line):
        """For more sophisticated commands"""
        line_split = line.split('.')
        class_name = line_split[0]
        if class_name in self.storage.all_models.keys():
            function = line_split[1].split('(')[0]
            if function == "all":
                self.do_all(class_name)
            elif function == "count":
                print(len([x for x in self.storage.all().values() if
                           x.to_dict()["__class__"] == class_name]))
            elif function == "show":
                self.do_show(class_name + " " +
                             line_split[1].split('(')[1].split(')')[
                                 0].strip("\"").strip("\'"))
            elif function == "destroy":
                self.do_destroy(class_name + " " +
                                line_split[1].split('(')[1].split(')')[
                                 0].strip("\"").strip("\'"))
            elif function == "update":
                dict_update = line_split[1][line_split[1].find('{'):
                                            line_split[1].find('}') + 1]
                obj_id = line_split[1].split('(')[1].split(",")[0].\
                    strip("\"").strip("\'")
                if dict_update and dict_update[0] == '{' and dict_update[-1]\
                        == '}':
                    dict_update = eval(dict_update)
                    for key, value in dict_update.items():
                        self.do_update(class_name + " " + obj_id + " " + key
                                       + " " + str(value))
                    return False
                self.do_update(class_name + " " + obj_id + " " +
                               line_split[1].split(',')[1].
                               strip(' ').strip("\"").strip("\'") + " " +
                               line_split[1].split('(')[1].split(',')[2].
                               strip(')').strip(' '))
        else:
            cmd.Cmd.default()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
