#!/usr/bin/python3
"""
This is module test_console.
This module is a unittest for the console module.
it can be run with python -m unittest tests/test_console.py from
the parent directory
"""
import unittest
import sys
from unittest.mock import patch
from io import StringIO

# needed, import does not work, and relative path neither does
# sys.path.insert(1,'/home/vagrant/projects/AirBnB_clone')
import console


class TestConsole(unittest.TestCase):
    """
    This class is a unittest for the console module

    **Instance methods**
    """
    def setUp(self):
        """Redirects stdin and stdout"""
        self.command = console.HBNBCommand()

    def test_help(self):
        """
        Tests the help command
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.command.onecmd("help"))
            # must redirect print to something, needs a return value
            self.assertEqual("""\nDocumented commands (
                type help <topic>):\n
                    ========================================
                        \nEOF  help  quit\n""",
                             fake_out.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
