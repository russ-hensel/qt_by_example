"""

Examples of the qtsql widgets in use

    this is a redoo, with time all will run on the same sample
    database and use inspection as part of there operation

    QSqlTableModel Tab


"""
# ---- top/search
""""
    Search for the following in the code below:



        crud            build_rr_w_crud_tab
        edit            EditStrat
        delegate
        groupbox
        isChecked
        get_text
        hide            hide a row
                        hide a column
        label
        lineEdit
        listbox      QListWidget         in ex_  listbox
        icon
        indexer       not yet need add_indexer  see stuffdb
        menu
        messagebox    see qt_widgets.py
        self.showMinimized()
        minimized
        select
        selectrows         table_view.setSelectionBehavior( QTableView.SelectRows )
        show
        iconify
        radiobutton
        radiobutton index
        size
        table_model                use a lot in stuffdb
                  set value at index
                  set_row_of_data
        tab tabpage
        text
        textOnLeft           for radiobutton
        widget


    See Also:

    Links
        Create Python GUIs with PyQt5 — Simple GUIs to full apps
            *>url  https://www.pythonguis.com/pyqt5/
        Qt Widget Gallery | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/gallery.html
        Widgets Classes | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/widget-classes.html


"""



#import adjust_path  # leave above imports

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


# widgets biger
# widgets -- small
# layouts
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

import ia_qt

what   = Qt.AlignCenter   # valid aligment perhaps to addWidget   layout.addWidget
import sys
#	addWidget(QWidget *widget, int stretch = 0, Qt::Alignment alignment = Qt::Alignment())
# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import above
from functools import partial

# sys.path.append( r"D:\Russ\0000\python00\python3\_examples"  )
# sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"  )
# sys.path.append( "../")  # not working today vscode
# sys.path.insert( 1, "/mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib" )
# import ex_helpers
# import gui_qt_ext

import utils_for_tabs as uft
import wat_inspector

#import table_model
#import rr_w_crud
#import table_widget


# ---- end imports
# ---- a few parameters will be deleted
rr_w_crud_app_title   = "russ_qsqlrelationalmodel_with_crud.py"
rr_w_crud_db_file     = "texs_x.db"
rr_w_crud_db_file     = ':memory:'


# note   = """
# main work example it WidgetExample
# Widget example with placer should be same with placer -- may have good salbage code
# same for the rest of the examples


# """


# print( note )




basedir = os.path.dirname(__file__)



INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_2
BEGIN_MARK_2  = uft.BEGIN_MARK_2



def delete_db_file( file_name ):
    """
    will delete any file, but intended for db file

    """
    exists    = str( os.path.isfile( file_name ) )
    print( f"{file_name} exists {exists}" )

    if exists:
        # this is the delete
        try:
            os.remove( file_name )                   # error if file not found
            print(f"removed {file_name} "  )
        except OSError as error:
            print( error )
            print( f"os.remove threw error on file {file_name}")

    else:
        print( f"file already gone  {file_name}")

# -------------------------------------
class SampleDB():
    """
    this will create an instance of SampleDB and set up two module Globals
        global EXAMPLE_DB   used to connect widgets to the db
        global DB_OBJECT    this object


    """
    #-------------------
    def __init__( self ):
        """
        The ususal
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
        global EXAMPLE_DB
        global DB_OBJECT

        if self.db is not None:
            self.db.close()
            self.db    = None  # or delete

        if DB_FILE    !=  ':memory:':
            # delete for a fresh start
            pass
            delete_db_file( DB_FILE )

        db           = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName( DB_FILE ) # ':memory:')  # In-memory database for this example
        self.db      = db
        EXAMPLE_DB   = db   # for simple module access
        DB_OBJECT    = self
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
        what    = "populate_people_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}" )

        query   = QSqlQuery( self.db )

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
        what    = "create_people_phones_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

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
        what    = "populate_people_phones_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query = QSqlQuery( self.db )

        table_data = [
            (1, "555-1234", "A"), (1, "555-5678", "B"), (1, "555-8765", "C"),
            (2, "555-4321", "A"), (1, "555-8765", "B"), (2, "555-3456", "C"),
            (3, "555-9876", "A"), (3, "555-1111", "B"), (3, "555-2222", "C"),
            (4, "555-3333", "A"), (4, "555-4444", "B"), (4, "555-5555", "C"),
            (5, "555-6666", "A"), (5, "555-7777", "B"), (5, "555-8888", "C"),
            (5, "555-9999", "A"), (5, "555-0000", "B"), (5, "555-1235", "C"),
            (2, "555-2345", "A"), (1, "555-3456", "B")
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
        Populte the book_club table
        """
        what    = "populate_book_club_table"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        query = QSqlQuery( self.db )

        # Insert 5 people into the 'people' table
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
        Create  table.
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

        # Create the 'people' table
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

        # Query all people
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
        !!Print out the table
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
    """
    #-------------------
    def __init__( self ):
        """
        """
        self.keys     = list( range( 2000, 5000 ))
        self.ix_keys  = -1

    #-------------------
    def get_next_key( self, ):
        """
        """
        self.ix_keys  += 1

        return self.ix_keys


#-----------------------------------------------
class TableModelTab( QWidget ):
    """
    and table view
    from  QAbstractTableModel
    see ez_qt table_widget and table_model table_widget
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self.build_tab()

    #-----------------------------------------------
    def build_tab( self, ):
        """

        """
        self.table_model_is_hidden  = False

        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        button_layout =  QHBoxLayout(   )

        headers = ["Name", "Age", "Occupation" ]
        #self.view           = QTableView()
        self.table_model          = table_model.TableModel( headers )  # QAbstractTableModel
        #self.model.set_data( data )

        table_view                  = QTableView()
        self.table_model_table_view = table_view
        # Connect the clicked signal to a slot
        table_view.doubleClicked.connect( self.double_clicked )
        table_view.doubleClicked.connect( self.clicked )
        table_view.setModel( self.table_model )

        print( "some selection options" )
        table_view.setSelectionBehavior( QTableView.SelectRows )       # For row selection
        # table_view.setSelectionBehavior( QTableView.SelectColumns )  # For column selection
        # table_view.setSelectionBehavior(QTableView.SelectItems)      # For item selection

        layout.addWidget( table_view )

        # ---- QPushButtons
        layout.addLayout( button_layout )
        widget        = QLabel( 'table_model\n TableModel()/QTableView()' )
        button_layout.addWidget( widget )

        widget = QPushButton("QPushButton")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("populate")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.table_model_tab_populate() )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("get_data")
        widget.clicked.connect(lambda: self.table_model_tab_get_data( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/unhide")
        widget.clicked.connect(lambda: self.table_model_hide_unhide( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/unhide column")
        widget.clicked.connect(lambda: self.table_model_toggle_hide_column( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        layout.addLayout( button_layout )
        widget        = QPushButton('Inspect')
        widget.clicked.connect(self.table_model_inspect )
        button_layout.addWidget( widget )

        # widget        = QPushButton('Info/Help')
        # connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "table_model.txt" )
        # widget.clicked.connect( connect_to )
        # button_layout.addWidget( widget )

        return tab_page

    # -------------------------------------
    def table_model_tab_populate(self,   ):
        """
        what it says
            seems ok
        populates a row at a time
        """
        model      = self.table_model
        #print( f" add_to_model_all_subjects {photo_id = } , {table = }, {table_id = },  {info =} "  )
        #key           = ( table, table_id )
        #key_row       = model_display.indexer.find( key )
        # set_row_of_data
        for ix in range( 3 ):
            # self.view_all_subjects.setModel(  self.model_all_subjects )
            # model        = self.model_display
            row_data     = [  f"a{ix}", f"b{ix}",   f"c{ix}", f"d{ix}"   ]
            #rint( f"{row_data = }")
            model.addRow( row_data)
            #model_display.indexer.set_is_valid( False )
        # set value at index
        an_index       = model.index( 2,2 )
        value          = 9999
        model.set_data_at_index(  an_index, value,  )

    #---------------------------------------
    def table_model_hide_unhide( self ):
        """
        onece filter applide not sure how to remove
        this is messed up might want to start over with chat
        """
        if self.table_model_filter:
            self.table_model_filter   = FilterProxyModelHideRows( )


    #-----------------------------------------------
    def double_clicked( self, index: QModelIndex):
        """
        what it says,
        index coms from table view
        """
        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")
        #self.add_ix_other( row )

    #-----------------------------------------------
    def clicked( self, index: QModelIndex):
        """
        what it says,
        index coms from table view
        """
        print( "clicked" )
        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")

        self.select_row( row )
        #self.add_ix_other( row )

    #-----------------------------------------------
    def select_row(self, row_index ):
         """Select a specific row."""

         print( "select_row" )
         # Get the selection model from the view
         selection_model = self.table_view.selectionModel()

         # Create an index for the row
         row_start      = self.model.index(row_index, 0)
         row_end        = self.model.index(row_index, self.model.columnCount() - 1)

         # Select the row
         selection_model.select(row_start, selection_model.Select | selection_model.Rows)

    def select_column(self, col_index):
        """
        Select a specific column.
        may want to test and hook up
        """
        # Get the selection model from the view
        selection_model = self.table_view.selectionModel()

        # Create an index for the column
        col_start       = self.model.index(0, col_index)
        col_end         = self.model.index(self.model.rowCount() - 1, col_index)

        # Select the column
        selection_model.select(col_start, selection_model.Select | selection_model.Columns)

    #-----------------------------------------------
    def table_model_toggle_hide_column(self,   ):
        """
        we actually use the view
        """
        print( "table_model_toggle_hide_column")
        self.table_model_is_hidden  = not self.table_model_is_hidden
        if self.table_model_is_hidden:
            self.table_model_table_view.hideColumn( 1 )
        else:
            self.table_model_table_view.showColumn( 1 )

        self.table_model_table_view.show()


    #-----------------------------------------------
    def table_model_tab_get_data(self,   ):
        """
        what it says
        seem ok
        """
        model           = self.table_model

        table_model.model_dump( model )

        data_list       = [  ]
        ix_row          = 0
        for ix_col in range( 3 ):
            index     = model.index( ix_row, ix_col )
            data      = model.data( index, ) #role=Qt.DisplayRole)
            data_list.append( data )
        print( f"table_model_tab_get_data   {data_list = }" )

    # ------------------------------------------
    def table_model_inspect(self):
        """
        what it says, read
        """
        # ia_qt.ia_obj( self.table_model,             msg = "table_model_inspect" )
        # ia_qt.ia_obj( self.table_model_table_view,  msg = "table_view_inspect" )
        ia_qt.q_abstract_table_model( self.table_model,   msg = "table_model_inspect" )

        view     = self.table_model_table_view
        # def get_selected_row_and_column():
        selected_indexes = view.selectionModel().selectedIndexes()
        if selected_indexes:
            for index in selected_indexes:
                row     = index.row()
                column  = index.column()
                print(f"Selected Cell - Row: {row}, Column: {column}")
        else:
            print("No selection")

    # ------------------------------------------
    def add_row_at_end(self):
        """
        may work needs to be hooked up
        """
        row_position = self.table_widget_1.rowCount()
        self.table_widget_1.insertRow( row_position )
    # ------------------------------------------
    def remove_row_currrent(self):
        """
        may work needs to be hooked up
        """
        row_position = self.table_widget_1.currentRow()
        self.table_widget_1.removeRow(row_position)

    # ------------------------------
    def set_size(self):
        """
        read it
        may work needs to be hooked up
        """

        self.table_widget_1.horizontalHeader().setStretchLastSection(True)
        self.table_widget_1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # ------------------------------
    def sort(self):
        """
        read it
        """
        """
        may work needs to be hooked up
        """
        msg   = "click headers to sort   "
        print( msg )
        # !! more research on args
        self.table_widget_1.sortItems (  1 , Qt.AscendingOrder  )

    # ------------------------------
    # def on_list_clicked( self  index: QModelIndex ): ) :
    #     """
    #     read it
    #     """
    #     msg   = "click headers to sort   "
    #     print( msg )
    # ------------------------------
    def on_cell_clicked( self, row, col  ):
        """
        read it

        """
        """
        may work needs to be hooked up
        """
        table      = self.table_widget_1

        item       = table.item( row, col )
        if item:
            print(f"Cell clicked: Row {row}, Column {col}, Data: {item.text()}")
        else:
            print(f"Cell clicked: Row {row}, Column {col}, Data: None")

    # ------------------------------
    def search(self, search_for   = "1," ):
        """
        read it
        passing of argument unclear ????
        """
        """
        may work needs to be hooked up
        """
        search_for   = "1,"
        msg          = f"search {search_for = }"
        print( msg )
        a_widget    =    self.table_widget_1
        # Clear current selection.
        a_widget.setCurrentItem( None )

        if not search_for:
            msg      =  "Empty string, don't search."
            print( msg )
            return

        matching_items = a_widget.findItems(search_for,  Qt.MatchContains )
        if matching_items:
            # We have found something.
            item       = matching_items[0]  # Take the first.
            msg        = f"found {item = }"
            print( msg )
            a_widget.setCurrentItem(item)
        else:
            msg        = f"nothing found {search_for = }"
            print( msg )

    def find_row_with_text( self  ):
        """
        read it

        """
        table               = self.table_widget_1
        ix_col_searched     = 2
        ix_found            = None
        target_text   = "Cell (2, 2)"
        for row in range( table.rowCount() ):
            item = table.item( row, ix_col_searched )  # Column 5
            if item and item.text() == target_text:
                ix_found = row

        print( f"find_row_with_text {ix_found = }")

        return ix_found

    def find_row_with_text_in_column(self, ):
        """
        might be faster
        might be wrong depending on how matching works
        from chat
        may be ok not yet tested
        """
        table               = self.table_widget_1

        ix_col_searched     = 2
        ix_found            = None
        target_text     = "xyz"

        matching_items = table_widget.findItems(target_text, QtCore.Qt.MatchExactly)
        for item in matching_items:
            if item.column() == column:
                ix_found            =  item.row()

        print( f"find_row_with_text {ix_found = }")

        return ix_found


# print( "!! next not completed")



#-----------------------------------------------
class QSqlQueryTab( QWidget ):
    """
    Yes, you can use a QSqlQueryModel to loop through all the rows of a
    database table. While QSqlQueryModel is primarily a model class for
    displaying read-only data in views like QTableView, you can
    still access the data programmatically by iterating through the rows and columns.

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


        widget = QPushButton( "Loop with\nQSqlQuery\nthirdline" )
        widget.clicked.connect(lambda: self.loop_with_qsqlquery( ) )
        widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

    #-----------------------------------------------
    def loop_with_qsqlquery( self ):
        """
        Stream data row by row using QSqlQuery to avoid loading everything into memory.
        """
        print( "" )
        print( "QSqlQueryTab.loop_with_qsqlquery uses EXAMPLE_DB" )
        query = QSqlQuery( "SELECT name, age FROM people", EXAMPLE_DB )
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


#-----------------------------------------------
class QTableWidgetTab( QWidget ):
    """
    here build a tab in its own class to hide its variables
    and have its own namespace
    this delegate interacts with a view
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
        layout              = QVBoxLayout( tab_page )

        table_widget        = QTableWidget(4, 5)  # row, column ??third arg parent
        self.table_widget   = table_widget
        layout.addWidget( table_widget )

        # ---- insert data --- now a mess, parameterize this
        print( "this adds cell 'upside down' and cell cords are ng ")
        for i in range( 4, 0,   -1 ):  # better match table
            for j in range( 5,  0, -1 ):  # col
                # these items arguments must be strings
                item     = QTableWidgetItem( "Cell ({}, {})".format( i, j) )
                table_widget.setItem(i, j, item)

        ix_col   = 1
        table_widget.setColumnWidth( ix_col, 22 )
        # Set selection behavior and mode

        print( "how select_row works may depend on these ")
        table_widget.setSelectionBehavior( QAbstractItemView.SelectRows )  # Can be SelectRows, SelectColumns, or SelectItems
        # table_widget.setSelectionMode(QAbstractItemView.MultiSelection)  # Can be SingleSelection or MultiSelection

        # set row count works but messes up model
        # row_count   = 2
        # a_widget.setRowCount( row_count )  # increase or decrease rows

        print( "also setColumnCount()  ")

        #self.table.setHorizontalHeaderLabels(employees[0].keys())

        labels  = [ "label0" ]   #ok
        labels  = [ "label0", "label1",
                    "label2", "label3", "label4" ] # too many also ok

        table_widget.setHorizontalHeaderLabels( labels  )
        table_widget.setSortingEnabled( True )

        table_widget.setSortingEnabled( True )

        table_widget.cellClicked.connect( self.on_cell_clicked )

        #layout.addWidget(self.table)  # Add the table to the layout

        # getting an error !!
        print( f"{table_widget.currentRow()}")
            # method returns the currently selected row. It returns -1 i

        # ---- buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # --- begin a_widget method
        a_widget           = QPushButton("add_row_at_end")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.add_row_at_end)

        button_layout.addWidget(a_widget)


        # delete or remove a row
        a_widget           = QPushButton("remove_row_currrent")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.remove_row_currrent)
        button_layout.addWidget(a_widget)

        # delete or remove a row
        a_widget           = QPushButton("set_size")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.set_size)
        button_layout.addWidget(a_widget)

        #
        a_widget           = QPushButton("sort")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.sort)
        button_layout.addWidget(a_widget)

        # ---- search
        a_widget           = QPushButton( "search" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.search )
        button_layout.addWidget(a_widget)

        # ---- search
        a_widget           = QPushButton( "find_row_with_text" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.find_row_with_text )
        button_layout.addWidget(a_widget)




        # # ---- QLineEdit  can it hold some data, the date?
        # widget          = QLineEdit()
        # widget.setText( "QLineEdit use set text to set value")
        # layout.addWidget( widget )


        # # ---- QPushButton
        # widget              = QPushButton("QPushButton x")
        # self.button_ex_1    = widget
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # a_widget        = widget
        # widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        # layout.addWidget( widget )


        # Create the table widget with 3 rows and 3 columns
        self.table_widget = QTableWidget(3, 3)

        # Set up column headers
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Add some sample data to the table
        self.populate_table()

        # Set selection behavior and mode
        self.table_widget.setSelectionBehavior( QAbstractItemView.SelectRows)  # Can be SelectRows, SelectColumns, or SelectItems
        self.table_widget.setSelectionMode(QAbstractItemView.MultiSelection)   # Can be SingleSelection or MultiSelection

        # Programmatically select a row and a column
        self.select_row(1)  # Select the second row (index 1)
        self.select_column(2)  # Select the third column (index 2)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    # -------------------------------------
    def populate_table(self):
        """Populate the table with some sample data."""
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row + 1}, {col + 1}")
                self.table_widget.setItem(row, col, item)

    # -------------------------------------
    def select_row(self, row_index):
        """Select a specific row.
        may depend on selection mode
        """
        print( f"select_row {row_index = }")
        self.table_widget.selectRow( row_index )

    # -------------------------------------
    def select_column(self, col_index):
        """Select a specific column."""
        self.table_widget.selectColumn(col_index)


    # ------------------------------
    def on_cell_clicked( self, row, col  ):
        """
        read it

        """
        print( "on_cell_clicked ")
        table      = self.table_widget

        item       = table.item( row, col )
        if item:
            print(f"Cell clicked: Row {row}, Column {col}, Data: {item.text()}")
        else:
            print(f"Cell clicked: Row {row}, Column {col}, Data: None")

        print( "enable some select if you wish ")
        self.select_row( row )


    # some of next may be mixed up with tableModel, beware
    # -------------------------------------
    def add_row_at_end(self):
        row_position = self.table_widget_1.rowCount()
        self.table_widget_1.insertRow( row_position )

    # -------------------------------------
    def remove_row_currrent(self):
        row_position = self.table_widget_1.currentRow()
        self.table_widget_1.removeRow(row_position)

    # ------------------------------
    def set_size(self):
        """
        read it
        """
        self.table_widget_1.horizontalHeader().setStretchLastSection(True)
        self.table_widget_1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # ------------------------------
    def sort(self):
        """
        read it
        """
        msg   = "click headers to sort   "
        print( msg )
        # !! more research on args
        self.table_widget.sortItems (  1 , Qt.AscendingOrder  )


    # ------------------------------
    def search(self, search_for   = "1," ):
        """
        read it
        passing of argument unclear ????
        """
        search_for   = "1,"
        msg          = f"search {search_for = }"
        print( msg )
        a_widget    =    self.table_widget_1
        # Clear current selection.
        a_widget.setCurrentItem( None )

        if not search_for:
            msg      =  "Empty string, don't search."
            print( msg )
            return

        matching_items = a_widget.findItems(search_for,  Qt.MatchContains )
        if matching_items:
            # We have found something.
            item       = matching_items[0]  # Take the first.
            msg        = f"found {item = }"
            print( msg )
            a_widget.setCurrentItem(item)
        else:
            msg        = f"nothing found {search_for = }"
            print( msg )

    #----------------------------
    def find_row_with_text( self  ):
        """
        read it
        getText get text
        """
        table               = self.table_widget_1
        ix_col_searched     = 2
        ix_found            = None
        target_text   = "Cell (2, 2)"
        for row in range( table.rowCount() ):
            item = table.item( row, ix_col_searched )  # Column 5
            if item and item.text() == target_text:
                ix_found = row

        print( f"find_row_with_text {ix_found = }")

        return ix_found

    #----------------------------
    def find_row_with_text_in_column(self, ):
        """
        might be faster
        might be wrong depending on how matching works
        from chat
        may be ok not yet tested
        """
        table               = self.table_widget_1

        ix_col_searched     = 2
        ix_found            = None
        target_text     = "xyz"

        matching_items = table_widget.findItems(target_text, QtCore.Qt.MatchExactly)
        for item in matching_items:
            if item.column() == column:
                ix_found            =  item.row()

        print( f"find_row_with_text {ix_found = }")

        return ix_found


# ---- new redoing work under way or even done ** ------------------------------------------------
#-----------------------------------------------
class QSqlDatabaseTab( QWidget ):
    """
    for the basic dabase object
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

        button_layout =  QHBoxLayout(   )
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
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    # ------------------------
    def breakpoint(self):
        """ """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        breakpoint()

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        # make some locals for inspection
        the_global_db   = DB_OBJECT
        # parent_window = self.parent( ).parent( ).parent().parent()
        # a_db          = parent_window.sample_db
        # model         = self.people_model
        # view          = self.people_view
        wat_inspector.go(
             msg            = "see the_global_db",
             inspect_me     = the_global_db,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def print_db(self):
        """ """
        what    = "print_db"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_print_people()
        DB_OBJECT.query_print_phone()
        DB_OBJECT.query_print_people_phone()

    # ------------------------
    def rebuild_db(self):
        """ """
        what    = "rebuild_db"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.reset()

#-----------------------------------------------
class QSqlRelationalTableModelTab( QWidget ):
    """

    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self._build_model()
        self._build_gui()

        self.model.select()

        #form = FormWidget(model, 0)
        #form.setWindowTitle('Edit Person Record')
        #form.show()

    # ------------------------------
    def _build_gui( self,   ):
        """

        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.view   )

        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # # ---- PB xxxxxx
        # widget              = QPushButton("QPushButton\n x")
        # self.button_ex_1    = widget
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        # button_layout.addWidget( widget )

        widget            = QPushButton( "select_for\n_all" )
        connect_to        = self.select_all
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        widget            = QPushButton( "select_\n_some" )
        connect_to        = self.select_some
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        widget            = QPushButton("insert\n_record")
        connect_to        = self.add_record
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

        sql behind this should be:
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people
            LEFT JOIN people_phones ON people.id = people_phones.person_id


        """

        model           = QSqlRelationalTableModel(self)
        self.model      = model
        # self.model          = qt_with_logging.QSqlRelationalTableModelWithLogging(
        #     self )
        model.setTable( "people" )

        debug_var   = self.model.fieldIndex( "id" )   # field name to number

        model.setRelation(
            self.model.fieldIndex( "id" ),  # column name in first table, here people

            QSqlRelation("people_phones", "person_id",      "phone_number")
            #             table to join to
            #                             column to join on
            #                                               # columns to fitch.display
        )

        column_index = model.fieldIndex( "age" )  # Get the column index for "name"
        print( f"{column_index = }")
        model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no
            # is this working ??


        # Set headers -- claud
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "Name")
        model.setHeaderData(2, Qt.Horizontal, "Age")
        model.setHeaderData(3, Qt.Horizontal, "Family Relation")
        model.setHeaderData(4, Qt.Horizontal, "Phone Number")

        # Set filter on table peplpe
        #self.model.setFilter( f"id =''" )  # think this is wrong

        # Configure headers and load data
        # self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        model.setEditStrategy(QSqlRelationalTableModel.OnManualSubmit)
        self.select_all()

        # Setup table view and add it to the layout
        view        = QTableView()
        self.view   = view
        view.setModel( model)

        # Adjust view properties
        view.resizeColumnsToContents()
        view.setAlternatingRowColors(True)
        view.setSortingEnabled(True)    # is thid click on header?



        # model->select();
        #model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));


    # ------------------------
    def _people_view_clickedxxx(self, index,   ):
        """ """
        what    = "_people_view_clicked"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        view    = self.people_view
        msg     = f"_view_clicked  "
        print( msg )
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

        msg     = f"{INDENT}xtracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}xtracted data {key = }   "
        print( msg )

        # ---- sync up second model
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def add_record(self):
        """
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people
            LEFT JOIN people_phones ON people.id = people_phones.person_id


"""
        what    = "add_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        model     = self.model

        # Assuming `model` is your QSqlRelationalTableModel instance for the `people` table

        # Create a new empty record for the 'people' table
        new_record      = model.record()

        # Set values for each field in the new record
        new_record.setValue("id", 123)                # Replace 123 with the actual ID value
        new_record.setValue("name", "John Doe")       # Set name
        new_record.setValue("age", 30)                # Set age
        new_record.setValue("family_relation", "Brother")  # Set family relation

        # Insert the new record at the end of the table
        if model.insertRecord(-1, new_record):
            # Try to submit all changes to the database
            if model.submitAll():
                print("Record inserted and changes committed to the database.")
            else:
                print("Error committing changes:", model.lastError().text())
        else:
            print("Error inserting record:", model.lastError().text())
        pass # for debug

    # ------------------------
    def xxxx(self):
        """ """
        what    = "xxxx"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_data()

    # ------------------------
    def breakpoint(self):
        """ """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()

    # ------------------------
    def select_all(self):
        """ """
        what    = "select_all greater than joe"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        model        = self.model
        column_index = model.fieldIndex( "age" )  # Get the column index for "name"
        print( f"for sorting {column_index = }")
        model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no


        model.setFilter( "" )
        model.select()

    # ------------------------
    def select_some(self):
        """ """
        what    = "select_some"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        self.model.setFilter('name < LOWER( "aaa" ) '   )  # which is greaterr


        self.model.select()
    # ------------------------
    def do_selections(self):
        """ """
        what    = "print_data"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db                    = parent_window.sample_db
        local_self_model        = self.model
        local_self_view         = self.view
        wat_inspector.go(
             msg            = "self.model from inspect method",
             #inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # # ------------------------
    # def inspect_ia(self):
    #     """ """
    #     ia_qt. ia_obj(      self,
    #                         msg             = "self, just a test ",
    #                         max_len         = None,

    #                         print_it        = True,
    #                         sty             = "",
    #                         include_dir     = False,
    #                         )


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
        # ---- people
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
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
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
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
    def _people_view_clicked(self, index,   ):
        """ """
        what    = "_people_view_clicked"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

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

        msg     = f"{INDENT}xtracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}xtracted data {key = }   "
        print( msg )

        # ---- sync up second model
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def add_record(self):
        """
        !!What it says
        """
        what    = "add_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # -----------------------
    def delete_selected_record(self):
        """
        !!What it says
        """
        what    = "delete_selected_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")


    # -----------------------
    def save(self):
        """
        !!What it says
        """
        what    = "add_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")


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
        what    = "select_all"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        self.people_model.select()  # Load the data into the model
        self.phone_model.select()   # Load the data into the model

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db          = parent_window.sample_db
        model         = self.people_model
        view          = self.people_view
        wat_inspector.go(
             msg            = "self.model from inspect method",
             # inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()


#---- Master Window ===========================================================
class QtSqlWidgetExamples( QMainWindow ):
    def __init__(self):
        """
        Lots of widget to run and examine each in own tab
        eventually all against the same db
        """
        super().__init__()

        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 1400
        qt_height   = 700

        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        self._build_menu()
        self.doc_dir             = "./docs/"
        self.create_db()

        self._build_gui()

        self.table_model_filter = None   # will be used to hide unhide

        return

    #------------------------------
    def _build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( "QtSqlWidgetExamplesInTabs" )

        self.setWindowIcon( QtGui.QIcon( './designer.png' ) )  # cannot get this to work

        central_widget          = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout   =  QVBoxLayout( central_widget )

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

        # ---- Done
        tab      = uft.SeperatorTab()
        title    = "Tab\nDone>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlDatabaseTab  -- will create and populate the db
        tab      = QSqlDatabaseTab()
        title    = "QSqlDatabase\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_database_tab.txt"

        # ----
        tab      = uft.SeperatorTab()
        title    = "Tab\nDraft>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlTableModelTab
        tab      = QSqlTableModelTab()
        title    = "QSqlTableModel\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_table_model_tab.txt"

        tab      = uft.SeperatorTab()
        title    = "Tab\nTBD>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlDatabaseTab
        tab      = QSqlRelationalTableModelTab()
        title    = "QSqlRelationalTableModel\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_relational_table_model_tab.txt"

        tab      = uft.SeperatorTab()
        title    = "Tab\nPlanned>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlQueryTab
        tab      =  QSqlQueryTab()
        title    = "QSqlQueryTab\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_query_tab.txt"

        # ---- QTableWidgetTab
        tab      =  QTableWidgetTab()
        title    = "QTableWidgetTab\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "q_table_widget_tab.txt"

        print( "later tabs are messing up the db beware")

        # tab      = TableModelTab()
        # title    = "TableModelTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "table_model_tab.txt"

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



        # tab      = QSqlQueryTab()
        # title    = "QSqlQueryTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "q_sql_Query_tab.txt"

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


        action          = QAction( "General Help...", self )
        connect_to      = partial( self.open_txt_file, "./docs/general_help_maybe.txt" )
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
    # def open_general_help( self,   ):
    #     """
    #     what it says read:

    #     """
    #     doc_name        = f"{self.doc_dir}qsql_widgets_help.txt"
    #     ex_editor       = r"xed"
    #     proc            = subprocess.Popen( [ ex_editor, doc_name ] )



    #     proc               = subprocess.Popen( [ ex_editor, doc_name ] )

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
        """
        tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
        doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        doc_name            = f"{self.doc_dir}{doc_name}"
        print( f"{doc_name = }")
        ex_editor          = r"xed"
        #connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "table_model.txt" )

        self.open_txt_file( doc_name )

    #-------
    def open_txt_file( self, file_name  ):
        """
        what it says read
        """
        proc               = subprocess.Popen( [ TEXT_EDITOR, file_name ] )


# ---- run and a few parameters
# --------------------
if __name__ == "__main__":


    TEXT_EDITOR   = "xed"
    # ---- quasi constants  -- one time setup per run
    # control with comments
    DB_FILE       = "sample.db"
    #DB_FILE       =  ':memory:'

    # next will be created and populated
    EXAMPLE_DB    = None  # populated later anyone can connect to this it is open
    DB_OBJECT     = None  # for its onwn functions

    app         = QApplication(sys.argv)
    dialog      = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog

    window      = QtSqlWidgetExamples()
    window.show()
    app.exec()

    sys.exit( 0 )  # cleanup do we need


# ---- eof

