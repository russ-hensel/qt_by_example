# -*- coding: utf-8 -*-

""""
Purpose:
    object inspector
   /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/wat_inspector.py
   /home/russ/Desktop/Disks ( gnome-disks ).desktop
   /boot

Status:
    add check box for wat style
    button for original object
    get layout better
    append to wat.txt


    !! search ddlist but editable
    !! fix eval esp 2
    !! add to eval
    !! add a text help


See Also:


Search for the following in the code below:

    def ex_        for the beginning of an example


    ...

Reference:

wat-inspector · PyPI
https://pypi.org/project/wat-inspector/

GitHub - igrek51/wat: Deep inspection of Python objects
https://github.com/igrek51/wat

WAT Inspector - Nuclear
https://nuclear-py.readthedocs.io/en/master/inspect/

You can call wat.modifiers / foo with the following modifiers:

    .short or .s to hide the attributes (variables and methods inside the object)
    .dunder to display dunder attributes (starting with __)
    .code to reveal the source code of a function, method, or class
    .long to show non-abbreviated values and docstrings
    .nodocs to hide documentation for functions and classes
    .caller to show how and where the inspection was called (works in files, not REPL)
    .all to include all available information
    .ret to return the inspected object
    .str to return the output string instead of printing it
    .gray to disable colorful output in the console





"""

# ---- Imports

import adjust_path


# ---- imports neq qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QDialog
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QTextDocument

from PyQt5 import QtGui

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

import subprocess
from   subprocess import run
from   subprocess import Popen, PIPE, STDOUT

import io
import pprint
from   pprint import pprint as pp
import sys
import dis
import wat
import ex_helpers
import ex_helpers as ex_h
#import make_qt_object
from   subprocess import Popen
import traceback



wat_app        = None
go             = None    # dialog.setup_go
display_wat    = None



# ------------------------------------
class DisplayWat( QDialog ):
    """
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

# Your custom QDialog class
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Dialog Window")

        # Add a label to the dialog
        label = QLabel("This is the main dialog window.")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

# Main function to run the dialog
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the QApplication instance

    dialog = MyDialog()  # Create an instance of your custom QDialog
    dialog.show()  # Show the dialog as the main window

    sys.exit(app.exec_())  # Run the application's event loop


    """
    # ------------------------------------------
    def __init__(self,  app,  parent = None ):
        """
        Args:
            app app to run dialog

        Returns:
            None.

        """
        global    display_wat

        global    wat_app
        global    go

        if display_wat:
            return

        self.app       = app

        super().__init__( parent )

        display_wat = self
        wat_app     = app
        go          = self.setup_go


        self.parent         = parent  # parent may be a function use parent_window
        self.parent_window  = parent

        msg   = "Wat inspector"
        self.setWindowTitle( msg  )
        self.inspect_name   = None
        qt_xpos             = 50
        qt_ypos             = 50
        qt_width            = 1400
        qt_height           = 800
        self.tab_help_dictxxxxx   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )


        self._build_gui_grid()
        self.last_position = 0  # for search



    # ------------------------------------------
    def _build_gui_grid( self, ):
        """
        what it says, read?
        """
        layout          = QGridLayout( self )
        self.layout     = layout
        ix_row          = 0
        ix_col          = 0
        row_span        = 1
        col_span        = 1


        # ---- msg_label
        row_span        = 1
        col_span        = 1
        widget          = QLabel("Qlabel 1")
        self.msg_label  = widget
        #widget.setLayoutDirection( Qt.RightToLeft )
            # Qt.LeftToRight )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ----
        ix_col       += 1
        widget        = QPushButton( "What" )
        widget.clicked.connect(  self.what )
        # widget.toggled.connect( self.cbox_clicked )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ----
        ix_col       += 1
        widget        = QPushButton( "Where" )
        widget.clicked.connect(  self.where_am_i )
        # widget.toggled.connect( self.cbox_clicked )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ---- QCheckBox
        ix_col         += 1
        widget          =  QCheckBox("tbd")
        #self.cbox_ex_1  = widget
        #widget.animal   = "Cat"   # monkey patch ??
        widget.setChecked(True)
        # widget.toggled.connect( self.cbox_clicked )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ---- eval
        ix_row         += 1
        ix_col         = 0
        widget          =  QPushButton( "Eval" )
        widget.clicked.connect(         self.do_eval )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        #ix_row         += 1
        ix_col             += 1
        widget              =  QLineEdit( " 1 + 1 " )
        self.eval_widget    = widget
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )



        # ---- eval2
        ix_row          += 1
        ix_col          = 0
        widget          =  QPushButton( "Eval 2" )
        #widget.clicked.connect(         self.do_eval )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        #ix_row         += 1
        ix_col             += 1
        widget              =  QLineEdit( " 2 + 2 " )
        self.eval_widget_2  = widget
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # row_span            = 1
        # col_span            = 2
        # ix_row              += 1
        # ix_col              = 0

        row_span            = 1
        col_span            = 2
        ix_row              += 1
        ix_col              = 0

        widget              = QLabel( "Locals" )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        row_span            = 1
        col_span            = 2
        #ix_row              += 1
        ix_col              += 1

        widget              = QLabel( "Globals" )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ---- locals
        row_span            = 1
        col_span            = 2
        ix_row              += 1
        ix_col              = 0
        widget              = QListWidget(    )
        self.local_widget   = widget
        #widget.setGeometry( 50, 50, 200, 200 )
        widget.itemClicked.connect( self.do_inspect_clicked_local )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ---- globals
        row_span            = 1
        col_span            = 2
        #ix_row              += 1
        ix_col              += 1
        widget              = QListWidget(    )
        self.global_widget  = widget
        #widget.setGeometry( 50, 50, 200, 200 )
        widget.itemClicked.connect( self.do_inspect_clicked_global )
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        #widget.itemClicked.connect( self.activate_clicked_command )

        # values    =  [ "one", "two"]
        # for value in values:
        #     item = QListWidgetItem( value )
        #     widget.addItem( item )

        # ix_row        = 1
        # ix_col        = 0
        # row_span      = 2
        # col_span      = 1
        # ---- text_edit
        ix_row              += 1
        ix_col              = 0
        # Create QTextEdit widget
        text_edit           = QTextEdit()
        widget              = text_edit
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit      = text_edit
        layout.addWidget( widget, ix_row, ix_col, row_span, col_span )


        # ---- bottom and buttons





        ix_row                  += 1
        ix_col                  = 0
        button_layout           = QHBoxLayout()
        layout.addLayout( button_layout, ix_row, ix_col    )


        widget                  = QLineEdit()
        self.line_edit          = widget
        widget.setPlaceholderText("Enter search text")
        button_layout.addWidget( widget, )

        # Buttons
        widget                  = QPushButton("Down")
        self.down_button        = widget
        widget.clicked.connect(self.search_down)
        button_layout.addWidget( widget,   )

        widget           = QPushButton("Up")
        self.up_button   = widget
        widget.clicked.connect(self.search_up)
        button_layout.addWidget( widget,   )


        a_widget                = QPushButton("Save to File")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.write_file )
        button_layout.addWidget( a_widget )

        a_widget                = QPushButton("Edit File")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.edit_file )
        button_layout.addWidget( a_widget )

        a_widget                = QPushButton("Help")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.open_general_help )
        button_layout.addWidget( a_widget )

        a_widget                = QPushButton("OK")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.accept )
        button_layout.addWidget( a_widget )



    #-------
    def open_general_help( self,   ):
        """
        what it says read:

        """
        doc_name            =   "watt_inspector_help.txt"
        ex_editor          = r"xed"
        proc               = subprocess.Popen( [ ex_editor, doc_name ] )

    # ------------------------------------------
    def do_eval( self,    ):
        """
        what it says, read?
        """
        do_wat  = True
        code    =  self.eval_widget.text()
        try:
            result   = eval( code, self.globals,   self.locals )

        except Exception as an_except:   #  or( E1, E2 )

            msg     = f"a_except         >>{an_except}<<  type  >>{type( an_except)}<<"
            print( msg )

            msg     = f"an_except.args   >>{an_except.args}<<"
            print( msg )

            s_trace = traceback.format_exc()
            msg     = f"format-exc       >>{s_trace}<<"
            print( msg )

            result   = "got exception "
            do_wat   = False

        # finally:
        #     msg     = f"in finally  {1}"
        #     print( msg )

        if do_wat:
            self.inspect_object( result  )

        print( result )
        print( code )

    # ------------------------------------------
    def setup_go( self, inspect_me = None,
                 a_locals = None,
                 a_globals = None,
                 msg = "no message" ):
        """
        what it says, read?
        """
        if inspect_me is not None:
            msg    = f"argument inspect_me {inspect_me} is deleted and will be ignored"
            print( msg )
        self.msg_label.setText( msg )
        self.setup( None,  a_locals, a_globals   )
        #self.do_inspect( inspect_me )
        self.show()
        self.app.exec_()

    # ------------------------------------------
    def setup( self, inspect_me = None,  a_locals = None,  a_globals = None ):
        """
        what it says, read?
        """
        #self.inspect_me      = inspect_me
        # self.inspect_arg     = inspect_me  # later extend to list
        self.locals          = a_locals
        self.globals         = a_globals
        # pp( self.objects )
        # print( self.objects )
        # print( ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" )
        if a_locals:
            widget      = self.local_widget
            widget.clear()
            values      =  [ i_key for i_key in a_locals.keys() ]
            for value in values:
                item = QListWidgetItem( value )
                widget.addItem( item )
                index_to_select = 0
                widget.setCurrentRow( index_to_select )

        if a_globals:
            widget     = self.global_widget
            widget.clear()
            values    =  [ i_key for i_key in a_globals.keys() ]
            for value in values:
                item = QListWidgetItem( value )
                widget.addItem( item )
                index_to_select = 0
                widget.setCurrentRow(index_to_select)

        # self.what( )
        #self.do_inspect()

    # ------------------------------------------
    def do_inspect_clicked_global( self, item  ):
        """
        what it says, read?
        """
        widget              = self.global_widget
        row = widget.row( item )

        text               = item.text()
        i_object           = self.globals[ text ]
        print( "\n-------clicked")
        #print( f"{ type(i_key) = } { i_key = }")
        print( f"{text} {type(i_object) = } { i_object = }")
        print( f"do_inspect_clicked i_object { i_object = }   {type(i_object) = }")
        self._inspect_me    = i_object
        self.inspect_name  = text     # or pass as args use nonen...

        print(f"Clicked row: {row}, text: {text}")
        widget              = self.text_edit
        widget.clear()
        self.do_inspect( i_object )


    # ------------------------------------------
    def do_inspect_clicked_local( self, item  ):
        """
        what it says, read?
        """
        widget              = self.local_widget
        row = widget.row( item )

        text               = item.text()
        i_object           = self.locals[ text ]
        print( "\n-------clicked")
        #print( f"{ type(i_key) = } { i_key = }")
        print( f"{text} {type(i_object) = } { i_object = }")
        print( f"do_inspect_clicked i_object { i_object = }   {type(i_object) = }")
        self._inspect_me    = i_object
        self.inspect_name  = text     # or pass as args use nonen...

        print(f"Clicked row: {row}, text: {text}")
        widget              = self.text_edit
        widget.clear()
        self.do_inspect( i_object )

    #  --------
    def copy_all_text( self, text_edit ):
        """
        what it says
        from chat, test?
        """
        # Save current cursor position
        cursor = text_edit.textCursor()
        original_position = cursor.position()

        # Select all text and copy to the clipboard
        text_edit.selectAll()
        text_edit.copy()   # think goe to clipboard
        all_text = self.text_edit.toPlainText()

        # Restore cursor to its original position
        cursor.setPosition(original_position)
        text_edit.setTextCursor(cursor)
        return  all_text

    # ------------------------------------------
    def write_file( self,   ):
        """
        read it
        !! add the message and some seperation .. other stuff ?
        """
        my_text    = self.copy_all_text( self.text_edit )

        file_name  = "./wat_inspector_out.txt"
        with open( file_name, 'a') as a_file:    # a will append so file should be deleted time to time "w" will be for write no append ?
            a_file.write( my_text)     # f"{i_line}\n" )

    # ------------------------------------------
    def edit_file( self,   ):
        """
        read it
        import  wat_inspector    """
        file_name  = "./wat_inspector_out.txt"
        proc = Popen( [ "xed" , file_name ] )

    # ------------------------------------------
    def what( self ):
        print( """" Inspect the passed object """ )
        self.inspect_object( self.inspect_arg  )

    # ------------------------------------------
    def where_am_i( self ):
        """
        """
        print(f"where_am_i   {''}")
        widget              = self.text_edit
        widget.clear()
        debug               = get_traceback_list()
        ex_text             = "\n".join( get_traceback_list() )

        cursor              = widget.textCursor()

        #ex_text    = f"{self.inspect_name}: \n {ex_text}"

        cursor.insertText( ex_text )

    # ------------------------------------------
    def inspect_object( self, an_object  ):
        """
        what it says, read?
        output result to text_edit widget
        """

        print( "inspect_object >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #print( f"i_object { self.inspect_me = }   {type( self.inspect_me ) = }")
        widget              = self.text_edit
        widget.clear()
        #self.inspect_me     = inspect_me
        ex_text             = self.get_wat_str( an_object )
        cursor              = widget.textCursor()

        ex_text    = f"inspect_object { '' }: \n {ex_text}"

        cursor.insertText( ex_text )

        cursor.movePosition(QTextCursor.Start)   # .End
        widget.setTextCursor(cursor)


    # ------------------------------------------
    def do_inspect( self, what_object  ):
        """
        what it says, read?
        """

        print( "do_inspect >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print( f"i_object { what_object = }   {type( what_object ) = }")
        widget              = self.text_edit
        widget.clear()
        #self.inspect_me     = inspect_me
        ex_text             = self.get_wat_str( what_object )
        cursor              = widget.textCursor()

        ex_text    = f"{self.inspect_name}: \n {ex_text}"

        cursor.insertText( ex_text )

        cursor.movePosition(QTextCursor.Start)   # .End
        widget.setTextCursor(cursor)
        # print( "\n\n\n><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        # print( "ex_text[0:500" )
        # print( ex_text[0:500] )

    def get_wat_str( self,  obj, options_dict = None ):

        """ """
        msg      = wat( obj, str = True, gray = True )
        #msg      = repr( wat( obj, str = True ) )

        #msg      = self.get_wat_str_old(  obj )

        return msg
        #return  repr( wat( obj, str = True ) )
        #return  wat( obj, str = True )
        #return  self.get_wat_str_old(  obj )


    def get_wat_str_old( self,  obj, options_dictxxx = None ):
        """
        might want to get exception info if it occurs
        """
        options_dict = {}
        if True:
        #if options_dict:
            print( "options_dict implement me")
            #options_dict["code"] =  True
            options_dict["caller"] =  True

        captured_output     = io.StringIO()
        original_stdout     = sys.stdout

        try:
            sys.stdout      = captured_output
            #wat( obj, short = True )
            #wat( obj, all   = True )
            # wat( obj, code  = True, short = True )
            # wat( obj, code  = True, caller = True ) ng
            #wat( obj, **{ "code": True } )
            wat( obj, )
        finally:

            sys.stdout = original_stdout

        output_string = captured_output.getvalue()

        return output_string

    # ---------------------
    def search_down(self):
        """ """
        search_text = self.line_edit.text()
        if search_text:
            cursor = self.text_edit.textCursor()
            cursor.setPosition(self.last_position)
            found = self.text_edit.find(search_text)

            if found:
                self.last_position = self.text_edit.textCursor().position()
            else:
                # Reset position if end is reached and no match
                self.last_position = 0

    # ---------------------
    def search_up(self):
        search_text = self.line_edit.text()
        if search_text:
            cursor = self.text_edit.textCursor()
            cursor.setPosition( self.last_position )
            # Use QTextDocument.FindBackward for backward search
            found = self.text_edit.find(search_text, QTextDocument.FindBackward)

            if found:
                self.last_position = self.text_edit.textCursor().position()
            else:
                # Reset position if start is reached and no match
                self.last_position = self.text_edit.document().characterCount()


# -----------------
def ex_run_display_wat():
    ex_name  = "ex_run_display_wat"

    app         = QApplication( sys.argv )  # Create the QApplication instance
    dialog      = DisplayWat( app )  # Create an instance of your custom QDialog
    #dialog.setup_go( io, globals()  )


    go( dialog.do_eval  ,
             a_locals   = locals(),
             a_globals  = globals(),
             msg = "dialog.do_eval from the caller at go" )   # wat_inspector.go( io, globals() )

    # externally wat_inspector.go( io, globals() )
    # import wat_inspector as wi

    # io inspected object, globals, a dict of objects
    #dialog.show()  # Show the dialog as the main window
    #app.exec_()

    # #dialog  = DisplayWat()  # Create an instance of your custom QDialog
    # dialog.setup( io, globals()  )
    # dialog.do_inspect(   )
    # dialog.show()  # Show the dialog as the main window
    # app.exec_()
    # ---- run some more
    #dialog.setup_go( sys, locals()  )

    #dialog.setup_go( ex_helpers, None  )






# -----------------
def ex_inspect_fail():
    ex_name  = "ex_inspect"
    print( f"{ex_h.begin_example( ex_name )}"
            "\n        try to capture as a string, seems to fail "
            "\n\n" )

    # # ----------------------------------------
    # msg          = "  wat additiona inof"
    # code_string  = '  wat   '
    # ret  = ex_h.eval_and_print( msg          = msg,
    #                                   code         = code_string,
    #                                   as_locals    = locals(),
    #                                   as_globals   = globals(), )

    # a_string  = wat.str.short(  sys,   )
    # print( f"{a_string = }")

    # a_string  = wat.str.short( str = True,  sys,   )
    # print( f"{a_string = }")

    ret  = wat.short.str( wat )
    print( ret )
    # a_string  = wat.str.short(  sys,   )
    # a_string  = wat.str.short(  sys,   )

    ex_h.end_example( ex_name )

#ex_inspect()


#pprint.pprint( traceback.format_stack() )
def get_traceback_list( msg = "get_traceback_list", print_it = True ):
    """
    debug_util.get_traceback_list()

    Returns:
        short_list (TYPE): DESCRIPTION.

    """
    stop_text = "main.py"

    #stop_text  File "/mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/debug_util.py", line 171, in call_tbl

    keep = True
    short_list  = [">>>>>>>>>>>>>see what inspector instead get_traceback_list<<<<<<<<<<<<<<<<<<<<<<"]
    for i_item in reversed( traceback.format_stack() ):

        #print( i_item )

        if keep:
            short_list.append( i_item )

            if stop_text in i_item:
                print( "stop ---------------------------------------")
                keep = False
    short_list.append( msg )
    short_list.append( ">>>>>>>>>>>>>get_traceback_list<<<<<<<<<<<<<<<<<<<<<<" )

    short_list    = list( reversed( short_list ) )
    if print_it:
        for i_item in short_list:
            print( i_item )


    return short_list


def call_tbl():
    for i_item in get_traceback_list():
        print( i_item )


# --------------------
if __name__ == "__main__":
    #----- for running examples
    ex_run_display_wat()
# --------------------
    #call_tbl()

# ---- eof



"""
__name__:
 [0;34m────────────────────────────────────────────────────────────────────────────────[0m
[1;34mvalue:[0m [0;32m'__main__'[0m
[1;34mtype:[0m [0;33mstr[0m
[1;34mlen:[0m [0;31m8[0m

[1mPublic attributes:[0m
  [0;34mdef [1;32mcapitalize[0;32m()[0m [2;37m# Return a capitalized version of the string.…[0m[0m
  [0;34mdef [1;32mcasefold[0;32m()[0m [2;37m# Return a version of the string suitable for caseless comparisons.[0m[0m
  [0;34mdef [1;32mcenter[0;32m(width, fillchar=' ', /)[0m [2;37m# Return a centered string of length width.…[0m[0m
  [0;34mdef [1;32mcount[0;32m(…)[0m [2;37m# S.count(sub[, start[, end]]) -> int…[0m[0m
  [0;34mdef [1;32mencode[0;32m(encoding='utf-8', errors='strict')[0m [2;37m# Encode the string using the codec registered for encoding.…[0m[0m
  [0;34mdef [1;32mendswith[0;32m(…)[0m [2;37m# S.endswith(suffix[, start[, end]]) -> bool…[0m[0m
  [0;34mdef [1;32mexpandtabs[0;32m(tabsize=8)[0m [2;37m# Return a copy where all tab characters are expanded using spaces.…[0m[0m

repr

__name__:
 "\x1b[0;34m────────────────────────────────────────────────────────────────────────────────\x1b[0m\n\x1b[1;34mvalue:\x1b[0m \x1b[0;32m'__main__'\x1b[0m\n\x1b[1;34mtype:\x1b[0m \x1b[0;33mstr\x1b[0m\n\x1b[1;34mlen:\x1b[0m \x1b[0;31m8\x1b[0m\n\n\x1b[1mPublic attributes:\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mcapitalize\x1b[0;32m()\x1b[0m \x1b[2;37m# Return a capitalized version of the string.…\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mcasefold\x1b[0;32m()\x1b[0m \x1b[2;37m# Return a version of the string suitable for caseless comparisons.\x1b[0m\x1b[0m\

old

__name__:
 value: '__main__'
type: str
len: 8

Public attributes:
  def capitalize() # Return a capitalized version of the string.…
  def casefold() # Return a version of the string suitable for caseless comparisons.
  def center(width, fillchar=' ', /) # Return a centered string of length width.…



---------------








"""







