#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:44:12 2024



"""
# ---- tof
from PyQt5.QtWidgets import (QButtonGroup, QCheckBox, QComboBox, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QListWidget,
                             QListWidgetItem, QMessageBox, QPushButton,
                             QRadioButton, QTabWidget, QTextEdit, QVBoxLayout,
                             QWidget)

from PyQt5.QtGui import QColor, QPalette

INDENT        = "    "   # {INDENT}
BEGIN_MARK_1  = "\n\n ------------ "
BEGIN_MARK_2  =     " ------------ "    # uft.


# for now lets get app globals here

EXAMPLE_DB     = None
DB_OBJECT      = None
PARAMETERS     = None
TEXT_EDITOR    = None




def print_func_header( what ):
        """
        what it says
        """
        #what    = "fix_me"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

#-----------------------------------------------
class SeperatorTab( QWidget ):
    """
    utils_for_tabs.py
    """
    def __init__(self, msg = None ):
        """
        """
        super().__init__( )
        if msg is None:
            msg         = "This tab indicates the status of the tabs to the right --->"
            self.msg    = msg
        self._build_gui()

    # ------------------------------
    def _build_gui( self,   ):
        """
        the usual
        """
        tab_page        = self

        layout          = QVBoxLayout( tab_page )
        self.layout     = layout

        widget  = QLabel( self.msg )
        layout.addWidget( widget )

# --------------------------
class ColoredFiller(QWidget):
    """
    M Fitzpatrick's book,  is source
    ColoredFiller('red')
    colored so you can see it, used as a filler object
    """
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor( QPalette.Window, QColor(color))
        self.setPalette(palette)



# ---- eof