#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:49:06 2024

@author: russ
"""
"""


qt_wat.py
qt_wat_app.py

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5 import QtGui

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QMainWindow
from PyQt5.QtWidgets import QGridLayout,   QVBoxLayout,   QButtonGroup
from PyQt5.QtWidgets import QWidget,       QLineEdit,     QLabel,      QTextEdit
from PyQt5.QtWidgets import QGroupBox,     QPushButton,   QMessageBox, QCheckBox, QRadioButton, QComboBox

from functools       import partial
import wat_inspector   # wat_setup

# ---- end imports


class MainWindow_1( QMainWindow ):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("QMainWindow")


        # Create central widget and grid layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Create buttons
        button1 = QPushButton("Button 1")
        self.button_1    = button1
        button2 = QPushButton("Button 2")
        button3 = QPushButton("call_wat_inspector")

        # Connect button signals to slots
        button1.clicked.connect(lambda: self.print_message(button1.text()))
        button2.clicked.connect(lambda: self.print_message(button2.text()))
        button3.clicked.connect( self.call_wat_inspector )

        # Create text entry fields and labels
        label1 = QLabel("Text Field 1:")
        label2 = QLabel("Text Field 2:")
        label3 = QLabel("Text Field 3:")
        text_field1 = QLineEdit()
        text_field2 = QLineEdit()
        text_field3 = QLineEdit()

        # Add widgets to the layout
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(label1, 1, 0)
        layout.addWidget(text_field1, 1, 1)
        layout.addWidget(label2, 2, 0)
        layout.addWidget(text_field2, 2, 1)
        layout.addWidget(label3, 3, 0)
        layout.addWidget(text_field3, 3, 1)

    # -------------------------------
    def print_message(self, text):
        """ """
        print("Button clicked:", text)

    # -------------------------------
    def call_wat_inspector(self,  ):
        """ """
        print("call_wat_inspector" )
        # wat_setup and go
        self_button_1     = self.button_1 # makds a local

        wat_inspector.go(
             msg            = "call_wat_inspector",
             inspect_me     = self,
             a_locals       = locals(),
             a_globals      = globals(), )


app         = QApplication(sys.argv)
dialog      = wat_inspector.DisplayWat( app )  # wat_setup
window = MainWindow_1()
window.show()
sys.exit(app.exec())