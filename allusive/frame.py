# allusive.frame
# The allusive app is made up of two frames, the editor and the viewer
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Aug 16 14:31:00 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: frame.py [] benjamin@bengfort.com $

"""
The allusive app is made up of two frames, this class implements thier
combined functionality so that they can be extended as needed.
"""

##########################################################################
## Imports
##########################################################################

import Tkinter as tk
from .colors import *

##########################################################################
## Constants
##########################################################################

DEFAULT_FRAME_CONFIG = {
    "borderwidth":0,
    "background":BG_DARK,
    "highlightthickness":0,
}

DEFAULT_TEXT_CONFIG = {
    "borderwidth":0,
    "font":"{Lucida Sans Typewriter} 14",
    "foreground":FG_LITE,
    "background":BG_DARK,
    "insertbackground":BG_CURSOR, # cursor
    "insertwidth":2,
    "selectforeground":FG_SELECT, # selection
    "selectbackground":BG_SELECT,
    "highlightthickness":0,
    "wrap":tk.WORD, # use word wrapping
    "undo":True,
}

##########################################################################
## AllusiveFrame
##########################################################################

class AllusiveFrame(tk.Frame):

    def __init__(self, master, **options):
        tk.Frame.__init__(self, master)

        # Configure the frame
        self.config(**options)

        # Set up the text widget
        self.text = tk.Text(self)
        self.text_config()
        self.text.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW+tk.SE)

    def config(self, **options):
        config = DEFAULT_FRAME_CONFIG.copy()
        config.update(options)
        tk.Frame.config(self, **config)

    def text_config(self, **options):
        config = DEFAULT_TEXT_CONFIG.copy()
        config.update(options)
        self.text.config(**config)
