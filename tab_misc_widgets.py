#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_widgets
    qt_widgets.main()
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















# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class MiscWidgetTab( QWidget ) :
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
        layouts
            a vbox for main layout
            h_box f or each row
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # # ---- filler_label
        # row_layout    = QHBoxLayout(   )
        # layout.addLayout( row_layout )

        # widget          = QLabel("filler_label -> ")
        # row_layout.addWidget( widget )

        # widget          = QLabel("filler")
        # #self.qlabel_1   = widget
        # widget.setLayoutDirection( Qt.RightToLeft )
        # #widget.setLayoutDirection( Qt.LeftToRight )
        # row_layout.addWidget( widget )

        # ---- New row colored_filler
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel( "colored_filler -> " )
        self.qlabel_1   = widget
        row_layout.addWidget( widget )

        widget          =  uft.ColoredFiller('red')
        self.qwidget_1  = widget
        row_layout.addWidget( widget )

        # ---- New Row button_1 and _2
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel( "q_pbutton_1 -> " )
        self.qlabel_1   = widget
        row_layout.addWidget( widget )

        widget              = QPushButton( "q_pbutton_1" )
        self.q_pbutton_1    = widget
        connect_to          = self.pb_1_clicked
        widget.clicked.connect( connect_to    )
        row_layout.addWidget( widget )

        widget              = QLabel("q_pbutton_2 -> ")
        row_layout.addWidget( widget )

        widget              = QPushButton( "q_pbutton_2" )
        self.q_pbutton_2    = widget
        connect_to          = self.pb_2_clicked
        widget.clicked.connect( connect_to    )
        row_layout.addWidget( widget,  )

        # ---- qlabel_1 an _2
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel("qlabel_1 -> ")
        row_layout.addWidget( widget )

        widget          = QLabel("qlabel_1")
        self.qlabel_1   = widget
        #widget.setLayoutDirection( Qt.RightToLeft )
        #widget.setLayoutDirection( Qt.LeftToRight )
        row_layout.addWidget( widget )

        # ---- qlabel_2
        widget          = QLabel("qlabel_2 -> ")
        row_layout.addWidget( widget )

        widget          = QLabel("qlabel_2 text")
        self.qlabel_2   = widget
        row_layout.addWidget( widget )
        #widget.setLayoutDirection( Qt.RightToLeft )
        #widget.setText( "change original text ..........." )
        #widget.setLayoutDirection( Qt.LeftToRight )
        #layout.addWidget( widget )
        #row_layout.addWidget( widget, Qt.AlignmentFlag.AlignRight )

        # ---- QCheckBoxs
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel("cbox_1 - 3-> ")
        row_layout.addWidget( widget )

        widget          = QCheckBox( "cbox_1 label"  )
        self.cbox_1     = widget
        widget.setChecked(True)
        widget.toggled.connect( self.cbox_clicked )
        row_layout.addWidget( widget, stretch = 0 )

        widget          = QCheckBox( "cbox_2 label"  )
        self.cbox_2     = widget
        widget.setChecked(True)
        widget.toggled.connect( self.cbox_clicked )
        row_layout.addWidget( widget, stretch = 0 )

        widget          = QCheckBox( "cbox_3 label"  )
        self.cbox_3     = widget
        widget.setChecked(True)
        widget.toggled.connect( self.cbox_clicked )
        row_layout.addWidget( widget, stretch = 0 )

        # ---- QLineEdit 1
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel("line_edit_1 -> ")
        row_layout.addWidget( widget )

        widget            = QLineEdit()
        self.line_edit_1  = widget
        widget.setText( "QLineEdit use setText to set value disabled? on second line?")
            #\n does not give second line
        widget.setDisabled( True )
        widget.setDisabled( False )
        widget.setPlaceholderText( "Enter your text here" )  # clear to see
        widget.textChanged.connect( self.on_text_changed ) # user or pro grammatically
        widget.textEdited.connect(self.on_text_edited)  # user only
        widget.editingFinished.connect(self.on_editing_finished) # done leaves control
        widget.setReadOnly(True)
        widget.setReadOnly(False)
        row_layout.addWidget( widget )

        # ---- QLineEdit 2
        widget          = QLabel("line_edit_2 -> ")
        row_layout.addWidget( widget )

        widget              = QLineEdit()
        self.line_edit_2    = widget
        widget.setText( "line_edit_2")
        widget.textChanged.connect(      lambda: self.signal_sent(  "textChanged"   ) )
        widget.editingFinished.connect(  lambda: self.signal_sent( "editingFinished"  ) )
            #\n does not give second line
        #widget.setDisabled( True )
        # no errors from these but do not seem effective
        widget.setLayoutDirection( Qt.RightToLeft )
        widget.setLayoutDirection( Qt.LeftToRight )
        row_layout.addWidget( widget )

        # ---- new row QRadioButtons
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel("radio_buttons 1-3 -> ")
        row_layout.addWidget( widget )

        widget        = QRadioButton("rb_1")
        self.rb_1     = widget
        row_layout.addWidget( widget )

        widget        = QRadioButton("rb_2")
        self.rb_2     = widget
        row_layout.addWidget( widget )

        widget        = QRadioButton("rb_3")
        self.rb_3    = widget
        row_layout.addWidget( widget )

        # widget        = QRadioButton("rb_1")
        # self.rb_1     = widget
        # #radiobutton   = QRadioButton("AUSTRALIA")
        # widget = QRadioButton('Left-Text Radio Button')
        # widget.setChecked(True)  # Set as default selected
        # widget.setLayoutDirection( Qt.RightToLeft )  # Set text layout direction to right-to-left textOnLeft
        # widget.setLayoutDirection( Qt.LeftToRight )
        # row_layout.addWidget( widget )

        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        self.button_ex_1         = widget

        widget = QPushButton("show_\nvalues")
        self.button_ex_1         = widget
        widget.clicked.connect(  self.show_values )
        button_layout.addWidget( widget )


        widget = QPushButton("mutate\n")
        self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

        widget = QPushButton("clear_\nvalues")
        a_widget        = widget
        widget.clicked.connect(  self.clear_values  )
        button_layout.addWidget( widget )

        widget = QPushButton("set_values\n")
        widget.clicked.connect( lambda: self.set_values( ) )
        button_layout.addWidget( widget )

        widget = QPushButton("clip\n")
        widget.clicked.connect( lambda: self.clip( ) )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    def get_button_style_sheet( self ):
        """
        what it says
        """
        return ("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    # ------------------------------------
    def mutate( self ):
        """
        what is says
            mutate the widgets
            considerbutt
                change the label text
        """
        print_func_header( "mutate" )

        print( "\n\nmutate does not do much yet work in progress ")

        if ( self.mutate_ix % 2 )  == 0:
            self.q_pbutton_1.setStyleSheet( self.get_button_style_sheet() )
        else:
            self.q_pbutton_1.setStyleSheet( "" )
        self.mutate_ix += 1

    # ------------------------------------
    def signal_sent( self, msg ):
        """
        when a signal is sent, use find
        """
        print_func_header( "signal_sent" )
        # msg   = f"{function_nl}signal_sent"
        # print( msg )
        print( f"signal_sent {msg}" )

    # ------------------------------------
    def put_in_clipboard( self, a_string ):
        """
        what it says:
        """
        print_func_header( "put_in_clipboard" )

        clipboard = QApplication.clipboard()

        # Set a string into the clipboard
        clipboard.setText( a_string )
        print( f"put_in_clipboard { a_string = }" )

        get_text_out   =   clipboard.text()

    # ------------------------------------
    def clear_values( self ):
        """
        There is much more info to show
        """
        print_func_header( "clear_values" )

        print( "\n\nclear_values")
        print( "clear_values self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??

    # ------------------------------------
    def set_values( self ):
        """
        What it says
        """
        print_func_header( "set_values" )

        print( "set_values  self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "xxxxx" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??

    # ------------------------------------
    def pb_1_clicked( self ):
        """
        What it says
        """
        print_func_header( "pb_1_clicked" )

    # ------------------------------------
    def pb_2_clicked( self ):
        """
        What it says
        """
        print_func_header( "pb_2_clicked" )


    # --------
    def clip( self ):
        """
        """
        print_func_header( "clip" )

        a_string    = self.line_edit_1.text()
        self.put_in_clipboard( a_string )

    # --------
    def cbox_clicked( self ):
        """
        """
        print_func_header( "cbox_clicked" )

        cbox = self.sender()   # look into self.sender() looks like it might be standard !!

        print( f"check box text() = { cbox.text()} ")

    # ---- signals sent -----------------------
    # --------------------------
    def on_editing_finished(self):
        """
        what is says
        """
        print_func_header( "on_editing_finished" )

        print("Editing finished")

    # ------------------------------------
    def on_text_changed( self, new_text):
        """
        what is says
        """
        print_func_header( "on_text_changed" )

        print(f"Text changed: {new_text}")

    # ------------------------------------
    def on_text_edited(self, new_text):
        """
        what is says
        """
        print_func_header( "on_text_edited" )

        print(f"User edited text: {new_text}")

    # ------------------------
    def show_values(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        print( f"{self.qwidget_1 = }")
        #print( f"{self.qwidget_1 = }")


        print( f"{self.line_edit_1.text() = }" )  # setText()   ??
        print( f"{self.line_edit_1.isEnabled() = }" )  # setEnabled() no focus
        print( f"{self.line_edit_1.isReadOnly() = }" )

        print( f"{self.qlabel_1.text() = }" )  # setText() ??
        print( f"{self.qlabel_2.text() = }" )

        print( f"{str(self.cbox_1.isChecked()) = }" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_q_pbutton_1    = self.q_pbutton_1
        self_q_pbutton_2    = self.q_pbutton_2

        self_qlabel_1       = self.qlabel_1
        self_qlabel_2       = self.qlabel_2

        self_line_edit_1  = self.line_edit_1
        self_line_edit_2  = self.line_edit_2

        self_qwidget_1      = self.qwidget_1

        #my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()

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


# ---- eof
