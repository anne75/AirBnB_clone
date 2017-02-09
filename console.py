#!/usr/bin/python3
import cmd
import sys


class myPrompt(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Implements the quit command"""
        raise SystemExit

    def do_EOF(self, args):
        """Implements EOF"""
        return True

    def emptyline(self):
        """Orverrides empty line default behavior"""
        pass

    def postloop(self):
        """Prints a newline after EOF"""
        print()

if __name__ == "__main__":
    myPrompt().cmdloop()
