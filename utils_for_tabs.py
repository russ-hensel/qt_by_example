#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:44:12 2024

@author: russ

seperator_tab.SeperatorTab

"""
# ---- tof
# widgets -- small
from PyQt5.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QTabWidget,
    QTextEdit,
    QWidget,
    QCheckBox,
    )

# layouts
from PyQt5.QtWidgets import (
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    )



INDENT        = "    "   # {INDENT}
BEGIN_MARK_1  = "\n\n------------ "
BEGIN_MARK_2  =  " ------------ "    # uft.



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

        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        widget  = QLabel( self.msg )
        layout.addWidget( widget )


# ------------------------
def utf_breakpointxxxx( ):
    """
    utils_for_tabs.utf_breakpoint()
    odd name because breakpoint is more or less resered
    """
    what    = "breakpoint"
    print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
    breakpoint()




# ---- eof