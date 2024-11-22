#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
based on
... /book_pyqt5_src/basic/widgets_2c.py
"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_fitz_book
    qt_fitz_book.main()
# --------------------



import time
import os


# ---- imports neq qt

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QSizePolicy
from PyQt5.QtCore import QDate, Qt,  QSize
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtGui
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow, QTimeEdit
from PyQt5.QtCore import QTime

from PyQt5.QtGui import QPixmap


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

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
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


# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class Fitz_2_Tab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_misc_widgets.py
        """
        super().__init__()
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        added some size control
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ---- fitz code here

        basedir = os.path.dirname(__file__)


        widget = QLabel("Hello")

        # # tag::scaledContents[]
        widget.setPixmap( QPixmap( "a_cat.jpg" ) )
        widget.setPixmap( QPixmap( "bird_house.jpg" ))

        # for some photos you may loose control of size this whould fix
        widget.setMinimumSize( 100, 75)  # Minimum width: 100px, Minimum height: 75px
        widget.setMaximumSize( 400, 300)  # Maximum width: 400px, Maximum height: 300px

        #widget.setPixmap( QPixmap( "otjex.jpg" ) )
        #widget.setPixmap( QPixmap(os.path.join( basedir, "a_cat.jpg")) )
        widget.setScaledContents(True)
        # widget.setGeometry( 50, 50, 50, 50 ) #
        layout.addWidget( widget )

        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_widgets_list   = self.widgets_list
        wat_inspector.go(
             msg            = "see self_widgets_list",
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