#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_widgets
    qt_widgets.main( )
# --------------------


import time
import wat
import wat_inspector



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
#from   ex_qt import ia_qt
#import ia_qt
import subprocess
from   subprocess import run
from   subprocess import Popen, PIPE, STDOUT
#import datetime
from   datetime import datetime

# import PyQt5.QtWidgets as qtw    #  qt widgets avoid so much import above
from   functools  import partial


import wat
import utils_for_tabs as uft
import qt_widgets
import parameters
#wat_inspector    = wat.Wat( "joe")

# ---- end imports


INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

# ----------------------------
class CustomDateEdit( QDateEdit ):
    """
    move a version to stuffdb
    custom_widget.pb   as CQDateEdit
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCalendarPopup(True)

        # Set an initial date (optional)
        self.setDate(QDate.currentDate())

    def contextMenuEvent(self, event):
        # Create the context menu
        context_menu = QMenu(self)

        # Add custom actions
        clear_action = QAction("Clear Date", self)
        today_action = QAction("Set to Today", self)

        # Connect actions to methods
        clear_action.triggered.connect(self.clear_date)
        today_action.triggered.connect(self.set_to_today)

        # Add actions to the menu
        context_menu.addAction(clear_action)
        context_menu.addAction(today_action)

        # Show the context menu
        context_menu.exec_(event.globalPos())

    def clear_date(self):
        self.clear()  # Clears the QDateEdit

    def set_to_today(self):
        self.setDate(QDate.currentDate())  # Sets date to today

#  --------
class QDateEditTab( QWidget ) :
    def __init__(self):
        """
        date_edit_tab.QDateEditTab

        """
        super().__init__()

        self.date_format   = "dd/MM/yyyy"

        self._build_gui()

    def _build_gui(self,   ):
        """
        the usual, build the gui
        """
        tab_page      = self
        layout        = QGridLayout( tab_page )
        button_layout = QHBoxLayout(   )

        ix_row        = 0
        ix_col        = 0

        widget  = QLabel( "start_date_widget w/o popup" )
        layout.addWidget( widget, ix_row, ix_col )   # row column alignment

        ix_col                  += 1
        #widget                  = QDateEdit()
        widget                  = CustomDateEdit()   # with context menu fro chat
        self.start_date_widget  = widget
        # widget.userDateChanged.connect( lambda: self.date_changed( ) )
        # widget.editingFinished.connect( lambda: self.date_changed( ) )
        #widget.setCalendarPopup( True )
        widget.setDate(QDate( 2022, 1, 1 ))
        layout.addWidget( widget, ix_row, ix_col )


        # ----
        ix_col    += 1
        widget  = QLabel( "end_date_widget -> (see _build_gui) ->" )
        layout.addWidget( widget, ix_row, ix_col )
        #placer.new_row()
        #placer.place( a_widget )

        """
           dateEdit->setSpecialValueText( " " );
           dateEdit->setDate( QDate::fromString( "01/01/0001", "dd/MM/yyyy" ) );
        """
        ix_col                  += 1
        widget                  = QDateEdit()
        self.end_date_widget    = widget
        widget.setCalendarPopup( True )
        widget.setDate(QDate( 2025, 1, 1 ))
        widget.setMinimumDate(QDate(1900, 1, 1))
        widget.setMaximumDate(QDate(2100, 12, 31))
        widget.setDisplayFormat( self.date_format )   # = "dd/MM/yyyy"
        widget.setSpecialValueText( " " )    # this will then reepor minimun date
        invalid_date            = QDate().fromString( "01/01/0001", self.date_format )
        widget.setDate( invalid_date )
        #widget.setDate(QDate( None, None, None, )) not ok
        widget.editingFinished.connect( lambda: self.date_changed(   ) )
        #placer.place( a_widget )
        layout.addWidget( widget, ix_row, ix_col )

        # ----- QDateTimeEdit
        ix_row                  += 1
        ix_col                  =0
        # Create a QDateTimeEdit widget
        widget            = QDateTimeEdit( )
        self.dateTimeEdit = widget

        # Set a default date/time
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        widget.setCalendarPopup(True)

        self.dateTimeEdit.setGeometry(50, 50, 200, 30)

        layout.addWidget( widget, ix_row, ix_col )

        # ---- QTimeEdit


        ix_row                  += 1
        ix_col                  =0
        # Create a QTimeEdit widget
        widget          = QTimeEdit( self )
        self.timeEdit   = widget


        # Set a default time -- some error here
        #self.timeEdit.setTime( QTime.currentTime() )

        # Set a custom display format
        self.timeEdit.setDisplayFormat("HH:mm:ss")

        # Set the widget geometry
        self.timeEdit.setGeometry(50, 50, 150, 30)

        widget.setDisplayFormat("HH:mm")

        # Show hours, minutes, and seconds (24-hour format)
        widget.setDisplayFormat("HH:mm:ss")
        widget.setDisplayFormat("hh:mm:ss AP")


        widget.setMinimumTime(QTime(8, 0, 0))
        widget.setMaximumTime(QTime(18, 0, 0))

        # Set the time step to 15 minutes
        #widget.setSingleStep( 15 )   # fails

        # Enable time wrapping
        widget.setWrapping(True)

        # Enable keyboard tracking to update immediately
        widget.setKeyboardTracking(True)

        # Clear the time edit field
        widget.clear()

        layout.addWidget( widget, ix_row, ix_col )

        # ---- buttons ---------------------------------
        ix_row    += 1
        ix_col    = 0
        layout.addLayout( button_layout, ix_row, ix_col )

        # # ---- Inspect
        # widget = QPushButton("inspect")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # a_widget        = widget
        # widget.clicked.connect( lambda: self.inspect( ) )
        # button_layout.addWidget( widget )

        # ---- mutate
        widget = QPushButton("mutate\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( self.mutate )
        button_layout.addWidget( widget )

        # ----set_empty
        widget = QPushButton("set_empty\n")
        widget.clicked.connect(lambda: self.set_empty( ))
        a_widget        = widget
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )

    # ------------------------------------
    def set_empty( self ):
        """
        what is says
        """
        print_func_header( "set_empty" )

        invalid_date     = QDate().fromString( "01/01/0001", "dd/MM/yyyy" )
        self.end_date_widget.setDate( invalid_date )

    # ------------------------------------
    def to_unix( self, qdate, ): # date_format = None ):
        """
        read it
        need a begin of day and an end of day this is end i think
        from chat
        """
        """
        what is says
        """
        print_func_header( "to_unix" )

        # from PyQt5.QtCore import QDate, QDateTime

        # # Example QDate object
        # qdate = QDate(2024, 9, 16)

        # # Convert QDate to QDateTime (time will be set to 00:00:00 by default)
        qdatetime       = QDateTime( qdate )

        # Get the Unix timestamp (seconds since epoch)
        unix_timestamp  = qdatetime.toSecsSinceEpoch()

        print(f"QDate: {qdate}")
        print(f"Unix Timestamp: {unix_timestamp}")

        return unix_timestamp

    # ------------------------------------
    def mutate( self ):
        """
        read it
        some conversions from chat



        I have a QDateEdit i get the qdate from it.
        I want to convert the qdate to a unit time, the last
        second of the date,

        and second I want to convert the date to
        the first second of the date,

        and finally i want to convert
        the date to the last second of the day before the date.

        Assume the date and times are GMT



        """
        print_func_header( "mutate" )

        # Convert to QDateTime
        qdatetime       = QDateTime.fromSecsSinceEpoch( int( time.time() ) )
        qdate           = qdatetime.date()

        self.start_date_widget.setDate( qdate  )

    # ------------------------------------
    def inspect_old( self ):
        """
        read it
        some conversions from chat

        I have a QDateEdit i get the qdate from it.
        I want to convert the qdate to a unit time, the last
        second of the date,

        and second I want to convert the date to
        the first second of the date,

        and finally i want to convert
        the date to the last second of the day before the date.

        Assume the date and times are GMT

        """
        print( "\n\n---------------------------------------")
        print( f"w/o popup  {self.start_date_widget.date() = }" )  # setText()   ??
        print( f"w   popup  {self.end_date_widget.date() = }" )  # setText()   ??
        a_date            = self.end_date_widget.date()

        unix_time_stamp   = self.to_unix( a_date,   )
        print( f"w   popup   self.end_date_widget.date() ={ unix_time_stamp }" )
        # from PyQt5.QtCore import QDateTime

        # # Example Unix timestamp (for September 16, 2024, 00:00:00)
        # unix_timestamp = 1726444800

        # Convert Unix timestamp to QDateTime
        qdatetime         = QDateTime.fromSecsSinceEpoch( unix_time_stamp )

        # Output the result
        print(f"Unix Timestamp: {unix_time_stamp}")
        print(f"QDateTime: {qdatetime.toString('yyyy-MM-dd hh:mm:ss')}")


        # Convert to QDateTime
        # qdatetime = QDateTime.fromSecsSinceEpoch(timestamp, Qt.UTC)

        print(f"QDateTime: {qdatetime.toString(Qt.ISODate)}")


        # Extract QDate from the QDateTime
        qdate = qdatetime.date()

        print(f"QDate: {qdate.toString(Qt.ISODate)}")



    def qdate_to_unix_last_second( self, qdate):
        """ Convert QDate to Unix timestamp for the last second of the day (23:59:59) """
        qdatetime = QDateTime(qdate, QDateTime().time().fromString("23:59:59", "hh:mm:ss"), Qt.UTC)
        unix_time = qdatetime.toSecsSinceEpoch()  # Get Unix timestamp in seconds
        return unix_time

    def qdate_to_unix_first_second(self, qdate):
        """ Convert QDate to Unix timestamp for the first second of the day (00:00:00) """
        qdatetime = QDateTime(qdate, QDateTime().time().fromString("00:00:00", "hh:mm:ss"), Qt.UTC)
        unix_time = qdatetime.toSecsSinceEpoch()  # Get Unix timestamp in seconds
        return unix_time

    def qdate_to_unix_last_second_previous_day(self, qdate):
        """ Convert QDate to Unix timestamp for the last second of the previous day (23:59:59) """
        qdate_previous = qdate.addDays(-1)  # Get the previous day
        qdatetime = QDateTime(qdate_previous, QDateTime().time().fromString("23:59:59", "hh:mm:ss"), Qt.UTC)
        unix_time = qdatetime.toSecsSinceEpoch()  # Get Unix timestamp in seconds
        return unix_time

    # --------
    def date_changed( self, arg ):
        """

        """
        """
        what is says
        """
        print_func_header( "date_changed" )

        print( f"{arg = }")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        my_tab_widget               = self
        self_start_date_widget      = self.start_date_widget
        self_timeEdit               = self.timeEdit
        wat_inspector.go(
             msg            = "from inspect method !! needs more locals",
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
