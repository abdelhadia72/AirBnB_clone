#!/usr/bin/python3
"""Unit tests for the console command interpreter"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the console command interpreter"""

    def setUp(self):
        """Set up testing environment"""
        self.cli = HBNBCommand()

    def test_do_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_quit(None))

    def test_do_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_EOF(None))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.cli.emptyline())

    def test_do_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_create("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_show("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_destroy("")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_do_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.do_update("")
            self.assertEqual("** class name missing **\n", f.getvalue())

if __name__ == '__main__':
    unittest.main()