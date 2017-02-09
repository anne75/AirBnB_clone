#!/usr/bin/python3
"""
This is module console.py.
It is the main entry point for the command line interpreter.
"""
import cmd
import sys


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

    prompt = '(AirBnB)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """Quit program at End Of File (or ctrl+D)"""
        return True

    def emptyline(self):
        """Orverrides empty line default behavior"""
        pass

    def postloop(self):
        """Prints a newline after EOF"""
        print()

if __name__ == "__main__":
    myPrompt().cmdloop()
