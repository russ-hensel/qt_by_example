#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:42:11 2024

@author: russ

        #self.setIcon( QMessageBox.Warning) #

def button_clicked(self, s):
print("click", s)
dlg = QDialog(self)   # where save is the main window see m fitx
dlg.setWindowTitle("HELLO!")
dlg.exec_()    # yes we do it again
# end::MainWindow[]


"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_widgets
    qt_widgets.main( )
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


import wat
import utils_for_tabs as uft
import qt_widgets
import parameters

import wat_inspector

# ---- end imports


INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header


#  --------
class DialogEtcTab( QWidget ) :
    def __init__(self):
        """
        q_dialog_etc_tab.py
        """
        super().__init__()
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box f or each row
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ---- New Row
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )



        # row_layout      = QHBoxLayout(   )
        # layout.addLayout( row_layout )

        # widget          = QLabel("cbox_1 - 3-> ")
        # row_layout.addWidget( widget )

        # widget          = QCheckBox( "cbox_1 label"  )
        # self.cbox_1     = widget
        # widget.setChecked(True)
        # widget.toggled.connect( self.cbox_clicked )
        # row_layout.addWidget( widget, stretch = 0 )

        # widget          = QCheckBox( "cbox_2 label"  )
        # self.cbox_2     = widget
        # widget.setChecked(True)
        # widget.toggled.connect( self.cbox_clicked )
        # row_layout.addWidget( widget, stretch = 0 )

        # widget          = QCheckBox( "cbox_3 label"  )
        # self.cbox_3     = widget
        # widget.setChecked(True)
        # widget.toggled.connect( self.cbox_clicked )
        # row_layout.addWidget( widget, stretch = 0 )

        # ---- QPushButton("Open Messagebox")
        widget          = QPushButton("show_message\n_box")
        widget.setCheckable(True)
        widget.clicked.connect( lambda: self.show_message_box( ) )
        row_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )

    # ------------------------------------
    def show_message_box( self ):
        """
        what is says
        """
        print_func_header( "show_message_box" )

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Make a Choice")
        msg_box.setText("Please choose one:")

        # Adding buttons
        choice_a = msg_box.addButton("Choice A", QMessageBox.ActionRole)
        choice_b = msg_box.addButton("Choice B", QMessageBox.ActionRole)

        # Set the dialog to be modal (blocks interaction with other windows)
        msg_box.setModal(True)

        # Execute the message box and wait for a response
        msg_box.exec_()

        if msg_box.clickedButton() == choice_a:
            print("Choice A selected")
        elif msg_box.clickedButton() == choice_b:
            print("Choice B selected")

        QMessageBox.information( self, "Deput_in_clipboardlete Ok", "detail_text_model Record deleted successfully.")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # self_q_pbutton_1    = self.q_pbutton_1
        # self_q_pbutton_2    = self.q_pbutton_2

        wat_inspector.go(
             msg            = "tbd add more locals",
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




