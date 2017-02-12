#!/usr/bin/python3
"""
This is module console.py.
It is the main entry point for the command line interpreter.
"""
import cmd
import sys
from models.base_model import BaseModel


class myPrompt(cmd.Cmd):
    """
    Subclass of Cmd to create a simple command line interpreter for
    the AirBnB_clone project.

    **Class variables**
    prompt: the command prompt

    **Instance methods**
    do_quit
    do_EOF
    emptyline
    postloop
    """
    myClasses = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """Quit program at End Of File (or ctrl+D)"""
        return True

    def emptyline(self):
        """Overrides empty line default behavior"""
        pass

    def postloop(self):
        """Prints a newline after EOF"""
        print()

    def do_create(self, args):
        """ Creates a new instance of BaseModel"""
        if len(args) > 0 and args in myPrompt.myClasses:
            myStore = BaseModel()
            myStore.save()
            print(myStore.id)
        elif args == 0:
            print("** class name missing **")
        else:
            # ADD message for id as well
            print("** class doesn't exist **")
    """
    def do_show(self, args):
        if len(args) == 2 and args in myPrompt.myClasses:
           myStore = BaseModel()
           print(myStore.id)
        else
    """

if __name__ == "__main__":
    myPrompt().cmdloop()
