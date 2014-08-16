# allusive
# A text editor that implements Neal Stephenson's cipher in Quicksilver
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Aug 16 11:40:55 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
A text editor that implements Neal Stephenson's cipher in Quicksilverc
"""

##########################################################################
## Imports
##########################################################################


##########################################################################
## Package constants
##########################################################################

__version__ = (0, 1, 0)

##########################################################################
## Package helpers
##########################################################################

def get_version():
    """
    Returns a string containing the version number
    """
    return ".".join("%i" % idx for idx in __version__)
