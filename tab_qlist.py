#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tab_qlist.py
"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_widgets
    qt_widgets.main( )
# --------------------

import time


# ---- imports neq qt

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QSizePolicy
from PyQt5.QtCore import QDate, Qt,  QSize
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtGui
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow, QTimeEdit
from PyQt5.QtCore import QTime

from PyQt5.QtCore  import  (
    QTimer,
    QDate,
    Qt,
    QModelIndex,
    QDateTime,
  )

# layouts
from PyQt5.QtWidgets import (
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    )

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


# widgets biger
from PyQt5.QtWidgets import (
    QGroupBox,
    QAction,
    QMenu,
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
    QDateEdit,
    QTableWidgetItem,
    QTableWidget,
    )

# sql
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlTableModel,
    QSqlQuery
    )

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDateTimeEdit
from PyQt5.QtCore import QDateTime

import inspect
import subprocess
from   subprocess import run
from   subprocess import Popen, PIPE, STDOUT
from   datetime import datetime

from   functools  import partial


import wat_inspector
import wat
import utils_for_tabs as uft
import qt_widgets
import parameters


# ---- end imports




INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header



#  --------
class QListWidgetTab( QWidget ) :
    def __init__(self):
        """
        the usual
        tab_list_widget.py
        """
        super().__init__()
        self._build_gui()

    #-----------------------------------------------
    def _build_gui(self,   ):
        """
        the usual
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout( )

        # ---- QListWidget
        widget              = QListWidget(    )
        self.list_widget_1  = widget
        widget.setGeometry( 50, 50, 200, 200 )
        layout.addWidget( widget )

        widget.itemClicked.connect( self.list_clicked )

        values    =  [ "one", "two"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )

        widget.clear()

        values    =  [ "oneish", "twoish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2
            widget.setCurrentRow(index_to_select)

        # --- buttons
        layout.addLayout( button_layout,  )

        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # --------------------
    def list_clicked( self, item ):
        """
        when the list is clicked get the text
        """
        print_func_header( "list_clicked" )

        widget        = self.list_widget_1
        row           = widget .row(item)

        # Get the text of the clicked item
        text = item.text()

        print(f"Clicked row: {row}, text: {text}")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )


        self_list_widget_1  = self.list_widget_1
        wat_inspector.go(
             msg            = "from inspect method",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof