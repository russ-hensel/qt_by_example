"""

Examples of




"""
# ---- top/search
""""
    Search for the following in the code below:






    See Also:

    Links



"""


# ---- imports

import inspect
import os
import sqlite3 as lite
import subprocess
import sys
from functools import partial
from platform import python_version
from subprocess import PIPE, STDOUT, Popen, run

#from app_global import AppGlobal
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QModelIndex,
                          QSize,
                          QSortFilterProxyModel,
                          Qt,
                          QTimer)
# sql
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlField,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)

from PyQt5.QtWidgets import (QAbstractItemView,
                             QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDataWidgetMapper,
                             QDateEdit,
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
                             QSpinBox,
                             QStyledItemDelegate,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

import parameters
import qt_table_model
import tab_fitz_1
import tab_fitz_2
import tab_fitz_3
import tab_fitz_4
import tab_fitz_5
import tab_fitz_6
import utils_for_tabs as uft
import wat_inspector

# ---- end imports


basedir         = os.path.dirname(__file__)


INDENT          = uft.INDENT
BEGIN_MARK_1    = uft.BEGIN_MARK_2
BEGIN_MARK_2    = uft.BEGIN_MARK_2

print_func_header  = uft.print_func_header


# ---- main window ===================================================================
class QtBookExamples( QMainWindow ):
    def __init__(self):
        """
        Code derived from M Fitz book
        """
        super().__init__()

        my_parameters       = parameters.Parameters()
        self.parameters     = my_parameters

        qt_xpos     = my_parameters.qt_xpos
        qt_ypos     = my_parameters.qt_ypos
        qt_width    = my_parameters.qt_width
        qt_height   = my_parameters.qt_height

        uft.TEXT_EDITOR     = my_parameters.text_editor
        # opened on right hand monitor
        # qt_xpos     = 10
        # qt_ypos     = 10
        # qt_width    = 3000
        # qt_height   = 600

        # # opens on main monitor
        # qt_xpos     = 10
        # qt_ypos     = 10
        # qt_width    = 1400
        # qt_height   = 700

        self.tab_help_dict   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )
        self.doc_dir             = "./docs/"
        self.build_gui()
        self.current_tab_index   = 0   # I need to track in changed

    # ------------------
    def build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( "QtBookExamples" )

        #self.setWindowIcon( QtGui.QIcon('clipboard_b_red_gimp.ico') )
        self.setWindowIcon( QtGui.QIcon( './designer.png' ) )  # cannot get this to work

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout  =  QVBoxLayout( central_widget )

        # --- out main layout
        layout      = QVBoxLayout(   )
        central_widget_layout.addLayout( layout )

        self.build_menu( )

        # ---- Create tabs
        self.tab_widget = QTabWidget()   # really the folder for the tabs
                                         # tabs themselves are just Widgets

        # Set custom height for the tabs
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 60px; }")

        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        self.tab_widget.tabBarClicked.connect( self.on_tab_clicked)

        self.tab_widget.tabCloseRequested.connect( self.on_tab_close_requested)
        self.tab_widget.setTabsClosable( False )
            # Allows you to enable or disable the close button on tabs.
        self.tab_widget.setMovable( True )
            # what it says

        layout.addWidget( self.tab_widget   )

        title    = "Many\nWidgets"
        tab      = tab_fitz_1.Fitz_1_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_1_tab.txt"

        title    = "Label\nwith Image"
        tab      = tab_fitz_2.Fitz_2_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_2_tab.txt"

        title    = "Mouse\nContext Menu"
        tab      = tab_fitz_3.Fitz_3_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_3_tab.txt"

        title    = "ToDo\nList"
        tab      = tab_fitz_4.Fitz_4_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_4_tab.txt"

        title    = "Graph\nDynamic"
        tab      = tab_fitz_5.Fitz_5_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_5_tab.txt"

        title    = "Graph\nStatic"
        tab      = tab_fitz_6.Fitz_6_Tab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "fitz_5_tab.txt" # share with 5 for awhild




        # title    = "QList\n"
        # tab      = tab_qlist.QListWidgetTab()
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "list_widget_tab.txt"





    # ------------------------------------
    def build_menu( self,  ):
        """
        what it says:
        """
        menubar         = self.menuBar()
        self.menubar    = menubar

        # a_menu.addSeparator()

        # ---- Help
        menu_help       = menubar.addMenu( "Help" )

        action          = QAction( "README.md...", self )
        connect_to      = partial( self.open_txt_file, "README.md" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "General Help...", self )
        connect_to      = partial( self.open_txt_file, "./docs/general_help.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Guide to QT Book Examples...", self )
        connect_to      = partial( self.open_txt_file, "./docs/guide_to_qt_book_examples.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Current Tab Help...", self )
        connect_to      = self.open_tab_help
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Developer Notes...", self )
        connect_to      = partial( self.open_txt_file, "readme_rsh.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

    #----------------------------
    def not_implemented( self,   ):
        """
        what it says read:
        """
        QMessageBox.information(self, "Not Implemented", "Working on this...")

    #----------------------------
    def inspect_mutate_not_conndected ( self,   ):
        """
        what it says read:
        """
        uft.print_func_header( "inspect......" )
        index = self.tab_widget.currentIndex()
        self.tab_widget.setCurrentIndex(2)  # Set the active tab by index

        text = self.tab_widget.tabText(0)  # Get the label of the first tab
        self.tab_widget.setTabText(0, "New Label")  # Set a new label

    #-------
    def open_general_help( self,   ):
        """
        what it says read:
        """
        doc_name            = f"{self.doc_dir}qt_widgets_help.txt"
        ex_editor           = r"xed"
        proc                = subprocess.Popen( [ ex_editor, doc_name ] )

    # ---- events ------------------------------------------
    #----------------------------
    def on_tab_changed(self, index):
        """
        what it says, read it
        """

        #print(f"on_tab_changed from { self.current_tab_index = } to {index = }")
        self.current_tab_index   = index
        self.tab_page_info()

    #----------------------------
    def on_tab_close_requested( self, index):
        self.tab_widget.removeTab(index)

    #----------------------------
    def on_tab_clicked(self, index):
        print(f"Tab {index} clicked.")

    #----------------------------
    def tab_page_info( self ):
        """
        what it says, read it
        """
        nb    = self.tab_widget
        print(f"nb.select()  >>{nb.currentIndex() = }<<")
        print(f'>>{nb.tabText(nb.currentIndex()) = }<<')
        # print(f'{ nb.index("current" ) = }' )

    # ----
    def iconify( self ):
        """
        what it says
        """
        self.showMinimized()   # for minimizing your window

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
        """
        tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
        doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        doc_name            = f"{self.doc_dir}{doc_name}"
        print( f"{doc_name = }")

        self.open_txt_file( doc_name )

    #-------
    def open_txt_file( self, file_name  ):
        """
        what it says read
        """
        proc               = subprocess.Popen( [ uft.TEXT_EDITOR, file_name ] )

# -----------------------------------
def main():
    """
    yes this is the main app
    """
    app                 = QApplication( [] )
    #dialog          = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog
    a_wat_inspector     = wat_inspector.WatInspector( app )
    window              = QtBookExamples()
    window.show()

    app.exec()

    #sys.exit( 0 )

# --------------------
if __name__ == "__main__":
    main()


# ---- eof
