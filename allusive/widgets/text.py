# allusive.widgets.text
# Text widgets for the Allusive app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Aug 17 12:19:01 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: text.py [] benjamin@bengfort.com $

"""
Text widgets for the Allusive app
"""

##########################################################################
## Imports
##########################################################################

import Tkinter as tk

##########################################################################
## Read Only Text Widget
##########################################################################

class ReadOnlyText(tk.Text):

    def __init__(self, *args, **kwargs):
        kwargs['state'] = tk.DISABLED
        tk.Text.__init__(self, *args, **kwargs)
