#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tab_table_model.py


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

print_func_header =  uft.print_func_header

# ---- end imports


#-----------------------------------------------
class TableModelTab( QWidget ):
    """
    and table view
    from  QAbstractTableModel
    see ez_qt table_widget and table_model table_widget
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
        the usual
        """
        self.table_model_is_hidden  = False

        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        button_layout = QHBoxLayout(   )

        headers = ["Name", "Age", "Occupation" ]
        #self.view           = QTableView()
        self.table_model          = qt_table_model.TableModel( headers )  # QAbstractTableModel
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
        # widget        = QLabel( 'table_model\n TableModel()/QTableView()' )
        # button_layout.addWidget( widget )

        # widget          = QPushButton("QPushButton")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # a_widget        = widget
        # #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        # button_layout.addWidget( widget )

        #-------------
        widget          = QPushButton( "table_model_\ntab_populate" )
        a_widget        = widget
        widget.clicked.connect( lambda: self.table_model_tab_populate() )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("table_model_\ntab_get_data")
        widget.clicked.connect(lambda: self.table_model_tab_get_data( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/\nunhide")
        widget.clicked.connect(lambda: self.table_model_hide_unhide( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/\nunhide column")
        widget.clicked.connect(lambda: self.table_model_toggle_hide_column( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        layout.addLayout( button_layout )
        widget        = QPushButton('table_model\n_inspect')
        widget.clicked.connect(self.table_model_inspect )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # -------------------------------------
    def table_model_tab_populate(self,   ):
        """
        what it says
            seems ok
        populates a row at a time
        """
        qt_widgets.print_func_header( "table_model_tab_populate" )

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
        once filter applied not sure how to remove
        this is messed up might want to start over with chat
        """
        qt_widgets.print_func_header( "table_model_hide_unhide !! fix me " )

        if self.table_model_filter:
            self.table_model_filter   = FilterProxyModelHideRows( )

    #-----------------------------------------------
    def double_clicked( self, index: QModelIndex):
        """
        what it says,
        index comes from table view
        """
        qt_widgets.print_func_header( "double_clicked" )

        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")
        #self.add_ix_other( row )

    #-----------------------------------------------
    def clicked( self, index: QModelIndex):
        """
        what it says,
        index comes from table view
        """
        qt_widgets.print_func_header( "clicked" )


        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")

        self.select_row( row )


    #-----------------------------------------------
    def select_row(self, row_index ):
         """Select a specific row."""

         qt_widgets.print_func_header( "select_row" )


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
        qt_widgets.print_func_header( "select_column" )

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
        qt_widgets.print_func_header( "table_model_toggle_hide_column" )


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
        print_func_header( "table_model_tab_get_data" )

        model           = self.table_model

        # !!table_model.model_dump( model )

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
        # ia_qt.q_abstract_table_model( self.table_model,   msg = "table_model_inspect" )
        print_func_header( "table_model_inspect" )

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
        print_func_header( "add_row_at_end" )

        row_position = self.table_widget_1.rowCount()
        self.table_widget_1.insertRow( row_position )

    # ------------------------------------------
    def remove_row_currrent(self):
        """
        may work needs to be hooked up
        """
        print_func_header( "remove_row_currrent" )

        row_position = self.table_widget_1.currentRow()
        self.table_widget_1.removeRow(row_position)

    # ------------------------------
    def set_size(self):
        """
        read it
        may work needs to be hooked up
        """
        print_func_header( "set_size" )

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
        print_func_header( "sort" )


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
        print_func_header( "on_cell_clicked" )

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
        print_func_header( "search" )

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
        print_func_header( "find_row_with_text" )

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
        print_func_header( "find_row_with_text_in_column !! fix me " )

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

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # self_q_pbutton_1    = self.q_pbutton_1
        # self_q_pbutton_2    = self.q_pbutton_2

        # self_qlabel_1       = self.qlabel_1
        # self_qlabel_2       = self.qlabel_2

        # #my_tab_widget = self
        # #parent_window = self.parent( ).parent( ).parent().parent()
        # local_self_text_edit  = self.qlabel_1
        wat_inspector.go(
             msg            = "tbd add more locals",
             a_locals       = locals(),
             a_globals      = globals(), )

        # print( "stuff to be moved !!")
        # msg   = f"{function_nl}inspect"
        # print( msg )
        # print( f"{ self.line_edit_1.text() = }" )  # setText()   ??
        # print( f"{ self.line_edit_1.isEnabled() = }" )  # setEnabled() no focus
        # print( f"{ self.line_edit_1.isReadOnly() = }" )

        # print( f"{ self.qlabel_1.text() = }" )  # setText() ??
        # print( f"{ self.qlabel_1.text() = }" )

        # print( f"{str( self.cbox_ex_1.isChecked()) = }" )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        qt_widgets.print_func_header( "breakpoint" )

        breakpoint()
