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



import inspect
#from   ex_qt import ia_qt
#import ia_qt
import subprocess
import sys
import time
#import datetime
from datetime import datetime
# import PyQt5.QtWidgets as qtw    #  qt widgets avoid so much import above
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
import qt_widgets
import utils_for_tabs as uft
import wat_inspector

# ---- imports neq qt












#wat_inspector    = wat.Wat( "joe")

# ---- end imports



# these must be defined at import time in uft
INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header




# INDENT        = uft.INDENT
# BEGIN_MARK_1  = uft.BEGIN_MARK_2
# BEGIN_MARK_2  = uft.BEGIN_MARK_2


# what          = Qt.AlignCenter   # valid alignment perhaps to addWidget   layout.addWidget
# #	addWidget(QWidget *widget, int stretch = 0, Qt::Alignment alignment = Qt::Alignment())
# note   = """
# main work example it WidgetExamplesInTabs

# Widget example with placer should be same with placer -- may have good salvage code
# same for the rest of the examples
# """


# ----------------------------
class GridLayoutTab( QWidget ) :
    def __init__(self):
        """
        the usual
            grid_layout_tab.GridLayoutTab
        """
        super().__init__()
        self._build_gui()

    # ----------------------------
    def _build_gui(self,   ):
        """
        the usual
        """

        tab_page      = self

        layout        = QGridLayout( tab_page )

        ix_row        = 1
        ix_col        = 0

        row_span      = 1 # default is 1
        col_span      = 1 # default is 1

        # rowSpan: (Optional) The number of rows the widget should span. Defaults to 1.
        # columnSpan: (Optional) The number of columns the widget should span. Defaults to 1.

        for ix_row  in range( 0, 6 ):
            for ix_col in range( 0,4 ):
                widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        for ix_row  in range( 0, 6, 2 ):
            for ix_col in range( 4, 6 ):
                row_span      = 2
                col_span      = 1
                widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        ix_row   += 2
        button_layout  = QHBoxLayout()
        layout.addLayout( button_layout, ix_row, 0, row_span, 6 )
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

        return tab_page

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection

        wat_inspector.go(
             msg            = "gridlayouttab",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof