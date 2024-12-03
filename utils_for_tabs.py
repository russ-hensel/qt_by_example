#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:44:12 2024

Utilities and now the resting place of the globals

"""
import sys
import importlib

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlDriver,
                         QSqlQuery,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
# ----QtWidgets layouts
# ---- tof
from PyQt5.QtWidgets import (QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDialog,
                             QFormLayout,
                             QGridLayout,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMessageBox,
                             QPushButton,
                             QRadioButton,
                             QTableView,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)




# ---- end imports

INDENT          = "    "   # {INDENT}
BEGIN_MARK_1    = "\n\n ------------ "
BEGIN_MARK_2    =     " ------------ "    # uft.

parameters      = None   # patche in by main program for now
display_parms   = None   # fixed on first call

main_window     = None

# for now lets get app globals here is None causeing a problem

# EXAMPLE_DB     = None
# DB_OBJECT      = None
# PARAMETERS     = None
# TEXT_EDITOR    = None

# -------------------------------------------------------
def create_class_from_strings(   module_name, class_name):
    """
    instance   = uft.create_class_from_strings(   module_name, class_name)
    this will load a class from string names
    this makes it easier to specify classes in the parameter file.

    args:  strings as named
    ret:   instance of the class

    example:
    if not ( self.parameters.ext_processing_module is None ):
        self.ext_processing =  self.create_class_from_strings( self.parameters.ext_processing_module,
                                                               self.parameters.ext_processing_class  )
    """

    a_class    = getattr( importlib.import_module(module_name), class_name )
    instance   = a_class(  )
    return instance



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

# -----------------------
def show_parameters( ):
    """
    what it says,
    """


       # display_parms   = DisplayParameters( None ) # parent = self
    dialog     = DisplayParameters( parent = main_window  )
    if dialog.exec_() == QDialog.Accepted:
        pass


class DisplayParameters( QDialog ):
    """
    dialog to display parameters

    """
    # ------------------------------------------
    def __init__(self,  parent ):
        """
        Args:


        Returns:
            None.

        """
        super().__init__( parent )
        self.parent         = parent  # parent may be a function use parent_window
        self.parent_window  = parent
        msg   = "Display Parameters "

        self.setWindowTitle( msg  )

        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 1000
        qt_height   = 500
        self.tab_help_dict   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        self._build_gui()

    # ------------------------------------------
    def _build_gui( self, ):
        """
        what it says, read?
        """
        layout              = QVBoxLayout( self )
        self.layout         = layout


        # ---- code_gen: edit_fields_for_form  -- end table entries

        # Create QTextEdit widget
        text_edit           = QTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = text_edit
        layout.addWidget( text_edit )



        parm_text      = str( parameters )

        cursor = text_edit.textCursor()
        cursor.insertText( parm_text )

        # # ---- buttons
        # self.setLayout( self.layout )
        #self.button_layout      = QVBoxLayout()
        button_layout           = layout


        a_widget                = QPushButton("OK")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.accept )
        button_layout.addWidget( a_widget )

        # # ----
        # self.buttons.setLayout( self.button_layout )

        # self.layout.addRow(self.buttons)



# ---- eof