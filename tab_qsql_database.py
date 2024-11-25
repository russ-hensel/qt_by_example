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


import inspect
import os
import sqlite3 as lite
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QPalette, QTextCursor, QTextDocument
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
# widgets biger
# widgets -- small
# layouts
from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDateTimeEdit,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QHeaderView,
                             QLabel,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QPushButton,
                             QRadioButton,
                             QSizePolicy,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QTimeEdit,
                             QVBoxLayout,
                             QWidget)

import parameters
import qt_table_model
import qt_widgets
import utils_for_tabs as uft
import wat_inspector

# ---- imports neq qt














# ---- end imports



INDENT          = uft.INDENT
BEGIN_MARK_1    = uft.BEGIN_MARK_1
BEGIN_MARK_2    = uft.BEGIN_MARK_2


print_func_header =  uft.print_func_header
parameters        = uft.parameters

# -----------------------------
def delete_db_file( file_name ):
    """
    will delete any file, but intended for db file
    """
    exists    = str( os.path.isfile( file_name ) )
    print( f"{file_name} exists {exists}" )

    if exists:
        try:
            os.remove( file_name )   # error if file not found
            print(f"removed {file_name} "  )

        except OSError as error:
            print( error )
            print( f"os.remove threw error on file {file_name}")

    else:
        print( f"file already gone  {file_name}                ")


# -------------------------------------
class SampleDB():
    """
    this will create an instance of SampleDB and set up two module Globals
    """
    #-------------------
    def __init__( self ):
        """
        The usual
        """
        self.db    = None
        self.reset()

    #------------
    def reset( self, ):
        """
        Reset and rebuild the db
        """
        self.create_connection()
        self.create_populate_tables()

    #------------
    def create_connection( self, ):
        """
        Create a SQLite database connection.
        """
        if self.db is not None:
            self.db.close()
            self.db    = None  # or delete?

        if uft.DB_FILE    !=  ':memory:':
            # delete for a fresh start
            pass
            delete_db_file( uft.DB_FILE )

        db              = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName( uft.DB_FILE )
        self.db         = db
        uft.EXAMPLE_DB  = db   # for simple module access
        uft.DB_OBJECT   = self

        debug_item      = uft.DB_OBJECT

        if not db.open():
            print("SampleDB Error: Unable to establish a database connection.")
            return False
        return True

    # ---------------------------
    def create_populate_tables( self, ):
        """
        Create  tables.and populate with a bit of data
        """
        what    = "create_populate_tables"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        self.create_people_table()
        self.populate_people_table()

        self.create_people_phones_table()
        self.populate_people_phones_table()

        self.create_book_club_table()
        self.populate_book_club_table()

    # ---------------------------
    def create_people_table( self, ):
        """
        Create people and people_phones tables
        ."""
        what    = "create_people_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query   = QSqlQuery( self.db )

        sql     = """
            CREATE TABLE people (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                age             INTEGER,
                family_relation TEXT
            )
        """

        query.exec_( sql )

    #------------
    def populate_people_table( self, ):
        """
        Populate the people table with sample data.
        """
        print_func_header( "populate_people_table" )

        if False:
            # a bit of straight sql lite -- this does not work for in memory?
            sql_con    = lite.connect( uft.DB_FILE )
            #conn       = sqlite3.connect("example.db")
            cursor     = sql_con.cursor()
            # Insert a row with a specific starting ID
            cursor.execute("INSERT INTO people (id, name) VALUES (?, ?)", (1000, "Initial Entry"))
            # cursor.commit()
            sql_con.commit()

            print( "people table initialized to starting id of 1000")

        if True:

            query       = QSqlQuery( self.db )
            sql  =   """INSERT INTO people (
                    id,
                    name,
                    age,
                    family_relation )
                VALUES ( 1000, "initial", 0, 0 )
            """
            query.prepare( sql )
            query.exec_()

        query       = QSqlQuery( self.db )

        # you can comment out some data if you wish
        table_data = [
            ("Alice",   25,   "Aunt"      ),
            ("Bob",     30,   "Father"    ),
            ("Charlie", 35,   "Daughter"  ),
            # ("David",   40,   "Daughter2" ),
            # ("James",   28,   "Aunt"      ),
            # ("Jim",     28,   "Son"       ),
            # ("Judy",    28,   "Sun"       ),
            # ("Jo",      29,   "God"       ),
        ]

        sql  =   """INSERT INTO people (
                name,
                age,
                family_relation )
            VALUES ( ?,?, ? )
        """

        for name, age, family_relation in table_data:
            # this only one way to bind
            query.prepare( sql )
            query.addBindValue(name)
            query.addBindValue(age)
            query.addBindValue(family_relation)
            query.exec_()

    # ---------------------------
    def create_people_phones_table( self, ):
        """
        Create people_phones table.
        """
        print_func_header( "create_people_phones_table" )

        query = QSqlQuery( self.db )

        sql   = """
            CREATE TABLE people_phones (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id       INTEGER,
                phone_number    TEXT,
                zone            TEXT,
                FOREIGN KEY(person_id) REFERENCES people(id) ON DELETE CASCADE
            )
        """
        query.exec( sql )

    #------------
    def populate_people_phones_table( self, ):
        """
        Populate the people_phones table.
        """
        print_func_header( "populate_people_phones_table" )

        query = QSqlQuery( self.db )

        table_data = [
            (1001, "555-1234", "A"), (1001, "555-5678", "B"), (1001, "555-8765", "C"),
            (1002, "555-4321", "A"), (1002, "555-8765", "B"), (1002, "555-3456", "C"),
            # (1003, "555-9876", "A"), (1003, "555-1111", "B"), (1003, "555-2222", "C"),
            # (1004, "555-3333", "A"), (1004, "555-4444", "B"), (1004, "555-5555", "C"),
            # (1005, "555-6666", "A"), (1005, "555-7777", "B"), (1005, "555-8888", "C"),
            # (1005, "555-9999", "A"), (1005, "555-0000", "B"), (1005, "555-1235", "C"),
            # (2, "555-2345", "A"),    (1, "555-3456", "B"),
        ]

        sql   = """INSERT INTO people_phones (
                      person_id,
                      phone_number,
                      zone )
                     VALUES ( ?, ?, ? )
        """

        # this  is the positional style with bind values
        for person_id, phone_number, zone in table_data:
            query.prepare( sql )
            # bind value for each ?
            query.addBindValue( person_id )
            query.addBindValue( phone_number)
            query.addBindValue( zone )
            query.exec_()

    #------------
    def create_book_club_table( self, ):
        """
        Book Clubs that people can belong to
        a many to many relationship based on people and book_club
        """
        what    = "create_book_club_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query   = QSqlQuery( self.db )

        sql     = """
            CREATE TABLE book_club (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                frequency       TEXT
            ) """

        query.exec_( sql )

    #------------
    def populate_book_club_table( self, ):
        """
        Populate the book_club table
        """
        what    = "populate_book_club_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query = QSqlQuery( self.db )

        table_data = [
            ("ScinectFiction",      "weekly"    ),
            ("Romance",             "weekly"    ),
            ("Westerns",            "monthly"   ),
            ("Biography",           "daily"     ),
        ]

        for name, frequency in table_data:
            # this only one way to bind
            sql     = """INSERT INTO book_club (
                name,
                frequency  )
                VALUES (?, ? )
            """

            query.prepare( sql )
            query.addBindValue( name )
            query.addBindValue( frequency )

            query.exec_()

    #------------
    def create_people_book_club_table( self, ):
        """
        Create  table -- what it says
        """
        what    = "create_people_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query = QSqlQuery( self.db )

        sql    = """
            CREATE TABLE people_book_club (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                people_id       INTEGER,
                book_club_id    INTEGER
              ) """

        query.exec_( sql )

    #------------
    def populate_people_book_club_data( self, ):
        """
        what it says
        """
        query = QSqlQuery( self.db )

        table_data = [
            ("Alice",   25,   "Aunt"      ),
            ("Bob",     30,   "Father"    ),
            ("Charlie", 35,   "Daughter"  ),
            ("David",   40,   "Daughter2" ),
            ("James",   28,   "Aunt"      ),
            ("Jim",     28,   "Son"       ),
            ("Judy",    28,   "Sun"       ),
            ("Jo",      29,   "God"       ),
        ]

        sql     = """INSERT INTO people (
                  name, age, family_relation) VALUES (?,?, ? )
        """

        for name, age, family_relation in table_data:
            # this only one way to bind
            query.prepare()
            query.addBindValue(name)
            query.addBindValue(age)
            query.addBindValue(family_relation)
            query.exec_()

    #------------
    def query_print_people( self, ):
        """
        Print out the table
        """
        print_func_header( "query_print_people" )

        query           = QSqlQuery( self.db )

        print("People:")
        query.exec_("SELECT id, name, age, family_relation FROM people")
        while query.next():
            person_id           = query.value(0)
            name                = query.value(1)
            age                 = query.value(2)
            family_relation     = query.value(3)
            print(f"ID: {person_id}, Name: {name}, Age: {age} {family_relation = }")

    #------------
    def query_book_club( self, ):
        """
        Print out the table
        """
        print_func_header( "query_book_club" )

        sql     = """
            SELECT
                id,
                name,
                frequency
                FROM book_club
            """

        print_func_header( "query_book_club" )

        query           = QSqlQuery( self.db )

        print("book_club table:")

        query.exec_(sql)

        while query.next():
            a_id             = query.value(0)
            name        = query.value(1)
            frequency     = query.value(2)

            print(f"ID: {a_id = }  { name = }  {frequency = }  ")


    #------------
    def query_print_phone( self, ):
        """
        Print out the table
        """
        what    = "query_print_phone"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query           = QSqlQuery( self.db )

        print("people_phones_data table:")
        query.exec_("SELECT id, person_id, phone_number, zone FROM people_phones")
        while query.next():
            a_id             = query.value(0)
            person_id        = query.value(1)
            phone_number     = query.value(2)
            zone              = query.value(3)
            print(f"ID: {a_id = }  { person_id = }  {phone_number = }  {zone = }")

    #------------
    def query_print_people_phone( self, ):
        """
        Print a join of people and people_phones
        """
        what    = "query_print_people_phone"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query           = QSqlQuery( self.db )

        print("\nPeople and their phone numbers: join of people and people_phones")

        query.exec_("""
            SELECT people.name, people_phones.phone_number
            FROM people
            JOIN people_phones ON people.id = people_phones.person_id
            ORDER BY people.name ASC
        """)

        while query.next():
            name            = query.value(0)
            phone_number    = query.value(1)
            print(f"Name: {name}, Phone: {phone_number}")

# -------------------------------------
class KeyGen():
    """
    This is a key generator, may use in future or not
    it is quite stupid but good enough for here
    """
    #-------------------
    def __init__( self ):
        """
        what it says
        """
        self.keys     = list( range( 2000, 5000 ))
        self.ix_keys  = -1

    #-------------------
    def get_next_key( self, ):
        """
        what it says
        """
        self.ix_keys  += 1

        return self.keys[ self.ix_keys ]

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
        #self.table_model_is_hidden  = False

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

        # ---- PB "insert_more_\ndata"
        widget              = QPushButton("insert_more_\ndata")
        connect_to          = self.insert_more_data
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB "delete_\ndata"
        widget              = QPushButton("delete_\ndata")
        connect_to          = self.delete_data
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )


        # ---- PB "query_book_\nclub "
        widget              = QPushButton("query_book_\nclub ")
        connect_to          = uft.DB_OBJECT.query_book_club # see SampleDB
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

        uft.DB_OBJECT.query_book_club()
        uft.DB_OBJECT.query_print_people_phone()

    # ------------------------
    def rebuild_db(self):
        """ """
        print_func_header( "rebuild_db" )

        uft.DB_OBJECT.reset()

    #-----------------------------------------------
    def insert_more_data( self ):
        """

        """
        print_func_header( "insert_more_data" )

        db      = uft.DB_OBJECT.db

        query   = QSqlQuery( db )

        table_data = [
            ("**History",      "weekly"    ),
            ("**Adventure",    "weekly"    ),
            ("**Easterns",      "monthly"  ),
            ("**Physics",      "daily"     ),
        ]

        for name, frequency in table_data:
            # this only one way to bind
            print( f"insert {name} {frequency}")

            sql     = """INSERT INTO book_club (
                name,
                frequency  )
                VALUES (?, ? )
            """

            query.prepare( sql )

            if not query.prepare(sql):
                print(f"Prepare failed: {query.lastError().text()}")
                continue

            query.addBindValue( name )
            query.addBindValue( frequency )

            if not query.exec_():
                print(f"Execution failed: {query.lastError().text()}")
            else:
                pass
                #print("Insert successful.")

    #-----------------------------------------------
    def delete_data( self ):
        """
        I have a table:
            CREATE TABLE book_club (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                frequency       TEXT

         could you give me the sql to delete all records where name begins with "*"
         give the code for running with QSqlQuery using a bind variable for the where clause
        """
        print_func_header( "delete_data" )

        db      = uft.DB_OBJECT.db

        query   = QSqlQuery(db)

        # SQL statement with a bind variable
        sql     = "DELETE FROM book_club WHERE name LIKE ?"

        if not query.prepare(sql):
            print(f"Prepare failed: {query.lastError().text()}")

        else:
            query.addBindValue("*%")

            if not query.exec_():
                print(f"Execution failed: {query.lastError().text()}")
            else:
                print("Records deleted successfully.")



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
