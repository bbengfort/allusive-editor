# tests
# Testing for the allusive module
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Aug 16 11:41:52 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the allusive module
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Test Cases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Tests a simple world fact by asserting that 10*10 is 100.
        """
        self.assertEqual(2**3, 8)

    def test_import(self):
        """
        Can import allusive
        """
        try:
            import allusive
        except ImportError:
            self.fail("Unable to import the allusive module!")

    def test_version(self):
        """
        Assert that the version is sane
        """
        import allusive
        self.assertEqual("0.1.0", allusive.get_version())
