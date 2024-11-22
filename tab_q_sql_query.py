#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:39:09 2024
QSqlQuery
tab_q_sql_query.py
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
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header



#-----------------------------------------------
class QSqlQueryTab( QWidget ):
    """
    Yes, you can use a QSqlQueryModel to loop through all the rows of a
    database table. While QSqlQueryModel is primarily a model class for
    displaying read-only data in views like QTableView, you can
    still access the data pro grammatically by iterating through the rows and columns.

    Here’s an example of how to use QSqlQueryModel to loop through each row in the table.
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page            = self

        #layout        = QVBoxLayout( tab_page )
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout(   )

        layout.addLayout( button_layout )

        widget = QPushButton( "loop_with\n_qsqlquery" )
        widget.clicked.connect(lambda: self.loop_with_qsqlquery( ) )
        widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    #-----------------------------------------------
    def loop_with_qsqlquery( self ):
        """
        select data then loop through with a print
        """
        print_func_header( "loop_with_qsqlquery" )

        query = QSqlQuery( "SELECT name, age FROM people", uft.EXAMPLE_DB )
        # print( '!! may need query = QSqlQuery()
        #        query.exec_("SELECT name, age FROM people"  ' ) # Execute the query '
        # if not query.exec_( sql ):
        #     error = query.lastError()
        #     print(f"Error executing query: {error.text()}")
        #     print(f"Driver error: {error.driverText()}")
        #     print(f"Database error: {error.databaseText()}")

        while query.next():
            name = query.value(0)  # Get the value of the first column (name)
            age = query.value(1)   # Get the value of the second column (age)
            print(f"Name: {name}, Age: {age}")

            print( "unpack ")
            row_data = [query.value(i) for i in range(query.record().count())]
            print(row_data)

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        the_global_db   = uft.DB_OBJECT
        # parent_window = self.parent( ).parent( ).parent().parent()
        # a_db          = parent_window.sample_db
        # model         = self.people_model
        # view          = self.people_view
        wat_inspector.go(
             msg            = "inspect...",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        the usual
        """
        print_func_header( "breakpoint" )

        breakpoint()