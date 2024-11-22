#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:10:44 2024


tab_qsql_database.
"""


# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main()
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
    QHeaderView,
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
import qt_table_model


# ---- end imports





INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2


print_func_header =  uft.print_func_header


#-----------------------------------------------
class QSqlDatabaseTab( QWidget ):
    """
    for the basic database object
    SampleDB()     QSqlDatabase    query
    """
    def __init__(self, ):
        """
        the usual
        """
        super().__init__( )

        self.build_tab()

    #-----------------------------------------------
    def build_tab( self, ):
        """
        what it says
        """
        self.table_model_is_hidden  = False

        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # ---- PB rebuild_db
        widget              = QPushButton( "rebuild_db\n ")
        self.button_ex_1    = widget
        widget.clicked.connect( self.rebuild_db )

        button_layout.addWidget( widget )

        # ---- PB print_db
        widget              = QPushButton("print_db\n ")
        connect_to          = self.print_db
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        connect_to        = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    # ------------------------
    def print_db(self):
        """ """
        print_func_header( "print_db" )

        uft.DB_OBJECT.query_print_people()
        uft.DB_OBJECT.query_print_phone()
        uft.DB_OBJECT.query_print_people_phone()

    # ------------------------
    def rebuild_db(self):
        """ """
        print_func_header( "rebuild_db" )

        uft.DB_OBJECT.reset()

    # ------------------------
    def inspect(self):
        """ """
        print_func_header( "inspect" )
        # make some locals for inspection
        the_global_db    = uft.DB_OBJECT
        # parent_window = self.parent( ).parent( ).parent().parent()
        # a_db          = parent_window.sample_db
        # model         = self.people_model
        # view          = self.people_view
        wat_inspector.go(
             msg            = "see the_global_db",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """ """
        print_func_header( "breakpoint" )

        breakpoint()

# ---- eof
