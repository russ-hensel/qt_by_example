"""

Examples of the qtsql widgets in use

    this is a redo, with time all will run on the same sample
    database and use inspection as part of there operation

    QSqlTableModel Tab


"""
# ---- top/search
""""
    Search for the following in the code below:



        crud            build_rr_w_crud_tab
        edit            EditStrat
        delegate

        get_text
        hide            hide a row
                        hide a column
        label


        select
        selectrows         table_view.setSelectionBehavior( QTableView.SelectRows )
        show


        table_model                use a lot in stuffdb
                  set value at index
                  set_row_of_data



    See Also:

    Links



"""


# ---- imports

from platform import python_version
import inspect
import os
import subprocess
import sys
from subprocess import PIPE, STDOUT, Popen, run
import sqlite3 as lite

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
                             QTabWidget, QTextEdit, QVBoxLayout, QWidget, QHeaderView)



import sys

from functools import partial


import utils_for_tabs as uft
import parameters
import qt_table_model

import wat_inspector

import tab_q_sql_relational_model_1
import tab_q_sql_relational_model_2
import tab_q_sql_relational_model_3
import tab_table_model
import tab_qsql_table_model
import tab_qsql_database
import tab_q_table_widget
import tab_q_sql_query

basedir         = os.path.dirname(__file__)


INDENT          = uft.INDENT
BEGIN_MARK_1    = uft.BEGIN_MARK_2
BEGIN_MARK_2    = uft.BEGIN_MARK_2

print_func_header  = uft.print_func_header

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

#-----------------------------------------------
class FilterProxyModelHideRows( QSortFilterProxyModel ):
    def __init__(self, rows_to_hide=None, *args, **kwargs):
        """
        from chat need to document
        :param rows_to_hide: DESCRIPTION, defaults to None
        :type rows_to_hide: TYPE, optional
        :param *args: DESCRIPTION
        :type *args: TYPE
        :param **kwargs: DESCRIPTION
        :type **kwargs: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        super().__init__(*args, **kwargs)
        # Store the list of row indices to hide
        self.rows_to_hide = rows_to_hide if rows_to_hide is not None else []

    # Custom filtering method to hide specific rows
    def filterAcceptsRow(self, source_row, source_parent):
        # Hide the row if its index is in the rows_to_hide list
        return source_row not in self.rows_to_hide

    # Method to update the list of rows to hide
    def setRowsToHide(self, rows):
        self.rows_to_hide = rows
        self.invalidateFilter()  # Reapply the filter to update the view

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

        if DB_FILE    !=  ':memory:':
            # delete for a fresh start
            pass
            delete_db_file( DB_FILE )

        db              = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName( DB_FILE )
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
            sql_con    = lite.connect( DB_FILE )
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
        what    = "query_print_people"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

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

        return self.ix_keys


#---- Master Window ===========================================================
class QtSqlWidgetExamples( QMainWindow ):
    def __init__(self):
        """
        Lots of widget to run and examine each in own tab
        eventually all against the same db
        """
        super().__init__()

        my_parameters   = parameters.Parameters()
        self.parameters = my_parameters
        uft.parameters  = my_parameters
        uft.main_window = self
        qt_xpos         = my_parameters.qt_xpos
        qt_ypos         = my_parameters.qt_ypos
        qt_width        = my_parameters.qt_width
        qt_height       = my_parameters.qt_height

        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        # !! still needs work
        global DB_FILE

        DB_FILE             = my_parameters.db_file_name
        uft.TEXT_EDITOR     = my_parameters.text_editor

        self._build_menu()
        self.doc_dir        = "./docs/"
        self.create_db()

        self._build_gui()

        self.table_model_filter = None   # will be used to hide unhide

    #------------------------------
    def _build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( "QtSqlWidgetExamplesInTabs" )

        # self.setWindowIcon( QtGui.QIcon( './designer.png' ) )  # cannot get this to work
        self.setWindowIcon( QtGui.QIcon( self.parameters.icon  )   )
        central_widget          = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout   =  QVBoxLayout( central_widget )

        minimun_useful          = self.parameters.minimun_useful
        # --- out main layout
        layout      = QVBoxLayout(   )
        central_widget_layout.addLayout( layout )

        # ---- Create tabs
        self.tab_help_dict      = {}
        self.tab_widget         = QTabWidget()   # really the folder for the tabs
                                                 # tabs themselves are just QWidgets

        # Set custom height for the tabs
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 40px; }") # 40 enough for 2 lines ??
        layout.addWidget( self.tab_widget   )

        # # ---- Done
        # tab      = uft.SeperatorTab()
        # title    = "Tab\nDone>>"
        # self.tab_widget.addTab( tab, title  )
        # ---- TableModelTab
        tab      = tab_table_model.TableModelTab()
        title    = "TableModelTab\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "table_model_tab.txt"

        # ---- QTableWidgetTab
        tab      =  tab_q_table_widget.QTableWidgetTab()
        title    = "QTableWidget\nMostly Broken"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "q_table_widget_tab.txt"

        # ---- QSqlQueryTab
        tab      =  tab_q_sql_query.QSqlQueryTab()
        title    = "QSqlQuery\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_query_tab.txt"

        # ---- QSqlDatabaseTab  -- will create and populate the db
        if minimun_useful <= 20:  # number is usefulness of tab
            tab      = tab_qsql_database.QSqlDatabaseTab()
            title    = "QSqlDatabase\n"
            self.tab_widget.addTab( tab, title  )
            self.tab_help_dict[ title ] = "qsql_database_tab.txt"

        # # ----
        # tab      = uft.SeperatorTab()
        # title    = "Tab\nDraft>>"
        # self.tab_widget.addTab( tab, title  )


        # ---- QSqlTableModelTab
        tab      = tab_qsql_table_model.QSqlTableModelTab()
        title    = "QSqlTableModel\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_table_model_tab.txt"

        # tab      = uft.SeperatorTab()
        # title    = "Tab\nTBD>>"
        # self.tab_widget.addTab( tab, title  )

        # ---- QSqlRelationalTableModelTab_1
        tab      = tab_q_sql_relational_model_1.QSqlRelationalTableModelTab_1()
        title    = "QSqlRelationalTableModel_1\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_relational_table_model_tab_1.txt"

        # ---- QSqlRelationalTableModelTab_2
        tab      = tab_q_sql_relational_model_2.QSqlRelationalTableModelTab_2()
        title    = "QSqlRelationalTableModel_2\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_relational_table_model_tab_2.txt"

        # ---- QSqlRelationalTableModelTab_2
        tab      = tab_q_sql_relational_model_3.QSqlRelationalTableModelTab_3()
        title    = "QSqlRelationalTableModel_3\n"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_relational_table_model_tab_3.txt"
        # tab      = uft.SeperatorTab()
        # title    = "Tab\nPlanned>>"
        # self.tab_widget.addTab( tab, title  )


        print( "later tabs are messing up the db beware")

        # tab      = QTableWidgetTab()
        # title    = "QTableWidgetTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "table_widget_tab.txt"

        # tab      = DataMapperTab()
        # title    = "DataMapperTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "data_mapper_tab.txt"

        # tab      = DataMapperDelegateTab()
        # title    = "DataMapper\nDelegateTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "data_mapper_delegate_tab.txt"


        # tab      = DelegateTab()
        # title    = "DelegateTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "delegate_tab.txt"

        # tab      = DelegateToLineEditsTab()
        # title    = "DelegateToLineEditsTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "delegate_line_edit_tab.txt"

        # tab      = self.build_db_tab()
        # self.tab_widget.addTab( tab, "BasicDB"  )

        # tab      = self.build_tvrmd_tab()
        # self.tab_widget.addTab( tab, "build_tvrmd_tab"  )

        # tab      = self.build_tvtmt_tab()
        # self.tab_widget.addTab( tab, "build_tvtmt_tab"  )
        # # tableview_tablemodel_titles.py  tvtmt

        # tab      = self.build_wmc_tab()
        # self.tab_widget.addTab( tab, "build_wmc_tab"  )

        # # look at later
        # # tab      = self.build_rr_w_crud_tab()
        # # self.tab_widget.addTab( tab, "build_rr_w_crud_tab"  )

        # # self.tab_widget.addTab( self.build_layout_tab( ), "Layouts" )

        # # tab      = self.create_tab_with_buttons( ["Button 1", "Button 2", "Button 3"])
        # # self.tab_widget.addTab( tab, "Tab 1"  )

    # ------------------------------------
    def _build_menu( self,  ):
        """
        what it says read:
        """
        menubar         = self.menuBar()
        self.menubar    = menubar

        # a_menu.addSeparator()

        # ---- Help
        menu_help       = menubar.addMenu( "Help" )

        action          = QAction( "README.md...", self )
        connect_to      = partial( self.open_txt_file, "README.md" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Guide to QT Widgets...", self )
        connect_to      = partial( self.open_txt_file, "./docs/guide_to_qt_widgets.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "General Help...", self )
        connect_to      = partial( self.open_txt_file, "./docs/general_help.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Current Tab Help...", self )
        connect_to      = self.open_tab_help
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Developer Notes...", self )
        connect_to      = partial( self.open_txt_file, "readme_rsh.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )


        action          = QAction( "Display Parmss...", self )
        #connect_to      = partial( self.open_txt_file, "readme_rsh.txt" )
        action.triggered.connect( self.show_parameters  )
        menu_help.addAction( action )

    #----------------------------
    def not_implemented( self,   ):
        """
        what it says read:
        """
        QMessageBox.information(self, "Not Implemented", "Working on this...")

    #-------
    def create_db( self,   ):
        """
        what it says read:
        """
        self.sample_db          =  SampleDB()

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
        """
        tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
        doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        doc_name            = f"{self.doc_dir}{doc_name}"
        #rint( f"{doc_name = }")

        self.open_txt_file( doc_name )

    #-------
    def open_txt_file( self, file_name  ):
        """
        what it says read
        """
        proc               = subprocess.Popen( [ uft.TEXT_EDITOR, file_name ] )


    # -----------------------
    def show_parameters(self):
        """
        what it says,
        """
        uft.show_parameters( )




def main():
    # ---- run and a few parameters

    uft.TEXT_EDITOR   = "xed"
    # ---- quasi constants  -- one time setup per run
    # control with comments --- move to parameters
    # DB_FILE       = "sample.db"
    # DB_FILE       =  ":memory:"


    app                 = QApplication( [] )

    a_wat_inspector     = wat_inspector.WatInspector( app ) # Create an instance of your custom QDialog

    window              = QtSqlWidgetExamples()
    window.show()
    ret_exec            = app.exec()

    sys.exit( ret_exec )  # cleanup do we need



# --------------------
if __name__ == "__main__":
    main()

# ---- eof

