# allusive.app
# Main entry point for the allusive-editor
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Aug 16 12:29:49 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
Main entry point for the allusive-editor
"""

##########################################################################
## Imports
##########################################################################

import Tkinter as tk
from .colors import *
from .frame import *

##########################################################################
## Constants
##########################################################################

TITLE = "Allusive"

##########################################################################
## App
##########################################################################

class AllusiveApp(tk.Tk, object):

    def __init__(self):
        tk.Tk.__init__(self)
        self.config(background=BG_DARK)
        self.wm_state("zoomed")
        self.title(TITLE)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        ## Initialize the widgets
        self.editor = AllusiveEditor(self)
        self.viewer = AllusiveViewer(self)

        self.editor.grid(row=0, column=0, sticky=tk.NW+tk.SE)
        self.viewer.grid(row=0, column=1, sticky=tk.NW+tk.SE)

    def run(self):
        """
        Run the primary frame (and any other frames)
        """
        tk.mainloop()

class AllusiveEditor(AllusiveFrame):
    pass

class AllusiveViewer(AllusiveFrame):

    def __init__(self, master, **options):
        options['background'] = TWILIGHT
        AllusiveFrame.__init__(self, master, **options)
        self.text_config(background=TWILIGHT)
