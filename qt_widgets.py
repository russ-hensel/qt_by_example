

# ---- tof
""""

Put all work into the tabs of WidgetExample
    except perhaps for placer work in second example
    rest for code extraction and deletion


"""
# ---- search
"""
    Search for the following in the code below:

        border        -- only on some widgets not QWidet
        button
        checkbox
        combobox     is a dropdownlist ddl
        edit          QLineEdit,   QTextEdit,
        action
        menu
        groupbox
        isChecked
        get_text
        grid
        label
        lineEdit
        listbox      QListWidget         in ex_  listbox
        icon
        MessageBox     QMessageBox
        qdate
        self.showMinimized()
        minimized
        show
        iconify
        radiobutton
        radiobutton index
        row
        size
        select
        stylesheet
        style
        text
        textOnLeft           for radiobutton
        widget
        partial

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


import adjust_path
import time

import wat
import wat_inspector

from   platform import python_version
print( f"your python version is: {python_version()}"  )   # add to running on

# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import below
# from   PyQt5.QtCore import Qt, QTimer
# from   PyQt5 import QtGui


# ---- imports neq qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QSizePolicy
from PyQt5.QtCore import QDate, Qt,  QSize
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtGui
from PyQt5.QtGui import QTextDocument

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
import ia_qt
import subprocess
from   subprocess import run
from   subprocess import Popen, PIPE, STDOUT
#import datetime
from   datetime import datetime

# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import above
from   functools  import partial

import sys
sys.path.append( r"D:\Russ\0000\python00\python3\_examples"  )
sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"  )
sys.path.append( "../")  # not working today vscode
sys.path.insert( 1, "/mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib" )


#import picture_viewer
import wat
import utils_for_tabs as uft

#wat_inspector    = wat.Wat( "joe")

# ---- end imports


INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_2
BEGIN_MARK_2  = uft.BEGIN_MARK_2



what   = Qt.AlignCenter   # valid aligment perhaps to addWidget   layout.addWidget
#	addWidget(QWidget *widget, int stretch = 0, Qt::Alignment alignment = Qt::Alignment())
note   = """
main work example it WidgetExamplesInTabs

Widget example with placer should be same with placer -- may have good salvage code
same for the rest of the examples

"""
print( note )

function_nl     = "\n\n"   #   msg   = f"{function_nl}function_name"   print( msg )


# --------------------------------
def set_groupbox_style( groupbox ):
        """
        used to modify the appearance of a groupbox
        see the groupbox tab
        """
        groupbox.setStyleSheet("""
            QGroupBox {
                border: 2px solid blue;
                border-radius: 10px;
                margin-top: 15px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                background-color: white;
            }
        """)


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
class QComboBoxWidgetTab( QWidget ) :
    def __init__(self):
        """
        """
        super().__init__()
        self._build_gui()

    # ---- combo tab ------------------------------------------------
    def _build_gui(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout(   )

        # ---- combo_1
        widget        = QComboBox()
        self.combo_1  = widget

        widget.addItem('Zero')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')

        widget.setCurrentIndex( 2 )   # set index

        # these work but in some case seem only to work with a lambda
        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        layout.addWidget( widget )

        # ---- combo_2
        widget        = QComboBox()
        self.combo_2  = widget

        widget.addItem('Zeroxx')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')
        #widget.editable( True )
        widget.setEditable( True )   # if is edited then value does not match index

        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        layout.addWidget( widget )


        # ---- buttons

        layout.addLayout ( button_layout )
        # --- buttons
        label       = "combo_reload"
        widget = QPushButton( label )
        widget.clicked.connect( self.combo_reload )

        button_layout.addWidget( widget )

        # ----
        label       = "inspect"
        widget = QPushButton( label )
        widget.clicked.connect( self.inspect )

        button_layout.addWidget( widget )

        # ----
        label       = "mutate"
        widget = QPushButton( label )
        widget.clicked.connect( self.mutate )

        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )
        #return tab_page

    # --------
    def show_combo_values(self):
        """

        """
        what    = "show_combo_values"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")


        print( "show_combo_values")
        ia_qt.q_combo_box( self.combo_1, "this is the first combobox from 1" )
        # current_text         = self.combo_1.currentText()
        # index                = self.combo_1.currentIndex()
        # msg   = ( f"\ncombo_1:"
        #           f"\n    current_text       = {current_text}"
        #           f"\n    index              = {index}"
        # )
        # print( msg )

        # current_text         = self.combo_2.currentText()
        # index                = self.combo_2.currentIndex()
        # index_text           = self.combo_2.itemText( index )
        # index_valid          = current_text == index_text
        # msg   = ( f"\ncombo_2:"
        #           f"\n    current_text       = {current_text}"
        #           f"\n    index              = {index}"
        #           f"\n    index_text         = {index_text}"
        #           f"\n    index_valid        = {index_valid}"
        # )
        # print( msg )
        # self.print_combo_values( self.combo_2 )
        ia_qt.q_combo_box( self.combo_2, "this is the second combobox from 1" )


    # # add this to ia_qt
    # def print_combo_values(self, combo_box ):
    #     """Prints all items in the QComboBox and the value of a specific index."""
    #     # Get all values
    #     all_items = [ combo_box.itemText(i) for i in range( combo_box.count())]
    #     print(f"All items in the QComboBox: {all_items}")

    #     # Get value at a specific index (e.g., index 2)
    #     specific_index = 2
    #     if specific_index <   combo_box.count():
    #         value_at_index =  combo_box.itemText( specific_index )
    #         print(f"Value at index {specific_index}: {value_at_index}")
    #     else:
    #         print(f"Index {specific_index} is out of range.")



    # -----------------------
    def conbo_signal(self, arg ):
        """
                activated(int index)
        void 	currentIndexChanged(int index)
        void 	currentTextChanged(const QString &text)
        void 	editTextChanged(const QString &text)
        void 	highlighted(int index)
        void 	textActivated(const QString &text)
        void 	textHighlighted(const QString &text)
        """
        what    = "conbo_signal"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( f"conbo_signal {arg}")

    # -----------------------
    def conbo_currentIndexChanged(self, arg ):
        """

        """
        print( f"conbo_currentIndexChanged {arg}")

    # -----------------------
    def combo_currentTextChanged(self, arg ):
        """
               activated(int index)
        void 	currentIndexChanged(int index)
        void 	currentTextChanged(const QString &text)
        void 	editTextChanged(const QString &text)
        void 	highlighted(int index)
        void 	textActivated(const QString &text)
        void 	textHighlighted(const QString &text)
        """
        print( f"combo_currentTextChanged {arg}")

    # --------------------------
    def combo_reload(self,   ):
        """
        notice order of events
        """
        what    = "combo_reload"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( f"combo_reload { '' }clear next --------", flush = True )
        values         =  [ "1_reload", "2", "3", "4", ]
            # what do i get I get a dict of lists, I need all the keys
        widget         = self.combo_1
        widget.clear()       # delete all items from comboBox
        print( f"combo_reload end clear / next addItems", flush = True )
        widget.addItems( values )
        print( f"{what} end { '' } --------", flush = True )

    # --------------------------
    def inspect_old( self, arg  ):
        """
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        print( f"combo_info { '' }  --------", flush = True )

        widget         = self.combo_1

        info           = widget.count()
        msg            = f"widget.count() {info}"
        print( msg )

        info           = widget.currentData()    # seem to always get None
        msg            = f"widget.currentData() {info}"
        print( msg )

        # qt5 not working for me
        # info           = widget.editable
        # msg            = f".editable {info}"
        # print( msg )

        info           = widget.currentText()
        msg            = f".currentText() {info}"
        print( msg )

        info           = widget.currentIndex()
        msg            = f".currentIndex() {info}"
        print( msg )

        info           = widget.placeholderText()
        msg            = f".placeholderText() {info}"
        print( msg )

        self.show_combo_values()   # move this code here


        print( f"combo_info end { '' } --------", flush = True )

    # ----
    def mutate(self,   ):
        """

        """
        what    = "mutate"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "\n>>>>change_widget   -- to do "   )
        self.combo_1.setCurrentIndex( 2 )

        self.combo_2.setCurrentText( "2" )


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        combo_1       = self.combo_1
        combo_2       = self.combo_2
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             #inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )


    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()

#  --------
class QDateEditTab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py

        """
        super().__init__()

        self.date_format   = "dd/MM/yyyy"

        self._build_gui()

    def _build_gui(self,   ):
        """

        """
        tab_page      = self
        layout        = QGridLayout( tab_page )
        button_layout = QHBoxLayout(   )

        ix_row        = 0
        ix_col        = 0

        widget  = QLabel( "w/o popup" )
        layout.addWidget( widget, ix_row, ix_col )   # row column allignment

        ix_col                  += 1
        #widget                  = QDateEdit()
        widget                  = CustomDateEdit()   # with context menu fro chat
        self.start_date_widget  = widget
        # widget.userDateChanged.connect( lambda: self.date_changed( ) )
        # widget.editingFinished.connect( lambda: self.date_changed( ) )
        #widget.setCalendarPopup( True )
        widget.setDate(QDate( 2022, 1, 1 ))
        layout.addWidget( widget, ix_row, ix_col )
        #placer.place( a_widget )

        # ----
        ix_col    += 1
        widget  = QLabel( "w popup" )
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
        widget.setDisplayFormat(   self.date_format )   # = "dd/MM/yyyy"
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

        # Set a custom display format
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        widget.setCalendarPopup(True)



        # Set the widget geometry
        self.dateTimeEdit.setGeometry(50, 50, 200, 30)

        #self.setGeometry(200, 200, 400, 200)

        layout.addWidget( widget, ix_row, ix_col )


        # ---- QTimeEdit

        from PyQt5.QtWidgets import QApplication, QMainWindow, QTimeEdit
        from PyQt5.QtCore import QTime

        ix_row                  += 1
        ix_col                  =0
        # Create a QTimeEdit widget
        widget          = QTimeEdit( self )
        self.timeEdit   = widget



        # Set a default time
        self.timeEdit.setTime(QTime.currentTime())

        # Set a custom display format
        self.timeEdit.setDisplayFormat("HH:mm:ss")

        # Set the widget geometry
        self.timeEdit.setGeometry(50, 50, 150, 30)


        # Show only hours and minutes
        widget.setDisplayFormat("HH:mm")

        # Show hours, minutes, and seconds (24-hour format)
        widget.setDisplayFormat("HH:mm:ss")

        # Show time in 12-hour format with AM/PM
        widget.setDisplayFormat("hh:mm:ss AP")

        from PyQt5.QtCore import QTime

        # Set minimum time to 8:00 AM
        widget.setMinimumTime(QTime(8, 0, 0))

        # Set maximum time to 6:00 PM
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

        # ---- Inspect
        widget = QPushButton("inspect")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.inspect( ) )
        button_layout.addWidget( widget )

        # ---- Inspect
        widget = QPushButton("mutate")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

        # ---- QPushButton
        widget = QPushButton("Clear\nEnd Date")
        widget.clicked.connect(lambda: self.set_empty( ))
        a_widget        = widget
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )

    # ------------------------------------
    def set_empty( self ):
        """
        read it

        """
        invalid_date     = QDate().fromString( "01/01/0001", "dd/MM/yyyy" )
        self.end_date_widget.setDate( invalid_date )

    # ------------------------------------
    def to_unix( self, qdate, ): # date_format = None ):
        """
        read it
        need a begin of day and an end of day this is end i think
        from chat
        """

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
        the date to the last second of the day befor the date.

        Assume the date and times are gmt



        """
        what    = "mutate"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "\n\nmutate ---------------------------------------")
        # print( f"w/o popup  {self.start_date_widget.date() = }" )  # setText()   ??
        # print( f"w   popup  {self.end_date_widget.date() = }" )  # setText()   ??
        #a_date            = self.end_date_widget.date()

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
        the date to the last second of the day befor the date.

        Assume the date and times are gmt

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
        print( "date_changed" )
        print( f"{arg = }")


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )



    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()

#  --------
class QGroupBoxTab( QWidget ) :
    def __init__(self):
        """

        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py

        """
        super().__init__()
        self._build_gui()


    def _build_gui(self,   ):
        """
        build the gui
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        # ---- QGroupBox
        #groupbox   = QGroupBox()  # no title
        groupbox   = QGroupBox( "QGroupBox 1" )   # version with title

        groupbox.setStyleSheet("""
            QGroupBox {
                border: 2px solid blue;
                border-radius: 10px;
                margin-top: 15px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                background-color: white;
            }
        """)

        layout.addWidget( groupbox )
        layout_b     = QHBoxLayout( groupbox  )

        self.build_gui_in_groupbox( layout_b )

        button_layout = layout # needs fixing

        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )

    # ---------------------------
    def build_gui_in_groupbox( self, layout ):
        """
        this is a bit of gui built inside another groupbos = QGroupBox()
        """
        widget = QPushButton("do_nothing")
        # Connect button signals to slots for group 2

        #widget.clicked.connect(  self.show_values  )
        layout.addWidget( widget )

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        breakpoint()

# ----------------------------
class GridLayoutWidgetTab( QWidget ) :
    def __init__(self):
        """



        """
        super().__init__()
        self._build_gui()

    # ----------------------------
    def _build_gui(self,   ):
        """

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
        #widget.clicked.connect( lambda: self.replace_widget_layout_tab() )


        # layout_a     = QHBoxLayout(    )
        # layout.addLayout( layout_a )
        # self.layout_tab_layout_a   = layout_a

       #  self.widget_ix              = 22
       #  widget                      = QPushButton( f"Button   {self.widget_ix}")
       #  layout_a.addWidget( widget )
       #  self.layout_tab_button_1    = widget
       #  self.widget_temp            = widget

       #  layout_b     = QHBoxLayout(    )
       #  layout.addLayout( layout_b )

       #  widget = QPushButton("show_values")
       #  layout_b.addWidget( widget )

       #  widget = QPushButton("remove_add_widget")
       #  layout_b.addWidget( widget )
       #  widget.clicked.connect( lambda: self.remove_add_widget_layout_tab() )

       #  widget = QPushButton("replace_widget")
       #  layout_b.addWidget( widget )
       #  widget.clicked.connect( lambda: self.replace_widget_layout_tab() )
       # # --------
       #  widget = QPushButton( "minimize" )  # showminimized iconify
       #  layout_b.addWidget( widget )
       #  print( "need to change self to the parent ")
       #  widget.clicked.connect(lambda: self.iconify( ))

        return tab_page


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db          = parent_window.sample_db
        model         = self.people_model
        view          = self.people_view
        wat_inspector.go(
             msg            = "self.model from inspect method",
             inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()
#  --------
class QTextEditTab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py

        """
        super().__init__()
        self._build_gui()
        # State variable to track search position
        self.last_position = 0

    def _build_gui(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        tab_page      = self
        layout        = QGridLayout( tab_page )

        text_edit       = QTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = text_edit

        print( f"{text_edit.minimumSize( ) =} ")
        text_edit.setMinimumHeight( 100 )
        print(  ia_qt.q_text_edit( text_edit, msg = "QTextEditTab.text_edit" ) )

        ix_row     = 0
        ix_col     = 0
        row_span   = 1
        col_span   = 1

        layout.addWidget( text_edit, ix_row, ix_col, row_span, col_span )  # rowSpan, columnSpan Allignment  # args are
            # widget: The widget you want to add to the grid.
            # row: The row number where the widget should appear (starting from 0).
            # column: The column number where the widget should appear (starting from 0).
            # rowSpan (optional): The number of rows the widget should span (default is 1).
            # columnSpan (optional): The number of columns the widget should span (default is 1).
            # alignment (optional): The ali

        # ----- search
        ix_row     += 1
        ix_col     = 0
        row_span   = 1
        col_span   = 1

        widget             = QLineEdit()
        self.line_edit     = widget

        # ---- ssee if these are legal
        #widget.setHeight( )

        # widget.maximumHeight(…) # maximumHeight(self) -> int
        # widget.maximumSize(…) # maximumSize(self) -> QSize
        # widget.maximumViewportSize(…) # maximumViewportSize(self) -> QSize
        # widget.maximumWidth(…) # maximumWidth(self) -> int
  # def setAcceptDrops(…) # setAcceptDrops(self, on: bool)
  # def setAcceptRichText(…) # setAcceptRichText(self, accept: bool)
  # def setAccessibleDescription(…) # setAccessibleDescription(self, description: Optional[str])
  # def setAccessibleName(…) # setAccessibleName(self, name: Optional[str])
  # def setAlignment(…) # setAlignment(self, a: Union[Qt.Alignment, Qt.AlignmentFlag])
  # def setAttribute(…) # setAttribute(self, attribute: Qt.WidgetAttribute, on: bool = True)
  # def setAutoFillBackground(…) # setAutoFillBackground(self, enabled: bool)
  # def setAutoFormatting(…) # setAutoFormatting(self, features: Union[QTextEdit.AutoFormatting, QTextEdit.AutoFormattingFlag])
  # def setBackgroundRole(…) # setBackgroundRole(self, a0: QPalette.ColorRole)
  # def setBaseSize(…) # setBaseSize(self, basew: int, baseh: int)…
  # def setContentsMargins(…) # setContentsMargins(self, left: int, top: int, right: int, bottom: int)…
  # def setContextMenuPolicy(…) # setContextMenuPolicy(self, policy: Qt.ContextMenuPolicy)
  # def setCornerWidget(…) # setCornerWidget(self, widget: Optional[QWidget])
  # def setCurrentCharFormat(…) # setCurrentCharFormat(self, format: QTextCharFormat)
  # def setCurrentFont(…) # setCurrentFont(self, f: QFont)
  # def setCursor(…) # setCursor(self, a0: Union[QCursor, Qt.CursorShape])
  # def setCursorWidth(…) # setCursorWidth(self, width: int)
  # def setDisabled(…) # setDisabled(self, a0: bool)
  # def setDocument(…) # setDocument(self, document: Optional[QTextDocument])
  # def setDocumentTitle(…) # setDocumentTitle(self, title: Optional[str])
  # def setEnabled(…) # setEnabled(self, a0: bool)
  # def setExtraSelections(…) # setExtraSelections(self, selections: Iterable[QTextEdit.ExtraSelection])
  # def setFixedHeight(…) # setFixedHeight(self, h: int)
  # def setFixedSize(…) # setFixedSize(self, a0: QSize)…
  # def setFixedWidth(…) # setFixedWidth(self, w: int)
  # def setFocus(…) # setFocus(self)…
  # def setFocusPolicy(…) # setFocusPolicy(self, policy: Qt.FocusPolicy)
  # def setFocusProxy(…) # setFocusProxy(self, a0: Optional[QWidget])
  # def setFont(…) # setFont(self, a0: QFont)
  # def setFontFamily(…) # setFontFamily(self, fontFamily: Optional[str])
  # def setFontItalic(…) # setFontItalic(self, b: bool)
  # def setFontPointSize(…) # setFontPointSize(self, s: float)
  # def setFontUnderline(…) # setFontUnderline(self, b: bool)
  # def setFontWeight(…) # setFontWeight(self, w: int)
  # def setForegroundRole(…) # setForegroundRole(self, a0: QPalette.ColorRole)
  # def setFrameRect(…) # setFrameRect(self, a0: QRect)
  # def setFrameShadow(…) # setFrameShadow(self, a0: QFrame.Shadow)
  # def setFrameShape(…) # setFrameShape(self, a0: QFrame.Shape)
  # def setFrameStyle(…) # setFrameStyle(self, a0: int)
  # def setGeometry(…) # setGeometry(self, a0: QRect)…
  # def setGraphicsEffect(…) # setGraphicsEffect(self, effect: Optional[QGraphicsEffect])
  # def setHidden(…) # setHidden(self, hidden: bool)
  # def setHorizontalScrollBar(…) # setHorizontalScrollBar(self, scrollbar: Optional[QScrollBar])
  # def setHorizontalScrollBarPolicy(…) # setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy)
  # def setHtml(…) # setHtml(self, text: Optional[str])
  # def setInputMethodHints(…) # setInputMethodHints(self, hints: Union[Qt.InputMethodHints, Qt.InputMethodHint])
  # def setLayout(…) # setLayout(self, a0: Optional[QLayout])
  # def setLayoutDirection(…) # setLayoutDirection(self, direction: Qt.LayoutDirection)
  # def setLineWidth(…) # setLineWidth(self, a0: int)
  # def setLineWrapColumnOrWidth(…) # setLineWrapColumnOrWidth(self, w: int)
  # def setLineWrapMode(…) # setLineWrapMode(self, mode: QTextEdit.LineWrapMode)
  # def setLocale(…) # setLocale(self, locale: QLocale)
  # def setMarkdown(…) # setMarkdown(self, markdown: Optional[str])
  # def setMask(…) # setMask(self, a0: QBitmap)…
  # def setMaximumHeight(…) # setMaximumHeight(self, maxh: int)
  # def setMaximumSize(…) # setMaximumSize(self, maxw: int, maxh: int)…
  # def setMaximumWidth(…) # setMaximumWidth(self, maxw: int)
  # def setMidLineWidth(…) # setMidLineWidth(self, a0: int)
  # def setMinimumHeight(…) # setMinimumHeight(self, minh: int)
  # def setMinimumSize(…) # setMinimumSize(self, minw: int, minh: int)…
  # def setMinimumWidth(…) # setMinimumWidth(self, minw: int)
  # def setMouseTracking(…) # setMouseTracking(self, enable: bool)
  # def setObjectName(…) # setObjectName(self, name: Optional[str])
  # def setOverwriteMode(…) # setOverwriteMode(self, overwrite: bool)
  # def setPalette(…) # setPalette(self, a0: QPalette)
  # def setParent(…) # setParent(self, parent: Optional[QWidget])…
  # def setPlaceholderText(…) # setPlaceholderText(self, placeholderText: Optional[str])
  # def setPlainText(…) # setPlainText(self, text: Optional[str])
  # def setProperty(…) # setProperty(self, name: Optional[str], value: Any) -> bool
  # def setReadOnly(…) # setReadOnly(self, ro: bool)
  # def setShortcutAutoRepeat(…) # setShortcutAutoRepeat(self, id: int, enabled: bool = True)
  # def setShortcutEnabled(…) # setShortcutEnabled(self, id: int, enabled: bool = True)
  # def setSizeAdjustPolicy(…) # setSizeAdjustPolicy(self, policy: QAbstractScrollArea.SizeAdjustPolicy)
  # def setSizeIncrement(…) # setSizeIncrement(self, w: int, h: int)…
  # def setSizePolicy(…) # setSizePolicy(self, a0: QSizePolicy)…
  # def setStatusTip(…) # setStatusTip(self, a0: Optional[str])
  # def setStyle(…) # setStyle(self, a0: Optional[QStyle])
  # def setStyleSheet(…) # setStyleSheet(self, styleSheet: Optional[str])
  # def setTabChangesFocus(…) # setTabChangesFocus(self, b: bool)
  # def setTabOrder(…) # setTabOrder(a0: Optional[QWidget], a1: Optional[QWidget])
  # def setTabStopDistance(…) # setTabStopDistance(self, distance: float)
  # def setTabStopWidth(…) # setTabStopWidth(self, width: int)
  # def setTabletTracking(…) # setTabletTracking(self, enable: bool)
  # def setText(…) # setText(self, text: Optional[str])
  # def setTextBackgroundColor(…) # setTextBackgroundColor(self, c: Union[QColor, Qt.GlobalColor])
  # def setTextColor(…) # setTextColor(self, c: Union[QColor, Qt.GlobalColor])
  # def setTextCursor(…) # setTextCursor(self, cursor: QTextCursor)
  # def setTextInteractionFlags(…) # setTextInteractionFlags(self, flags: Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag])
  # def setToolTip(…) # setToolTip(self, a0: Optional[str])
  # def setToolTipDuration(…) # setToolTipDuration(self, msec: int)
  # def setUndoRedoEnabled(…) # setUndoRedoEnabled(self, enable: bool)
  # def setUpdatesEnabled(…) # setUpdatesEnabled(self, enable: bool)
  # def setVerticalScrollBar(…) # setVerticalScrollBar(self, scrollbar: Optional[QScrollBar])
  # def setVerticalScrollBarPolicy(…) # setVerticalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy)
  # def setViewport(…) # setViewport(self, widget: Optional[QWidget])
  # def setViewportMargins(…) # setViewportMargins(self, left: int, top: int, right: int, bottom: int)…
  # def setVisible(…) # setVisible(self, visible: bool)
  # def setWhatsThis(…) # setWhatsThis(self, a0: Optional[str])
  # def setWindowFilePath(…) # setWindowFilePath(self, filePath: Optional[str])
  # def setWindowFlag(…) # setWindowFlag(self, a0: Qt.WindowType, on: bool = True)
  # def setWindowFlags(…) # setWindowFlags(self, type: Union[Qt.WindowFlags, Qt.WindowType])
  # def setWindowIcon(…) # setWindowIcon(self, icon: QIcon)
  # def setWindowIconText(…) # setWindowIconText(self, a0: Optional[str])
  # def setWindowModality(…) # setWindowModality(self, windowModality: Qt.WindowModality)
  # def setWindowModified(…) # setWindowModified(self, a0: bool)
  # def setWindowOpacity(…) # setWindowOpacity(self, level: float)
  # def setWindowRole(…) # setWindowRole(self, a0: Optional[str])
  # def setWindowState(…) # setWindowState(self, state: Union[Qt.WindowStates, Qt.WindowState])
  # def setWindowTitle(…) # setWindowTitle(self, a0: Optional[str])
  # def setWordWrapMode(…) # setWordWrapMode(self, policy: QTextOption.WrapMode)
  # def setupViewport(…) # setupViewport(self, viewport: Optional[QWidget])

  # def sizeHint(…) # sizeHint(self) -> QSize
  # def sizeIncrement(…) # sizeIncrement(self) -> QSize
        #widget.minimumHeight(  ) # minimumHeight(self) -> int
        #QSize( 100, 500  )


        widget.setPlaceholderText("Enter search text")
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        #ix_row     += 1
        ix_col     += 1
        row_span   = 1
        col_span   = 1
        widget           = QPushButton("Down")
        self.down_button = widget
        widget.clicked.connect(self.search_down)
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        ix_col     += 1
        widget           = QPushButton("Up")
        self.up_button   = widget
        widget.clicked.connect( self.search_up )
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        # ---- lower buttons
        ix_row     += 1
        ix_col     = 0
        row_span   = 1
        col_span   = 1
        button_layout = QHBoxLayout(   )
        layout.addLayout ( button_layout, ix_row, ix_col, row_span,  col_span )
            # if you have row_span you need col_span, only positional


        # # ----
        # label       = "show_values"
        # widget = QPushButton( label )
        # widget.clicked.connect( self.show_combo_values )

        # button_layout.addWidget( widget )

        # ---- PB clear_text
        widget = QPushButton("clear\n_text")
        widget.clicked.connect( self.clear_text )
        button_layout.addWidget( widget,   )

        # ---- PB set_text\n_ver_1
        widget = QPushButton( "set_text\n_ver_1" )
        widget.clicked.connect(  self.set_text_ver_1 )
        #widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

        # ---- PB set_text\n_ver_2
        widget = QPushButton( "set_text\n_ver_2" )
        widget.clicked.connect(  self.set_text_ver_2 )
        #widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

        widget = QPushButton("insert_text\n")
        widget.clicked.connect( self.insert_text  )
        button_layout.addWidget( widget,  )


        # widget = QPushButton( "delete\n_text" )
        # widget.clicked.connect(lambda: self.delete_text(text_edit))
        # widget.setMaximumWidth(150)
        # button_layout.addWidget( widget,   )

        # widget = QPushButton( "change\n_widget" )
        # widget.clicked.connect(lambda: self.change_widget( text_edit ))
        # widget.setMaximumWidth(150)
        # button_layout.addWidget( widget,   )

        widget = QPushButton( "copy_line_of_text\n" )
        widget.clicked.connect(lambda: self.copy_line_of_text( text_edit ))
        button_layout.addWidget( widget,   )

        widget = QPushButton( "copy_n_lines\n_of_text" )
        widget.clicked.connect(lambda: self.copy_n_lines_of_text( text_edit, 5 ))
        button_layout.addWidget( widget,   )

        widget = QPushButton("copy_selected\n_text")
        widget.clicked.connect( self.copy_selected_text )
        button_layout.addWidget( widget,   )





        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # ---------------  end of button actions and class
    # ---------------------------------------
    def display_string( self, a_string, update_now = False ):
        """
        !! we may phase out for print_string  or the reverse ??
             make one call the other
        print to message area, with scrolling and
        log if we are configured for it

        parameters.gui_text_log_fn    = False  # "gui_text.log"
                                               # a file name or something false


        parameters.log_gui_text       = False # True or false to log text
        parameters.log_gui_text_level = 10    # logging level for above

        !! add parameter clear_msg = True or false

        """
        print(  f"in display_string, with a_string = {a_string}")
        # return
        #   try  !!!  QTextEdit.clear()
        cursor = self.text_edit.textCursor()
        # cursor.movePosition( QTextCursor::End )
        cursor.insertText( a_string )

    #  --------
    def print_message(self, text):
        print("Button clicked:", text)

    #  --------
    def clear_text( self ):
        """
        """
        print( "QTextEditTab.clear_text"   )
        self.text_edit.clear()

    #  --------
    def copy_text(self, text_edit):
        """
        """
        print( "QTextEditTab.copy_text"   )
        selected_text      = text_edit.toPlainText()
        QApplication.clipboard().setText(selected_text)
        print(  f" copy_text -> {selected_text }" )
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


    # ----
    def set_text_ver_1(self,  ):
        """
        """
        what    = "set_text_ver_1"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        a_string    = 1 * (

        """
        More than 20 years have passed since I authored the Python
 e of the most popular
programming languages in the world. Python programmers also
have a wealth of information at their fingertips in the form of
advanced editors, IDEs, notebooks, web pages, and more. In fact,
there’s probably little need to consult a reference book when almost
any reference material you might want can be conjured to appear
before your eyes with the touch of a few keys.

        """ )

        self.set_text( a_string )
    # ----
    def set_text_ver_2(self,  ):
        """
        """
        what    = "set_text_ver_2"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        a_string    = 22  * (

        """
        HOMEXCEL Sponges Kitchen 24pcs, Non-Scratch Scrub Dish Sponges,
        Safe on Non-Stick Cookware,Dual Sided Cleaning Sponges
        for Kitchen,Household,Bathroom and More

        """ )

        self.set_text( a_string )
    # ----------
    def set_textxxx(self, a_string ):
        """
        """
        text_edit       = self.text_edit
        text_edit.clear()
        cursor          = text_edit.textCursor()
        cursor.insertText(a_string)

    # ----
    def delete_text(self, text_edit):
        """
        """
        what    = "delete_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        #print( "QTextEditTab.delete_text"   )

        text_edit.clear()

    # ----
    def insert_text( self, ):
        """
        insert text at the cursor position
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        a_string  = ( """>>---- so here is a bit
of text the we will
           ------------------> insert
at the cursor ----<<""")

        text_edit       = self.text_edit
        cursor          = text_edit.textCursor()
        cursor.insertText( a_string )

    #----------------------------
    def copy_selected_text(self,  ):
        """
        """
        what    = "copy_selected_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        text_edit       = self.text_edit
        selected_text   = text_edit.textCursor().selectedText()
        QApplication.clipboard().setText( selected_text )
        print(  f"{what} -> {selected_text = } now in clipbpard" )

    #----------------------
    def copy_n_lines_of_text(self, text_edit, num_lines ):
        """
        chat:
            .....
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "QTextEditTab.copy_n_lines_of_text"   )
        cursor = text_edit.textCursor()

        # Save the original cursor position
        original_position = cursor.position()

        # Move to the start of the current line
        cursor.movePosition(cursor.StartOfLine)

        # List to store the next lines
        lines = []

        # Collect the next `num_lines` lines
        for _ in range( num_lines ):
            # Select the line from the start to the end
            cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor)
            line_text = cursor.selectedText()

            # Add the selected line to the list
            lines.append(line_text)

            # Move to the start of the next line
            cursor.movePosition(cursor.Down)

        # Restore the original cursor position
        cursor.setPosition(original_position)
        self.text_edit.setTextCursor(cursor)

        # Print or return the list of lines
        print(f"Next {num_lines} lines:", lines)
        return lines


    #----------------------
    def copy_line_of_text(self, ):
        """
        chat:
        With a QTextWidge holding some text:
        from the cursor position copy the text from the
        beginning of the line to the end of the line.
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        text_edit  = self.text_edit
        cursor              = text_edit.textCursor()
        # Save the original cursor position
        original_position   = cursor.position()
        cursor.movePosition( cursor.StartOfLine )

        # Select the text from the beginning to the end of the line
        cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor)
        selected_text = cursor.selectedText()
        # print(f"Copied text: {selected_text = }")

        # Optionally, copy to the system clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(selected_text)

        # Restore the original cursor position
        cursor.setPosition(original_position)
        self.text_edit.setTextCursor(cursor)

        print(f"Copied text: {selected_text = }")

        #print( "copied text is {1 = } "   )


    # ---------------------
    def search_down(self):
        """
        think i want no print for this
        search from current currsor down in text field
        """
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
        """
        think i want no print for this
        search from current currsor up in text field
        """
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


    # ---------------------
    def inspect_widget(self,  ):
        """
        in a QTextEdit how do i find the position of the cursor
        move the cursor to some position, move the cursor to the top, or bottom
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "\n >>>> inspect_widget.inspect_widget  -- to do "   )
        print( "some cursor stuff in copy__")
        print( f"copy_all_text {self.copy_all_text( self.text_edit )}" )


    # ----
    def change_widget(self, text_edit ):
        """
        in a QTextEdit how do i find the position of the cursor
        move the cursor to some positext_edit.show()tion, move the cursor to the top, or bottom

        # Move the cursor by 5 characters while keeping the selection
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 5)

        # Apply the modified cursor to the QTextEdit to reflect the selection
        text_edit.setTextCursor(cursor)
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "\n>>>>change_widget   -- to do "   )
        print( "some cursor stuff in copy__")

        # Ensure that the cursor is visible and the widget scrolls to it
        text_edit.ensureCursorVisible()

        cursor = text_edit.textCursor()
        cursor.setPosition(10)  # Moves the cursor to position 10 in the text
        text_edit.setTextCursor(cursor)
        # Move the cursor by 5 characters while keeping the selection
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 5)
        # Apply the modified cursor to the QTextEdit to reflect the selection
        text_edit.setTextCursor(cursor)
        text_edit.show()
        # time.sleep( 1 )

        # cursor = text_edit.textCursor()
        # cursor.movePosition(QTextCursor.Start)   # .End
        # text_edit.setTextCursor(cursor)
        # time.sleep( 1 )

        # print( "cursor to end ")
        # cursor = text_edit.textCursor()
        # cursor.movePosition(QTextCursor.End)   # .End
        # text_edit.setTextCursor(cursor)


        # # Move cursor to position 100
        # cursor = text_edit.textCursor()
        # cursor.setPosition(100)
        # text_edit.setTextCursor(cursor)

        print( "\n>>>>change_widget   -- to do "   )

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        local_self            = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()

#  --------
class QLayoutWidgetTab( QWidget ) :
    def __init__(self):
        """

        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py

        """
        super().__init__()
        self._build_gui()


    def _build_gui(self,   ):
        """

        """

        tab_page      = self

        layout        = QVBoxLayout( tab_page )

        layout_a     = QHBoxLayout(    )
        layout.addLayout( layout_a )
        self.layout_tab_layout_a   = layout_a

        self.widget_ix              = 22
        widget                      = QPushButton( f"Button   {self.widget_ix}")
        layout_a.addWidget( widget, stretch = 2 )
        self.layout_tab_button_1    = widget
        self.widget_temp            = widget

        layout_b     = QHBoxLayout(    )
        layout.addLayout( layout_b )

        widget = QPushButton("show_values")
        layout_b.addWidget( widget )

        widget = QPushButton("remove_add_widget")
        layout_b.addWidget( widget )
        widget.clicked.connect( lambda: self.remove_add_widget_layout_tab() )

        widget = QPushButton("replace_widget")
        layout_b.addWidget( widget )
        widget.clicked.connect( lambda: self.replace_widget_layout_tab() )

       # --------
        widget = QPushButton( "minimize" )  # showminimized iconify
        layout_b.addWidget( widget )
        print( "need to change self to the parent ")
        widget.clicked.connect(lambda: self.iconify( ))

        button_layout = layout_b
        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )

    #-----------------------------------------------
    def remove_add_widget_layout_tab( self, ):
        """
        deletes and adds but position may change
        """
        print( "LayoutWidgetTab.remove_add_widget_layout_tab"   )

        print( "replace widget is better may need delete later ")
        self.widget_ix             += 1
        widget = QPushButton("Button + str(self.widget_ix)")

        #layout_b.addWidget( widget )

        self.layout_tab_layout_a.removeWidget( self.widget_temp  )
        self.widget_temp   = widget
        # button1.deleteLater()  # Optionally delete the old widget
        self.layout_tab_layout_a.addWidget( widget )

    #-----------------------------------------------
    def replace_widget_layout_tab( self, ):
        """
        deletes and adds but position may change
        """
        what    = "insert_text"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        print( "LayoutWidgetTab.replace_widget_layout_tab"   )

        widget                      = self.widget_temp
        self.widget_ix             += 1
        widget_new                  = QPushButton( f"Button   {self.widget_ix}")
        #self.keep_me                = widget_new
        # stop from delete

        self.replace_layout_widget( self.layout_tab_layout_a, widget, widget_new )
        self.widget_temp            = widget_new

        # print( f"{widget}")
        # print( f"{widget_new}")

    def replace_layout_widget( self, layout, widget, widget_new ):
        """
        function should work copy and paste
        will be a problem if widget is not found in layout

        Args:
            layout (TYPE): DESCRIPTION.
            widget (TYPE): DESCRIPTION.

        """
        print( "LayoutWidgetTab.replace_layout_widget"   )
        # print( f"{widget}")
        # print( f"{widget_new}")
        # Find the index of the existing widget
        index               = layout.indexOf( widget )
        print( f"widget at {index}")
        # Remove the old widget
        widget_to_remove    = layout.takeAt(index).widget()

        # see if this is causing a problem
        if widget_to_remove:
            widget_to_remove.deleteLat



    # def table_widget_no_edit(self,  ):
    #     """
    #     from chat

    #     """
    #     table = self.table
    #     for row in range(table.rowCount()):
    #         for column in range(table.columnCount()):
    #             item = table.item(row, column)
    #             if item is not None:
    #                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)



    # def table_widget_add_row(self, data=None):
    #     """
    #     Method to add a row with optional data

    #     """
    #     row_position = self.table.rowCount()
    #     self.table.insertRow(row_position)

    #     # If data is provided, set it in the cells
    #     if data:
    #         for i, item in enumerate(data):
    #             self.table.setItem(row_position, i, QTableWidgetItem(item))

    # # Method to delete the selected row
    # def table_widget_delete_row(self):
    #     selected_row = self.table.currentRow()
    #     if selected_row >= 0:
    #         self.table.removeRow(selected_row)

    # # Method to edit a particular cell
    # def table_widget_edit_cell(self, row, column, new_value):
    #     self.table.setItem(row, column, QTableWidgetItem(new_value))

    # # Example method to add an item to a particular cell
    # def table_widget_add_item(self, row, column, value):
    #     self.table.setItem(row, colum

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        #print( "QTextEditTab.copy_line_of_text"   )( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )


    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        breakpoint()


    # -----------------------
    def build_gui_sub(self, layout ):
        """
        = QGroupBox()
        """


#  --------
class QListWidgetTab( QWidget ) :
    def __init__(self):
        """


        """
        super().__init__()
        self._build_gui()


    #-----------------------------------------------
    def _build_gui(self,   ):
        """

        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout( )

        # ---- QListWidget
        widget              = QListWidget(    )
        self.list_widget_1  = widget
        widget.setGeometry( 50, 50, 200, 200 )
        layout.addWidget( widget )

        widget.itemClicked.connect( self.list_clicked )

        values    =  [ "one", "two"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )

        widget.clear()

        values    =  [ "oneish", "twoish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2
            widget.setCurrentRow(index_to_select)

        ia_qt.q_list( widget )

        # --- buttons
        layout.addLayout( button_layout,  )

        button_layout.addWidget( widget )



        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )

    # --------------------
    def list_clicked( self, item ):
        # Get the row ID (index)
        what    = "list_clicked"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        widget        = self.list_widget_1
        row           = widget .row(item)

        # Get the text of the clicked item
        text = item.text()

        print(f"Clicked row: {row}, text: {text}")


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )




    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        breakpoint()


#  --------
class TemplateCopyMeWidgetTab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self._build_gui()


    def _build_gui(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        """

        tab_page      = self

        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout( )


        # ---- QGroupBox
        #groupbox   = QGroupBox()
        # groupbox   = QGroupBox( "QGroupBox 1" )   # version with title
        # layout.addWidget( groupbox )
        # layout_b     = QHBoxLayout( groupbox  )
        # self.build_gui_in_groupbox( layout_b )

        # ---- buttons
        layout.addLayout ( button_layout )

        label       = "combo_reload"
        widget      = QPushButton( label )
        #widget.clicked.connect( self.combo_reload )
        button_layout.addWidget( widget )

        # ----
        label       = "inspect"
        widget      = QPushButton( label )
        widget.clicked.connect( self.inspect )
        button_layout.addWidget( widget )


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             inspect_me     = self.text_edit,
             a_locals       = locals(),
             a_globals      = globals(), )



    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        breakpoint()

# #  --------
# class PictureViewerTab( QWidget ) :
#     def __init__(self):
#         """

#         """
#         super().__init__()
#         self._build_gui()


#     def _build_gui(self,   ):
#         """
#         all build on a local QWidget
#         count : const int
#         currentData : const QVariant
#         currentIndex : int
#         """

#         tab_page      = self

#         layout        = QVBoxLayout( tab_page )
#         button_layout = QHBoxLayout( )

#         widget        = picture_viewer.PictureViewer(   )
#         self.viewer   = widget
#         layout.addWidget( widget )
#         # ---- QGroupBox
#         #groupbox   = QGroupBox()
#         # groupbox   = QGroupBox( "QGroupBox 1" )   # version with title
#         # layout.addWidget( groupbox )
#         # layout_b     = QHBoxLayout( groupbox  )
#         # self.build_gui_in_groupbox( layout_b )

#         # ---- buttons
#         layout.addLayout ( button_layout )

#         label       = "add buttons\n and actions"
#         widget      = QPushButton( label )
#         #widget.clicked.connect( self.combo_reload )
#         button_layout.addWidget( widget )


#         label       = "combo_reload"
#         widget      = QPushButton( label )
#         #widget.clicked.connect( self.combo_reload )
#         button_layout.addWidget( widget )

#         # ----
#         label       = "inspect"
#         widget      = QPushButton( label )
#         widget.clicked.connect( self.inspect )
#         button_layout.addWidget( widget )


#     # --------------------------
#     def inspect( self, arg  ):
#         """
#         count : const int
#         currentData : const QVariant
#         currentIndex : int
#         currentText : QString
#         duplicatesEnabled : bool
#         editable : bool
#         """
#         print( f"Inspect picture_viewer  { '' }  --------",   )

#         wat.short( self.viewer )
#         wat_says   = wat.str( self.viewer )
#         print( f"\n\n\n-----------------------------------\n{wat_says}")
#         pass
#         # widget         = self.combo_1

#         # info           = widget.count()
#         # msg            = f".count() {info}"
#         # print( msg )

#         # info           = widget.currentData()    # seem to always get None
#         # msg            = f".currentData() {info}"
#         # print( msg )

#         # # qt5 not working for me
#         # # info           = widget.editable
#         # # msg            = f".editable {info}"
#         # # print( msg )

#         # info           = widget.currentText()
#         # msg            = f".currentText() {info}"
#         # print( msg )

#         # info           = widget.currentIndex()
#         # msg            = f".currentIndex() {info}"
#         # print( msg )

#         # info           = widget.placeholderText()
#         # msg            = f".placeholderText() {info}"
#         # print( msg )

#         # self.show_combo_values()   # move this code here


#         # print( f"combo_info end { '' } --------", flush = True )




#  --------
class SmallerWidgetTab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py

        """
        super().__init__()
        self._build_gui()

    # -------------------------------
    def _build_gui(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout(   )

        # ---- QLabel
        widget          = QLabel("Qlabel 1")
        self.qlabel_1   = widget
        widget.setLayoutDirection( Qt.RightToLeft )
        #widget.setLayoutDirection( Qt.LeftToRight )
        layout.addWidget( widget )

        # ---- QLabel
        widget          = QLabel("Qlabel 2 layout allign right ")
        self.qlabel_2   = widget
        widget.setLayoutDirection( Qt.RightToLeft )
        #widget.setText( "change original text ..........." )
        #widget.setLayoutDirection( Qt.LeftToRight )
        #layout.addWidget( widget )
        layout.addWidget( widget, Qt.AlignmentFlag.AlignRight )

        # ---- QCheckBox
        widget          = QCheckBox("i am a QCheckBox" )
        self.cbox_ex_1  = widget
        widget.animal   = "Cat"   # monkey patch ??
        widget.setChecked(True)
        widget.toggled.connect( self.cbox_clicked )
        layout.addWidget( widget, stretch = 0 )

        # ---- QLineEdit 1
        widget              = QLineEdit()
        self.line_edit_1    = widget
        widget.setText( "QLineEdit use setText to set value disabled? on second line?")
            #\n does not give second line
        widget.setDisabled( True )
        widget.setDisabled( False )
        widget.setPlaceholderText( "Enter your text here" )  # clear to see
        widget.textChanged.connect( self.on_text_changed ) # user or programatically
        widget.textEdited.connect(self.on_text_edited)  # user only
        widget.editingFinished.connect(self.on_editing_finished) # done leaves control
        widget.setReadOnly(True)
        widget.setReadOnly(False)


        # focusInEvent(QFocusEvent): This event is triggered when the QLineEdit gains focus (e.g., when the user clicks on it).

        # focusOutEvent(QFocusEvent):
        # keypress, mouse events....
        # iemput masks, completers....;. placeholder

        layout.addWidget( widget )

        # ---- QLineEdit 2
        widget              = QLineEdit()
        self.line_edit_2    = widget
        widget.setText( "QLineEdit line_edit_2")
        widget.textChanged.connect( lambda: self.signal_sent(  "textChanged"   ) )
        widget.editingFinished.connect(  lambda: self.signal_sent( "editingFinished"  ) )
            #\n does not give second line
        #widget.setDisabled( True )
        # no errors from these but do not seem effective
        widget.setLayoutDirection( Qt.RightToLeft )
        widget.setLayoutDirection( Qt.LeftToRight )
        layout.addWidget( widget )

        # ----  QRadioButton
        widget        = QRadioButton("AUSTRALIA")
        #radiobutton   = QRadioButton("AUSTRALIA")
        widget = QRadioButton('Left-Text Radio Button')
        widget.setChecked(True)  # Set as default selected
        widget.setLayoutDirection( Qt.RightToLeft )  # Set text layout direction to right-to-left textOnLeft
        widget.setLayoutDirection( Qt.LeftToRight )
        layout.addWidget( widget )

        layout.addLayout( button_layout,  )



        self.button_ex_1         = widget

        widget = QPushButton("mutate")
        self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )


        widget = QPushButton("ClearValues")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.clear_values( ) )
        button_layout.addWidget( widget )

        widget = QPushButton("SetValues")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.set_values( ) )
        button_layout.addWidget( widget )

        widget = QPushButton("Clip")
        # widget.clicked.con    # ------------------------------------nect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.clip( ) )
        button_layout.addWidget( widget )

        # ---- QPushButton("Open Messagebox")
        widget = QPushButton("Open Messagebox")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.show_message_box( ) )
        button_layout.addWidget( widget )


        # ---- PB inspect
        widget = QPushButton("inspect")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )



    # ------------------------------------
    def mutate( self ):
        """
        There is much more info to show

        """
        print( "\n\nmutate")


    # ------------------------------------
    def signal_sent( self, msg ):
        """

        """
        msg   = f"{function_nl}signal_sent"
        print( msg )
        print( f"signal_sent {msg}" )

    # ------------------------------------
    def put_in_clipboard( self, a_string ):
        """
        could you give me the code for putting a string in the qt clipboard
        """
        msg   = f"{function_nl}put_in_clipboard"
        print( msg )

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
        print( "\n\nclear_values")
        print( "clear_values self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??

    # ------------------------------------
    def set_values( self ):
        """
        There is much more info to show

        """
        print( "\n\nset_values")
        print( "set_values  self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "xxxxx" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??

    # --------
    def clip( self ):
        """
        """
        msg   = f"{function_nl}clip"
        print( msg )
        a_string    = self.line_edit_1.text()
        self.put_in_clipboard( a_string )

    # --------
    def cbox_clicked( self ):
        """
        """
        print( "\n\ncbox_clicked")
        cbox = self.sender()   # look into self.sender() looks like it might be standard !!
        print( "Animal " + (cbox.animal) + " is " + str(cbox.isChecked()))
        print( f"check box text() = { cbox.text()} ")

    # ---- signals sent -----------------------
    # --------------------------
    def on_editing_finished(self):
        print( "\n\non_editing_finished")
        print("Editing finished")

    # ------------------------------------
    def on_text_changed( self, new_text):
        print( "\n\non_text_changed")
        print(f"Text changed: {new_text}")

    # ------------------------------------
    def on_text_edited(self, new_text):
        print( "\n\on_text_edited")
        print(f"User edited text: {new_text}")

    # ------------------------------------
    def show_message_box( self ):
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


    # ------------------------------------
    def inspect( self ):
        """
        There is much more info to show

        """
        msg   = f"{function_nl}inspect"
        print( msg )
        print( f"{ self.line_edit_1.text() = }" )  # setText()   ??
        print( f"{ self.line_edit_1.isEnabled() = }" )  # setEnabled() no focus
        print( f"{ self.line_edit_1.isReadOnly() = }" )

        print( f"{ self.qlabel_1.text() = }" )  # setText() ??
        print( f"{ self.qlabel_1.text() = }" )

        print( f"{str( self.cbox_ex_1.isChecked()) = }" )

        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_qwidget_to_inspect   = QWidget()

        wat_inspector.go(
             msg            = "self.cbox_ex_1 from inspect method",
             inspect_me     = self.cbox_ex_1,
             a_locals       = locals(),
             a_globals      = globals(), )


    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()


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

        # opened on right hand monitor
        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 3000
        qt_height   = 600

        # opens on main monitor
        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 1400
        qt_height   = 700



        self.tab_help_dict   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )
        self.doc_dir             = "./docs/"
        self.build_gui()
        self.current_tab_index   = 0   # I need to track in changed


    def build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( "QtWidgetExamplesInTabs" )
        #self.setIcon( QMessageBox.Warning) #
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
        self.tab_widget.setTabsClosable( True)   # Allows you to enable or disable the close button on tabs.
        self.tab_widget.setMovable( True )         #

        layout.addWidget( self.tab_widget   )

        # ---- Draft
        tab      = uft.SeperatorTab()
        title    = "Draft\n>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QTextEdit
        title    = "QTextEdit\n"
        tab      = QTextEditTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "text_edit_tab.txt"

        # ---- TBD
        tab      = uft.SeperatorTab()
        title    = "TBD\n>>"
        self.tab_widget.addTab( tab, title  )

        title    = "Smaller\nWidgetTab"
        tab      = SmallerWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "little_widdget_tab.txt"

        title    = "QQComboBox\n"
        tab      = QComboBoxWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "combo_box_widdget_tab.txt"

        title    = "QDateEdit\n"
        tab      = QDateEditTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "date_edit_widdget_tab.txt"

        title    = "QGroupBox"
        tab      = QGroupBoxTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "group_Widget_tab.txt"

        title    = "QLayout\n"
        tab      = QLayoutWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "layout_Widget_tab.txt"

        title    = "QGridLayout\nWidgetTab"
        tab      = GridLayoutWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "layout_Widget_tab.txt"

        title    = "QList\nWidgetTab"
        tab      = QListWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "list_widdget_tab.txt"


        # ---- Done
        tab      = uft.SeperatorTab()
        title    = "Done\n>>"
        self.tab_widget.addTab( tab, title  )

        # ---- Template
        title    = "Template\nCopy"
        tab      = TemplateCopyMeWidgetTab()
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "template_copy_me_tab.txt"


    # ------------------------------------
    def build_menu( self,  ):
        """
        what it says read:

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
        index = self.tab_widget.currentIndex()
        self.tab_widget.setCurrentIndex(2)  # Set the active tab by index



        current_widget =  self.tab_widget.currentWidget( )


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

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
            still needs work
        """
        tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
        # print( f"{self.doc_dir}{tab_title = }")

        doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        doc_name            = f"{self.doc_dir}{doc_name}"
        print( f"{doc_name = }")
        ex_editor          = r"xed"

        proc               = subprocess.Popen( [ ex_editor, doc_name ] )

    #----------------------------
    def not_implemented( self,   ):
        """
        what it says read:
        """
        QMessageBox.information(self, "Not Implemented", "Working on this...")

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

    def tab_page_info( self ):
        """
        what it says, read it
        """
        nb    = self.tab_widget
        print(f"nb.select()  >>{nb.currentIndex() = }<<")
        print(f'>>{nb.tabText(nb.currentIndex()) = }<<')
        # print(f'{ nb.index("current" ) = }' )

    #-----------------------------------------------
    def build_list_widget_tabxxx(self,   ):
        """

        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )

        widget        = QListWidget(    )
        widget.setGeometry( 50, 50, 200, 200 )
        layout.addWidget( widget )

        #widget.itemClicked.connect( self.activate_clicked_command )

        values    =  [ "one", "two"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )

        widget.clear()

        values    =  [ "oneish", "twoish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2

            widget.setCurrentRow(index_to_select)

        ia_qt.q_list( widget )

        return tab_page



    # ---- build_layout_tab -----------------------------------------------------
    # #-----------------------------------------------
    # def build_layout_tabxxxx(self,   ):
    #     """
    #     build a tab to show off layout widgets
    #     """
    #     tab_page      = QWidget()
    #     layout        = QVBoxLayout( tab_page )

    #     layout_a     = QHBoxLayout(    )
    #     layout.addLayout( layout_a )
    #     self.layout_tab_layout_a   = layout_a

    #     self.widget_ix              = 22
    #     widget                      = QPushButton( f"Button   {self.widget_ix}")
    #     layout_a.addWidget( widget )
    #     self.layout_tab_button_1    = widget
    #     self.widget_temp            = widget

    #     layout_b     = QHBoxLayout(    )
    #     layout.addLayout( layout_b )

    #     widget = QPushButton("show_values")
    #     layout_b.addWidget( widget )

    #     widget = QPushButton("remove_add_widget")
    #     layout_b.addWidget( widget )
    #     widget.clicked.connect( lambda: self.remove_add_widget_layout_tab() )

    #     widget = QPushButton("replace_widget")
    #     layout_b.addWidget( widget )
    #     widget.clicked.connect( lambda: self.replace_widget_layout_tab() )
    #    # --------
    #     widget = QPushButton( "minimize" )  # showminimized iconify
    #     layout_b.addWidget( widget )
    #     widget.clicked.connect(lambda: self.iconify( ))

    #     return tab_page

    # #-----------------------------------------------
    # def remove_add_widget_layout_tab( self, ):
    #     """
    #     deletes and adds but position may change
    #     """
    #     print( "replace widget is better may need delete later ")
    #     self.widget_ix             += 1
    #     widget = QPushButton("Button + str(self.widget_ix)")

    #     #layout_b.addWidget( widget )

    #     self.layout_tab_layout_a.removeWidget( self.widget_temp  )
    #     self.widget_temp   = widget
    #     # button1.deleteLater()  # Optionally delete the old widget
    #     self.layout_tab_layout_a.addWidget( widget )

    # #-----------------------------------------------
    # def replace_widget_layout_tab( self, ):
    #     """
    #     deletes and adds but position may change
    #     """
    #     print( "replace_widget_layout_tab")
    #     widget                      = self.widget_temp
    #     self.widget_ix             += 1
    #     widget_new                  = QPushButton( f"Button   {self.widget_ix}")
    #     #self.keep_me                = widget_new
    #     # stop from delete

    #     self.replace_layout_widget( self.layout_tab_layout_a, widget, widget_new )
    #     self.widget_temp            = widget_new

    #     # print( f"{widget}")
    #     # print( f"{widget_new}")

    # def replace_layout_widget( self, layout, widget, widget_new ):
    #     """
    #     function should work copy and paste
    #     will be a problem if widget is not found in layout

    #     Args:
    #         layout (TYPE): DESCRIPTION.
    #         widget (TYPE): DESCRIPTION.

    #     """
    #     # print( f"{widget}")
    #     # print( f"{widget_new}")
    #     # Find the index of the existing widget
    #     index               = layout.indexOf( widget )
    #     print( f"widget at {index}")
    #     # Remove the old widget
    #     widget_to_remove    = layout.takeAt(index).widget()

    #     # see if this is causing a problem
    #     if widget_to_remove:
    #         widget_to_remove.deleteLater()

    #     # Insert the new widget at the same index
    #     layout.insertWidget( index, widget_new )



    # def table_widget_no_edit(self,  ):
    #     """
    #     from chat

    #     """
    #     table = self.table
    #     for row in range(table.rowCount()):
    #         for column in range(table.columnCount()):
    #             item = table.item(row, column)
    #             if item is not None:
    #                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)



    # def table_widget_add_row(self, data=None):
    #     """
    #     Method to add a row with optional data

    #     """
    #     row_position = self.table.rowCount()
    #     self.table.insertRow(row_position)

    #     # If data is provided, set it in the cells
    #     if data:
    #         for i, item in enumerate(data):
    #             self.table.setItem(row_position, i, QTableWidgetItem(item))

    # # Method to delete the selected row
    # def table_widget_delete_row(self):
    #     selected_row = self.table.currentRow()
    #     if selected_row >= 0:
    #         self.table.removeRow(selected_row)

    # # Method to edit a particular cell
    # def table_widget_edit_cell(self, row, column, new_value):
    #     self.table.setItem(row, column, QTableWidgetItem(new_value))

    # # Example method to add an item to a particular cell
    # def table_widget_add_item(self, row, column, value):
    #     self.table.setItem(row, column, QTableWidgetItem(value))

    # ---- button tab ------------------------------------------------
    def build_button_tab(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        1/0
        tab_page      = QWidget()

        layout        = QVBoxLayout( tab_page )

        # ---- combo_1
        widget        = QComboBox()
        self.combo_1  = widget

        widget.addItem('Zero')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')

        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        layout.addWidget( widget )

        # ---- combo_2
        widget        = QComboBox()
        self.combo_2  = widget

        widget.addItem('Zero')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')
        #widget.editable( True )
        widget.setEditable( True )

        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        layout.addWidget( widget )

        # ---- bittpms
        label       = "combo_reload"
        widget = QPushButton( label )
        widget.clicked.connect( self.combo_reload )

        layout.addWidget( widget )

        # ----
        label       = "combo_info"
        widget = QPushButton( label )
        widget.clicked.connect( self.combo_info )

        layout.addWidget( widget )

        return tab_page



    # --------
    def get_layout_widgets(self, layout):
        """

        Args:
            layout (TYPE): DESCRIPTION.

        Returns:
            None.

        """
        widgets = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                widgets.append(item.widget())
            elif item.layout():
                # recursion
                widgets.extend( self.get_layout_widgets( item.layout() ) )
        # return widgets
        for widget in widgets:
            print(type(widget).__name__)

    # --------
    def current_text_changed(self, s):
        """

        """
        print("Current text: ", s)

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


    # --------
    def print_message(self, text):
        print("Button clicked:", text)

     # --------
    def make_partial_widget_clicked( self, widget):
        """
        """
        from   functools import partial
        a_partial_foo       = partial( self.widget_clicked,  widget = widget )  # will set first arg    # --------

        return a_partial_foo

    # --------
    def widget_clicked( self, widget):
        """
        alterternative button clicked function
        seems like will not work with labmda instead use make_partial_widget_clicked
        """
        print( "widget_clicked" )
        print( f"widget >{widget}<")
        print( f"widget.text() >{widget.text()}<")

    # ----
    def iconify( self ):
        """

        """
        self.showMinimized()   # for minimizing your window

    # --------
    def close_event(self, event):
        """

        Args:
            event (TYPE): DESCRIPTION.

        Returns:
            None.

        """
        if self.popup_question():
            print("The program was shut down.")
            event.accept()
        else:
            print("not exiting")
            event.ignore()

    # --------
    def popup_question(self):
        """
        Generate a popup that requests if you want to do something or not.
        here exit the application --- see close_event
        """
        msgbox =  QMessageBox()
        msgbox.setWindowTitle("Whatever title you want to add.")
        msgbox.setIcon( QMessageBox.Warning)
        msgbox.setText("Do you want to quit WidgetExample?")
        botonyes =  QPushButton("Yes")
        msgbox.addButton(botonyes, QMessageBox.YesRole)
        botonno =  QPushButton("No")
        msgbox.addButton(botonno, QMessageBox.NoRole)
        msgbox.exec_()
        if msgbox.clickedButton() == botonno:
            return False
        else:
            return True

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

        proc               = subprocess.Popen( [ TEXT_EDITOR, file_name ] )



# --------------------
if __name__ == "__main__":

    TEXT_EDITOR   = "xed"
    app     = QApplication(sys.argv)
    dialog  = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog


    window  = QtWidgetExamples()
    window.show()
    #sys.exit(
    app.exec()

    sys.exit( 0 )


# ---- eof