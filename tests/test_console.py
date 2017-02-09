#!/usr/bin/python3
"""
This is module test_console.
This module is a unittest for the console module.
it can be run with python -m unittest tests/test_console.py from
the parent directory
"""
import unittest
import sys
import os

# needed, import does not work, and relative path does not work either
sys.path.insert(1,'/home/vagrant/projects/AirBnB_clone')
import console

class TestConsole(unittest.TestCase):
    """
    This class is a unittest for the console module

    **Instance methods**
    """
    def test_help(self):
        """
        Tests the help command
        """
        help_prompt = console.myPrompt().do_help
        # must redirect print to something, needs a return value
        self.assertEqual(help_prompt(""), """
Documented commands (type help <topic>):
========================================
EOF  help  quit

""")

if __name__ == "__main__":
    unittest.main()
