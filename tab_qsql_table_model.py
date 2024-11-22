#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:55:08 2024

tab_qsql_table_model.
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
import qt_sql_widgets

# ---- end imports



INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header





#-----------------------------------------------
class QSqlTableModelTab( QWidget ):
    """
    QSqlTableModel
        and  QTableView
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self._build_model()
        self._build_gui()

        self.select_all()

    # ------------------------------
    def _build_gui( self,   ):
        """
        What it says
        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.people_view   )

        layout.addWidget( self.phone_view    )

        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # ---- PB select_all
        widget              = QPushButton("select_all\n")
        connect_to          = self.select_all
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB get_selected_rows
        widget              = QPushButton("get_selected_rows\n")
        widget.clicked.connect( self.get_selected_rows )
        button_layout.addWidget( widget )



        # # ---- PB get_data_from_model
        # widget              = QPushButton("get_data\n_from_model")
        # connect_to          = self.get_data_from_model
        # widget.clicked.connect( connect_to )
        # button_layout.addWidget( widget )

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

    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        """
        #print_func_header( "_build_model" )
        # ---- people
        model                  = QSqlTableModel( self, uft.EXAMPLE_DB  )
        self.people_model      = model
        model.setTable('people')

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .

        model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.people_view        = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSelectionBehavior( QTableView.SelectRows )
        view.clicked.connect( self._people_view_clicked  )

        # ---- people_phones
        model                  = QSqlTableModel( self, uft.EXAMPLE_DB  )
        self.phone_model       = model
        model.setTable( 'people_phones' )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.phone_view         = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        #view.setSelectionBehavior( QTableView.SelectRows )
        #view.clicked.connect( self._view_clicked  )

            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
       #  model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

    # ------------------------
    def get_selected_rows(self, index,   ):
        """ """
        print_func_header( "get_selected_rows" )

        from PyQt5.QtWidgets import QTableView, QAbstractItemView
        from PyQt5.QtCore import Qt

        view            = self.people_view
        # Assuming `view` is your QTableView
        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            # Iterate over the selected rows
            for index in selected_indexes:
                row = index.row()  # Get the row number
                print(f"Selected row: {row = }")


    # ------------------------
    def _people_view_clicked(self, index,   ):
        """ """
        print_func_header( "_people_view_clicked" )

        view    = self.people_view
        msg     = f"_view_clicked {index} "
        print( msg )
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        print( msg )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        print( msg )

        model           = self.people_model
        people_model    = model
        no_rows         = model.rowCount()

        msg     = f"{INDENT}{model.rowCount() = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        age_ix       = 2
        age          = model.data( model.index( row_ix, age_ix ) )

        msg     = f"{INDENT}extracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # column may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}extracted data {key = }   "
        print( msg )

        msg     = f"{INDENT}phones are now displayed for for the person clicked on"
        print( msg )

        # ---- sync up second model with row clicked in first
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()


    # -----------------------
    def delete_selected_record(self):
        """
        !!What it says
        """
        print_func_header( "delete_selected_record" )


    # -----------------------
    def save(self):
        """
        !!What it says
        """
        print_func_header( "save" )


    # # ------------------------
    # def print_data(self):
    #     """ """
    #     what    = "print_data"
    #     print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    #     DB_OBJECT.query_data()

    # # ------------------------
    # def do_selections(self):
    #     """ """
    #     what    = "print_data"
    #     print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def select_all(self):
        """ """
        print_func_header( "select_all" )


        self.people_model.select()  # Load the data into the model

        self.phone_model.setFilter( "" )
        self.phone_model.select()

    # ------------------------
    def inspect(self):
        """ """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db          = parent_window.sample_db
        people_model         = self.people_model
        people_view          = self.people_view
        wat_inspector.go(
             msg            = "inspect QSqlTableModelTab",
             # inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        print_func_header( "breakpoint" )

        breakpoint()


