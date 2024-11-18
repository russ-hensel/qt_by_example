#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


tab_q_sql_relational_model_2.QSqlRelationalTableModelTab_2()



"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main( )
# --------------------


# ---- imports

from platform import python_version
import inspect
import os
import subprocess
import sys
from subprocess import PIPE, STDOUT, Popen, run

#from app_global import AppGlobal
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate, QModelIndex, QSize, QSortFilterProxyModel, Qt,
                          QTimer)
# sql
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlRelation,
                         QSqlRelationalDelegate, QSqlRelationalTableModel,
                         QSqlTableModel)


from PyQt5.QtSql import QSqlRecord, QSqlField



from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
                             QButtonGroup, QCheckBox, QComboBox,
                             QDataWidgetMapper, QDateEdit, QDialog,
                             QDoubleSpinBox, QFormLayout, QGridLayout,
                             QGroupBox, QHBoxLayout, QHeaderView, QLabel,
                             QLineEdit, QListWidget, QListWidgetItem,
                             QMainWindow, QMenu, QMessageBox, QPushButton,
                             QRadioButton, QSpinBox, QStyledItemDelegate,
                             QTableView, QTableWidget, QTableWidgetItem,
                             QTabWidget, QTextEdit, QVBoxLayout, QWidget)



import sys

from functools import partial


import utils_for_tabs as uft
import wat_inspector

import parameters


INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_2
BEGIN_MARK_2  = uft.BEGIN_MARK_2

def print_func_header( what ):
        """
        what is says
        """
        #what    = "fix_me"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

#-----------------------------------------------
class QSqlRelationalTableModelTab_2( QWidget ):
    """
    for widgets joining two tables
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self._build_model()
        self._build_gui()

        self.model.select()

    # ------------------------------
    def _build_gui( self,   ):
        """
        the usual
        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.view   )

        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )


        # ---- PB select_for\n_all
        widget            = QPushButton( "select_for\n_all" )
        connect_to        = self.select_all
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB select\n_some
        widget            = QPushButton( "select\n_some" )
        connect_to        = self.select_some
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB "get_data\n_from_model"
        widget              = QPushButton( "get_data\n_from_model" )
        connect_to          = self.get_data_from_model
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB i"insert\n_record"
        widget            = QPushButton("insert\n_record")
        connect_to        = self.add_record
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB i"insert\n_record"
        widget            = QPushButton("update_db\n")
        connect_to        = self.update_db
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )


        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget            = QPushButton("breakpoint\n")
        connect_to        = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        for _1
        sql behind this should be:  old
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people
            LEFT JOIN people_phones ON people.id = people_phones.person_id

        for _2  -- turn around the primary table  most of fields come from secondary table
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people_phones
            LEFT JOIN people ON people.id = people_phones.person_id


        """
        model           = QSqlRelationalTableModel( self )
        self.model      = model

        model.setTable( "people_phones" )

        #debug_var   = self.model.fieldIndex( "person_id" )   # field name to number

        model.setRelation(
            self.model.fieldIndex( "person_id" ),  # column name in first table,

            QSqlRelation( "people", "id", "name, age")
            #             table to join to in second table
            #                      column to join on
            #                                           # columns from people phones to fetch.and display display
            #QSqlRelation("people_phones", "person_id", "phone_number, zone")

        )

        # column_index = model.fieldIndex( "age" )  # Get the column index for "name"
        # print( f"{column_index = }")
        # model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no

        # Set headers -- need to match to model
        model.setHeaderData(0, Qt.Horizontal, "c0")
        model.setHeaderData(1, Qt.Horizontal, "c1")
        model.setHeaderData(2, Qt.Horizontal, "c2")
        model.setHeaderData(3, Qt.Horizontal, "c3")
        model.setHeaderData(4, Qt.Horizontal, "c4")

        # self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        model.setEditStrategy( QSqlRelationalTableModel.OnManualSubmit )
        self.select_all()

        # ---- view
        view        = QTableView()
        self.view   = view
        view.setModel( model)

        # --- view options
        view.resizeColumnsToContents()
        view.setAlternatingRowColors(True)
        view.setSortingEnabled(True)    # is this click on header?


    # ------------------------
    def _people_view_clickedxxx(self, index,   ):
        """ """
        print_func_header( "_people_view_clickedxxx" )

        view    = self.people_view
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        print( msg )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        print( msg )

        model      = self.people_model
        people_model = model
        no_rows    = model.rowCount()

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
        key_ix       = 0 # may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}extracted data {key = }   "
        print( msg )

        # ---- sync up second model
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def add_record(self):
        """
        what it says
            we need to add to primary table here: people_phones

        for ix_row = 10 ix_col = 0  data = 1   id of smething probably person
        for ix_row = 10 ix_col = 1  data = 'Alice'
        for ix_row = 10 ix_col = 2  data = 25
        for ix_row = 10 ix_col = 3  data = '555-1234'
        for ix_row = 10 ix_col = 4  data = 'A'
        for ix_row = 10 ix_col = 5  data = None

           SELECT
               people.id,
               people.name,    ix_name    = 2
               people.age,     ix_age     = 3
               people.family_relation,
               people_phones.phone_number

                   ix_zone  = 4
                   end of table
           FROM people_phones
           LEFT JOIN people ON people.id = people_phones.person_id



        """
        print_func_header( "add_record" )

        msg             = "data for id  123  name  John Doe"
        print( msg )

        model           = self.model

        new_record      = model.record()

        """
        CREATE TABLE people_phones (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id       INTEGER,
                phone_number    TEXT,
                zone            TEXT,
                FOREIGN KEY(person_id) REFERENCES people(id) ON DELETE CASCADE
            )
        """

        # --- set values
        new_record.setValue( "id", 123)
        new_record.setValue( "name", "John Doe")
        new_record.setValue( "age", 30)
        new_record.setValue( "family_relation", "Brother")

        if model.insertRecord(-1, new_record):
            pass
            # if model.submitAll():
            #     print("Record inserted and changes committed to the database.")
            # else:
            #     print("Error committing changes:", model.lastError().text())
        else:
            print("Error inserting record:", model.lastError().text())
        pass

        print( "the database has not yet been updated -- you may want to update_db, select_all or get_data_from_model next ")

    # -----------------------
    def update_db(self):
        """
        what it says
        """
        print_func_header( "update_db" )

        model           = self.model

        if model.submitAll():
            print("Changes committed to the database.")
        else:
            print("Error committing changes:", model.lastError().text())

        print( "you may want to select_all or get_data_from_model next ")


    # ------------------------
    def select_all(self):
        """
        select with a sort
        """
        print_func_header( "select_all" )

        model        = self.model
        column_index = model.fieldIndex( "age" )  # Get the column index for "name"
        print( f"for sorting {column_index = }")
        model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no

        model.setFilter( "" )

        model.select()

    # ------------------------
    def select_some(self):
        """
        select base on some criteria, read the code for details
        """
        print_func_header( "select_some" )

        self.model.setFilter('age >  26 '   )
        self.model.select()

    # -----------------------
    def get_data_from_model(self):
        """
        What it says
            get data
            get rowcount
            can we get column count
            can we get column names
            note we also have a view
        """
        print_func_header( "select_some" )

        model           = self.model

        row_count       = model.rowCount()
        column_count    = model.columnCount()

        for ix_row in range( row_count ):
            for ix_col  in range( 6 ):   # should figure out a column count
                index     = model.index( ix_row,   ix_col   )
                data      = model.data( index )
                msg       = f"for {ix_row = } {ix_col = }  {data = }"
                print( msg )

    # ------------------------
    def do_selections(self):
        """
        not sure ... is dead?
        """
        print_func_header( "do_selections" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_self                = self
        parent_window           = self.parent( ).parent( ).parent().parent()
        a_db                    = parent_window.sample_db
        local_self_model        = self.model
        local_self_view         = self.view
        wat_inspector.go(
             msg            = "inspect for QSqlRelationalTableModelTab",
             #inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        the usual
        """
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof
