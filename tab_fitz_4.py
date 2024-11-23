#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 "/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_1.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_1b.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_2.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_3.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_4.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_5.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_6.py"

largely the last


"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_fitz_book
    qt_fitz_book.main()
# --------------------


import inspect
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QAbstractListModel,
                          QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QImage, QPalette, QTextCursor, QTextDocument
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
                             QDial,
                             QDoubleSpinBox,
                             QFontComboBox,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLCDNumber,
                             QLineEdit,
                             QListView,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QProgressBar,
                             QPushButton,
                             QRadioButton,
                             QSizePolicy,
                             QSlider,
                             QSpinBox,
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



















# ---- end imports

print_func_header   = uft.print_func_header

basedir = os.path.dirname(__file__)

tick = QImage(os.path.join("tick.png"))


class TodoModel( QAbstractListModel ):
    def __init__(self, *args, todos=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)






#  --------
class Fitz_4_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )


        # # ---- TodoModel
        # widget = TodoModel( )
        # layout.addWidget( widget,   )

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        self.model      = TodoModel()

        widget          = QListView()
        self.todoView   = widget
        self.todoView.setModel(self.model)
        row_layout.addWidget( widget,   )

        # ---- new row,
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- PB
        widget = QPushButton("delete\n")
        widget.clicked.connect( self.delete   )
        button_layout.addWidget( widget,   )


        # ---- PB
        widget = QPushButton("complete\n")
        widget.clicked.connect( self.complete    )
        button_layout.addWidget( widget,   )

        # ---- new row,
        row_layout = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ---- Line Edit
        widget = QLineEdit("new items here")
        self.todoEdit  = widget
        #widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )



        # ---- new row,
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- "add\n_todo"
        widget = QPushButton("add\n_todo")
        widget.clicked.connect( self.add    )
        button_layout.addWidget( widget,   )

        # ---- new row,
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )


        # ---- PB inspect
        widget = QPushButton("load\n")
        widget.clicked.connect( self.load    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("save\n")
        widget.clicked.connect( self.save    )
        button_layout.addWidget( widget,   )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        print_func_header( "add" )

        text = self.todoEdit.text()
        # Remove whitespace from the ends of the string.
        text = text.strip()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()  # <1>
            # Empty the input
            self.todoEdit.setText("")

    def delete(self):
        """ """
        print_func_header( "delete" )

        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()

    def complete(self):
        """ """
        print_func_header( "complete" )

        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()

    # tag::loadsave[]
    def load(self):
        print_func_header( "load" )

        try:
            with open("data.json", "r") as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

        self.model.layoutChanged.emit() # This triggers a refresh of the entirety of the view. I


    def save(self):
        print_func_header( "save" )

        with open("data.json", "w") as f:
            data = json.dump(self.model.todos, f)


    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_model         = self.model
        self_todo_view     = self.todoView

        wat_inspector.go(
             msg            = "locals for model and view",
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
