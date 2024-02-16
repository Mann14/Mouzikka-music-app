#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 15, 2018 06:02:58 PM +0530  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import tkinter.ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import View
    View.vp_start_gui()




