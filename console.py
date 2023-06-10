#!/usr/bin/env python3
"""Console module"""
import cmd
from models import storage
from models.base_model import BaseModel
# import all our models here

class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Overwrite the default emptyline method"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                new_model = eval(arg)()
                new_model.save()
                print(new_model.id)
            except NameError:
                print("** class doesn't exist **")
    
    # ... define do_show, do_destroy, do_all, do_update following similar structure

if __name__ == '__main__':
    HBNBCommand().cmdloop()
