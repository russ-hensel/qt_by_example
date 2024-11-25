#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:31:35 2024

tab_q_table_widget.py
"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main()
# --------------------


import inspect
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


from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from PyQt5.QtWidgets import (QAbstractItemView,
                             QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDataWidgetMapper,
                             QDateEdit,
                             QDateTimeEdit,
                             QDialog,
                             QDoubleSpinBox,
                             QFormLayout,
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
                             QSpinBox,
                             QStyledItemDelegate,
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
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header


#-----------------------------------------------
class QTableWidgetTab( QWidget ):
    """
    here build a tab in its own class to hide its variables
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """
        the usual
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
        a_widget           = QPushButton("add_row\n_at_end")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.add_row_at_end)

        button_layout.addWidget(a_widget)

        # delete or remove a row
        a_widget           = QPushButton("remove_row\n_current")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.remove_row_currrent)
        button_layout.addWidget(a_widget)

        # delete or remove a row
        a_widget           = QPushButton("set_size\n")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.set_size)
        button_layout.addWidget(a_widget)

        #
        a_widget           = QPushButton("sort\n")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.sort)
        button_layout.addWidget(a_widget)

        # ---- search
        a_widget           = QPushButton( "search\n" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.search )
        button_layout.addWidget(a_widget)

        # ---- find_row_with_text
        a_widget           = QPushButton( "find_row_\nwith_text" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.find_row_with_text )
        button_layout.addWidget(a_widget)

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

        # Create the table widget with 3 rows and 3 columns
        self.table_widget = QTableWidget(3, 3)

        # Set up column headers
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Add some sample data to the table
        self.populate_table()

        # Set selection behavior and mode
        self.table_widget.setSelectionBehavior( QAbstractItemView.SelectRows)  # Can be SelectRows, SelectColumns, or SelectItems
        self.table_widget.setSelectionMode(QAbstractItemView.MultiSelection)   # Can be SingleSelection or MultiSelection

        # Pro grammatically select a row and a column
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
        print_func_header( "select_row" )

        print( f"select_row {row_index = }")
        self.table_widget.selectRow( row_index )

    # -------------------------------------
    def select_column(self, col_index):
        """Select a specific column."""
        print_func_header( "select_column" )

        self.table_widget.selectColumn(col_index)

    # ------------------------------
    def on_cell_clicked( self, row, col  ):
        """
        read it

        """
        print_func_header( "on_cell_clicked" )

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
        """ """
        print_func_header( "add_row_at_end" )

        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow( row_position )

    # -------------------------------------
    def remove_row_currrent(self):
        """
        what it says
        """
        print_func_header( "remove_row_current" )

        row_position = self.table_widget.currentRow()
        self.table_widget.removeRow( row_position )

    # ------------------------------
    def set_size(self):
        """
        read it
        """
        table   = self.table_widget
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # ------------------------------
    def sort(self):
        """
        read it
        """
        print_func_header( "sort")

        # !! more research on args
        self.table_widget.sortItems ( 1, Qt.AscendingOrder  )

    # ------------------------------
    def search(self, search_for   = "1," ):
        """
        read it
        passing of argument unclear ????
        """
        print_func_header( "search")

        search_for   = "1,"
        msg          = f"search {search_for = }"
        print( msg )
        a_widget    =    self.table_widget
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
        print_func_header( "find_row_with_text" )

        table               = self.table_widget
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
        !! revisit  -- seems not to be connected
        might be faster
        might be wrong depending on how matching works
        from chat
        may be ok not yet tested
        """
        print_func_header( "find_row_with_text_in_column" )

        table               = self.table_widget

        ix_col_searched     = 2
        ix_found            = None
        target_text         = "xyz"

        matching_items      = table.findItems(target_text, QtCore.Qt.MatchExactly )
        for item in matching_items:
            if item.column() == column:
                ix_found            =  item.row()

        print( f"find_row_with_text {ix_found = }")

        return ix_found

    # ------------------------
    def breakpoint(self):
        """
        the usual
        """
        print_func_header( "breakpoint" )

        breakpoint()

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection

        self_table_widget   = self.table_widget

        wat_inspector.go(
             msg            = "inspect...",
             a_locals       = locals(),
             a_globals      = globals(), )


# ---- eof