

# ---- tof
""""




"""
# ---- search
"""
    Search for the following in the code below:



    See Also:

    Links
        Create Python GUIs with PyQt5 — Simple GUIs to full apps
            *>url  https://www.pythonguis.com/pyqt5/
        Qt Widget Gallery | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/gallery.html
        Widgets Classes | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/widget-classes.html


"""

# ---- imports


import inspect
#from   ex_qt import ia_qt
#import ia_qt
import subprocess
import sys
#import adjust_path
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
# widgets bigger
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
import tab_box_layout
import tab_combo_box
import tab_date_edit
import tab_dialog_etc
import tab_grid_layout
import tab_groupbox
import tab_misc_widgets
import tab_qlist
import tab_text_edit
import utils_for_tabs as uft
import wat_inspector

# from   platform import python_version
# print( f"your python version is: {python_version()}"  )   # add to running on

# # import PyQt5.QtWidgets as qtw    #  qt widgets avoid so much import below
# from   PyQt5.QtCore import Qt, QTimer
# from   PyQt5 import QtGui


# ---- imports neq qt












# ---- end imports

__version__   = "ver02 2024 22 14.00"
INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_1
BEGIN_MARK_2  = uft.BEGIN_MARK_2



# ---- main window ===================================================================
class QtWidgetExamples( QMainWindow ):
    def __init__(self):
        """
        window with many widgets, placed with regular layouts

        refactoring from earlier code, not yet done
        spinbox here but not in visible code also QTextEdit....
        stacked..... missing
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
        self.setWindowTitle( "QtWidgetExamples" )

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

        # # ---- Draft
        # tab      = uft.SeperatorTab()
        # title    = "Draft\n>>"
        # self.tab_widget.addTab( tab, title  )

        # # ---- TBD
        # tab      = uft.SeperatorTab()
        # title    = "TBD\n>>"
        # self.tab_widget.addTab( tab, title  )

        title    = "Misc\nWidgets"
        tab      = tab_misc_widgets.MiscWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "misc_widget_tab.txt"


        title    = "QComboBox\n"
        tab      = tab_combo_box.QComboBoxTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "combo_box_widget_tab.txt"


        title    = "QGroupBox\n"
        tab      = tab_groupbox.QGroupBoxTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "group_widget_tab.txt"

        # ---- QTextEdit
        title    = "QTextEdit\n"
        tab      = tab_text_edit.QTextEditTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "text_edit_tab.txt"

        title    = "QList\n"
        tab      = tab_qlist.QListWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "list_widget_tab.txt"

        title    = "DialogEtc\n"
        tab      = tab_dialog_etc.DialogEtcTab()    # tab_dialog_etc.py
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "dialog_etc_tab.txt"

        title    = "QDateEdit\n"
        tab      = tab_date_edit.QDateEditTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "date_edit_widget_tab.txt"

        title    = "QGroupBox\n"
        tab      = tab_groupbox.QGroupBoxTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "group_widget_tab.txt"

        title    = "QBoxLayout\n"
        tab      = tab_box_layout.QBoxLayoutTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "layout_Widget_tab.txt"

        # ---- QGridLayout
        title    = "QGridLayout\n"
        tab      = tab_grid_layout.GridLayoutTab()   # tab_grid_layout
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "grid_layout_tab.txt"

        # # ---- Done
        # tab      = uft.SeperatorTab()
        # title    = "Done\n>>"
        # self.tab_widget.addTab( tab, title  )

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

        action          = QAction( "Guide to QT Widgets...", self )
        connect_to      = partial( self.open_txt_file, "./docs/guide_to_qt_widgets.txt" )
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

    # #-------
    # def open_tab_help( self,   ):
    #     """
    #     what it says read:
    #         still needs work
    #     """
    #     tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
    #     # print( f"{self.doc_dir}{tab_title = }")

    #     doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
    #     doc_name            = f"{self.doc_dir}{doc_name}"
    #     print( f"{doc_name = }")
    #     ex_editor          = r"xed"

    #     proc               = subprocess.Popen( [ ex_editor, doc_name ] )

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

    # ---- maybe dead maybe salvage

    # --------
    def on_rb_clicked(self):
        """
        """
        radioButton = self.sender()
        if radioButton.isChecked():
            print( "\nCountry is %s" % (radioButton.country))
            #print(   "Id is       %s" % (radioButton.i ))
            print( f"self.country_group.id( radioButton ) {self.country_group.id( radioButton )}")
        print(f"country_group.checkedButton() >{self.country_group.checkedButton()}<" )
        checked_button    = self.country_group.checkedButton()
        print(f"checked_button.text(){checked_button.text()}" )
        # next seem to be assigned negative numbers ...
        print(f"country_group.checkedId() >{self.country_group.checkedId()}<" )
        buttons    = self.country_group.buttons()
        for i_button in buttons:
            print( f"{i_button}")

    # --------
    def show_values(self):
        """
        show all the values from widgets
        """
        print( "get and show values of widgets")

        line_edit_value  = self.line_edit_ex_1.text()
        cbox_value       = str( self.cbox_ex_1.isChecked())
        # need to save  list and loop thru    radioButton.isChecked() --- or ask the group
        cb1_text         = self.combobox_ex_1.currentText()

        msg   = ( f"\nline_edit_value    = {line_edit_value}"
                  f"\ncbox_value         = {cbox_value}"
                  f"\ncb1_text           = {cb1_text}"
        )
        print( msg )
        # self.message_widget.display_string( msg, )

# -----------------------------------
def main():
    """
    yes this is the main app
    """

    app                 = QApplication(sys.argv)
    #dialog          = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog
    a_wat_inspector     = wat_inspector.WatInspector( app )
    window              =  QtWidgetExamples()
    window.show()
    #sys.exit(
    app.exec()

    #sys.exit( 0 )

# --------------------
if __name__ == "__main__":
    main()


# ---- eof
