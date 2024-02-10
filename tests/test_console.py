#!/usr/bin/python3
"""Unittests for testing console output."""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models

def test_create(self):
        """Tests the create command."""
        old_num = len(models.storage.all())
        tests = ["", "Model"]
        outputs = ["** class name missing **\n",
                   "** class doesn't exist **\n"]
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            new_num = len(models.storage.all())
            self.assertEqual(new_num, old_num + 1)
            for i in range(2):
                output.truncate(0)
                output.seek(0)
                HBNBCommand().onecmd(f"create {tests[i]}")
                out_val = output.getvalue()
                self.assertEqual(out_val, outputs[i])
