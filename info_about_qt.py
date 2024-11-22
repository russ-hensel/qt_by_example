#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:36:24 2024

@author: russ
"""

# ---- imports neq qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QSizePolicy
from PyQt5.QtCore import QDate, Qt,  QSize
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtGui
from PyQt5.QtGui import QTextDocument

# sql
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlRelation,
                         QSqlRelationalDelegate, QSqlRelationalTableModel,
                         QSqlTableModel)

from PyQt5.QtCore  import  (
    QTimer,
    QDate,
    Qt,
    QModelIndex,
    QDateTime,
    QAbstractTableModel,
    pyqtSlot,
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


# widgets bigger
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
    QSqlQuery,
    QSqlRecord,
    QSqlField,
    )


# ---- end imports



DEBUGGING       = False  # in testing may be changed externally

indent_0        = "   " # used for formatting
INDENT          = "    "
INDENT2         = INDENT

MAX_REPR_LEN    = 150 #
MAX_STR_LEN     = 150 #
MAX_LIST_ITEMS  = 8

NEW_LINE        = "\n"

joe = f"joe{NEW_LINE}then some more "

if DEBUGGING:
    pass



common_dir_items  = (
['__module__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__weakref__',
 '__doc__',
 '__hash__',
 '__new__',
 '__init__',
 '__dict__',
 '__repr__',
 '__str__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__sizeof__',
 '__dir__',
 '__class__']
)

more_common_dir_items  = (
[ "__iter__", "__mod__", "__rmod__",

 "__len__", "__getitem__", "__add__", "__mul__", "__rmul__", "__contains__" ] )

common_dir_items = common_dir_items  + more_common_dir_items


# ---------------------
def to_columns( item_list, format_list = ( "{: <30}", "{:<30}" ), indent = "    "  ):
    """
    for __str__  probably always default format_list
    see ColunmFormatter which is supposed to be more elaborate version
    see its __str__
    ex:
        import string_util
        a_str     = string_util.to_columns( a_str, ["column_data",    f"{self.column_data}"  ] )
        a_str     = string_util.to_columns( a_str,
                                            ["column_data",    f"{self.column_data}"  ],
                                            format_list = ( "{: <30}", "{:<30}" )
    """
    #rint ( f"item_list {item_list}.............................................................. " )
    line_out  = ""
    for i_item, i_format in zip( item_list, format_list ):
        a_col  = i_format.format( i_item )
        line_out   = f"{indent}{line_out}{a_col}"
    # if current_str == "":
    #     ret_str  = f"{line_out}"
    # else:
    #     ret_str  = f"{current_str}\n{line_out}"

    return line_out


# ---------------------
def to_columns_old( current_str, item_list, format_list = ( "{: <30}", "{:<30}" ), indent = "    "  ):
    """
    for __str__  probably always default format_list
    see ColunmFormatter which is supposed to be more elaborate version
    see its __str__
    ex:
        import string_util
        a_str     = string_util.to_columns( a_str, ["column_data",    f"{self.column_data}"  ] )
        a_str     = string_util.to_columns( a_str,
                                            ["column_data",    f"{self.column_data}"  ],
                                            format_list = ( "{: <30}", "{:<30}" )
    """
    #rint ( f"item_list {item_list}.............................................................. " )
    line_out  = ""
    for i_item, i_format in zip( item_list, format_list ):
        a_col  = i_format.format( i_item )
        line_out   = f"{indent}{line_out}{a_col}"
    if current_str == "":
        ret_str  = f"{line_out}"
    else:
        ret_str  = f"{current_str}\n{line_out}"
    return ret_str


def short_repr( a_obj, max_len = MAX_REPR_LEN ):
    """
    make a repr, shorten if too long
    read code
    consider ret of is truncated in tuple

    """
    a_str  = repr( a_obj )

    if len( a_str ) > max_len:
        a_str  = a_str[ :max_len ] + "..."

    return a_str

# -----------
def short_str( a_obj, max_len = MAX_STR_LEN ):
    """
    make a str, shorten if too long
    read code
    consider ret of is truncated in tuple

    """
    a_str  = repr( a_obj )

    if len( a_str ) > max_len:

        a_str  = a_str[ :max_len ] + "..."
    return a_str


# ----------------------------------------
class InfoAbout(   ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        Usual init see class doc string
        """
        # this is the constructor run when you create
        # like  app = AppClass( 55 )
        self.info_provider_list    = []
        self.add_defined_inspectors()

        self.info_about_base       = InfoAboutBase()


    # ----------------------
    def add_inspectors( self, list_of_inspectors   ):
        """
        """
        for i_inspector in list_of_inspectors:
            self.add_inspector( i_inspector )

    # ----------------------
    def add_defined_inspectors( self,   ):
        """
        """
        an_inspector   = InfoAboutQLineEdit(  )
        self.add_inspector( an_inspector )

        # an_inspector   = InfoAboutList(  )
        # self.add_inspector( an_inspector )

        # an_inspector   = InfoAboutQTextEdit(  )
        # self.add_inspector( an_inspector )

        an_inspector   = InfoAboutQSqlRelationalTableModel(  )
        self.add_inspector( an_inspector )

        self.add_inspector( InfoAboutQTextEdit() )
        self.add_inspector( InfoAboutQTableView() )
        self.add_inspector( InfoAboutTableModel() )
        self.add_inspector( InfoAboutQComboBox()  )
        #self.add_inspector(   )
        #self.add_inspector(   )


    # ----------------------
    def add_inspector( self, info_provider_instance  ):
        """
        """
        self.info_provider_list.append( info_provider_instance )

    # ----------------------
    def get_info( self,
                    inspect_me,
                    *,
                    msg      = None,
                    max_len  = None,
                    xin      = "",
                    print_it = True,
                    sty      = "",
                    include_dir  = False,  ):
        """
        this is what we call to actually do an inspection
        """
        info  = None

        # print( self.info_provider_list )
        # debug_provider_list    = self.info_provider_list


        for i_info_provider in self.info_provider_list:
            if  i_info_provider.have_info_for( inspect_me ):
                print( "---------------")
                info = i_info_provider.get_info(
                         inspect_me,
                         msg      = None,
                         max_len  = None,
                         xin      = "",
                         print_it = True,
                         sty      = "",
                         include_dir  = False,
                        )
                break

        if info is None:
            #info = "no_info"
            info = self.info_about_base.get_info(
                     inspect_me,
                     msg      = None,
                     max_len  = None,
                     xin      = "",
                     print_it = True,
                     sty      = "",
                     include_dir  = False,
                    )

        return info

        #self.info_provider_instance.append( info_provider_instance )

    #----------- debug -----------
    #----------- main functions -----------


class InfoAboutBase(   ):
    """
    lots may be implemented as utations
    """
    MSG_PREFIX  = "\n>>>> "
    #----------- init -----------
    def __init__(self,       ):
        """
        Usual init see class doc string
        """
        self.reset()
        self.my_class    = None

    #---------------------
    def reset( self, ):
        """ """
        self.msg                   = ""
        self.line_list             = []
        #self.

    # --------------------------
    def have_info_for( self, a_obj ):

        return isinstance(  a_obj, self.my_class   )

    # def have_info_for( self, obj ):
    #     """ """
    #     have_info  = isinstance(  obj, self.my_class  )
    #     return have_info

    # ------------------------
    def get_info( self,
                    inspect_me,
                    *,
                    msg             = None,
                    max_len         = None,
                    xin             = "",
                    print_it        = True,
                    sty             = "",
                    include_dir     = False,
                    details_only    = False, ):
        """ """
        self.reset()

        self.inspect_me     = inspect_me
        self.msg            = msg
        self.max_len        = max_len
        self.xin            = xin
        self.print_it       = print_it
        self.sty            = sty
        self.include_dir    = include_dir
        self.details_only   = details_only
        self.fix_msg( )

        self.begin_info()
        self.mid_info()
        self.custom_info()

        self.dir_info()

        info                =  NEW_LINE.join( self.line_list )

        return info

    # ----------------------------------------
    def  dir_info( self  ):
        """
        Purpose:
            list out some __dir__() info as a string

            <class 'PyQt5.QtSql.QSqlError.ErrorType'>
            databaseText
            a_atter = <built-in method databaseText of QSqlError object at 0x7f84245a0350>
            driverText
            a_atter = <built-in method driverText of QSqlError object at 0x7f84245a0350>
            isValid
            a_atter = <built-in method isValid of QSqlError object at 0x7f84245a0350>

            might be nice to shorten or declutter items

        """
        if  not self.include_dir:
            # self.line_list.append(  f"include_dir IS FALSE " )
            return

        #msg       = f"directory (non standard items) for object of type {type( a_obj ) = }"
        #msg       = f"directory (non standard items):"
        #print( msg )

        the_dir         = self.inspect_me.__dir__()
        reduced_dir     = [ i_dir  for   i_dir in the_dir if i_dir not in common_dir_items ]
        reduced_dir.sort()
        current_str     = ""
        for i_dir in reduced_dir:

            # clean it up a bit ??
            #print( i_dir )
            a_atter     =   getattr( self.inspect_me, i_dir, None )
            # if a_atter.startswith( "<built-in method" ):
            #     a_atter  = "method"
            # if a_atter.startswith( "<built-in method" ):
            #     a_atter  = "method"

            #print( f"{i_dir= } .... {a_atter = }", flush = True )
            # to_columns( current_str, item_list, format_list = ( "{: <30}", "{:<30}" ), indent = "    "  ):

            current_str = to_columns(  [ str( i_dir ), str( a_atter) ] )
            self.add_line( current_str )

    # -----------------------
    def add_line( self, i_line ):
        """
        this is info for all
        """
        self.line_list.append( i_line )

    #-------------------------
    def mid_info( self ):
        """
        this is info for all
        """
        #self.add_line(  "so it begins" )
        self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        self.add_line(   "" )

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
        """
        self.add_line( f"{self.xin}{INDENT2}custom_info from info about base to be done " )
        #self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )

    # ------------------------------
    def begin_info( self ):
        """
        this is info for all
        """
        self.add_line(  "so it begins" )
        self.add_line( f"object is an instance of {type( self.inspect_me)}" )

        a_srep      = short_str( self.inspect_me )
        self.add_line( f">>>>>>>>>>{self.xin}{INDENT}>{a_srep}<" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        self.add_line(   "end of begin " )
        # a_srep  = short_str( a_obj )
        # a_str   = f"{a_str}\n{xin}{INDENT}>{a_srep}<"

        # a_str   = f"{a_str}\n{xin}{INDENT2}type is = { str( type(a_obj) ) }"
        # #a_str   = f"{a_str}\n{xin}{INDENT2}str     = {str( a_obj )}"
        # a_repr  = short_repr( a_obj )
        # a_str   = f"{a_str}\n{xin}{INDENT2}repr    = {a_repr}"


    # ------------------------
    def fix_msg( self ):
        """ """
        if self.msg is None:
            #self.msg  = default_msg( my_type_str )
            self.msg         = f"{self.MSG_PREFIX}for instance of  {type( self.inspect_me )}"

        else:
            self.msg = f"{self.MSG_PREFIX}{self.msg} "

    # ------------------------
    def return_info( self ):
        """ """
        info       = "\n".join( self.line_list )




# ---- now the actual cases --------------------------------
# -----------------------------------
class InfoAboutxxx( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = str

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a str  " )

        self.add_line(  f"{self.xin}{INDENT2}{obj.xxxx() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )


        #self.add_line(  f"{self.xin}{INDENT2}toPlainText()            = {self.inspect_me.toPlainText() }" )
        # ix = 0
        # for  i_key, i_value in self.inspect_me.items():

        #     ix += 1
        #     if ix > MAX_LIST_ITEMS:
        #         more_items   = len(self.inspect_me) - MAX_LIST_ITEMS
        #         self.add_line( f"{self.xin}{INDENT}and{more_items} more items.... " )
        #         #a_str   = f"{a_str}\n{xin}{INDENT}and {len(a_obj) - max_items} more items.... "
        #         break

        #     self.add_line( f"{self.xin}{INDENT} {i_key = } {i_value = }" )

class InfoAboutQSqlRecord( QSqlRecord  ):

    #----------- init -----------
    def __init__(self,   ):

        """
        look at relationaltable see if some stuff should be moved here
        """

        super( ).__init__(     )
        self.my_class    = str

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlRecord -- !! indents are a mess" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.count() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isEmpty() = }" )
        # self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )
        # self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )
        # self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )

        column_count   = obj.count( )
        # bad isea ?
        for  ix, ix_field in enumerate( list( range( column_count ) ) ):

            if ix > MAX_LIST_ITEMS:
                more_items   = column_count - MAX_LIST_ITEMS
                self.add_line( f"{self.xin}{INDENT}and{more_items} more items.... " )
                break

            self.add_line( f"{self.xin}{INDENT2}{obj.fieldName( ix_field ) = } {obj.field( ix_field ).value() = }" )

            field   = obj.field( ix_field )
            f       = field
            self.add_line( f"{f.isAutoValue( ) = } {f.isGenerated( ) = } "
                           f"{f.isNull() = }  {f.isReadOnly( ) = } {f.isValid( ) = }  " )
            # self.add_line( f"{INDENT2}      field_info = {field_info}" )

# -----------------------------------
class InfoAboutQSqlDatabase( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QSqlDatabase

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlDatabase" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )


        self.add_line(  f"{self.xin}{INDENT2}{obj.tables() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.database() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.databaseName() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )


# -----------------------------------
class InfoAboutQSqlQuery( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QSqlQuery

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlQuery" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.bindValue() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.boundValues() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isActive() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isSelect() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isValid()  = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.lastError() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.lastInsertId() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.lastQuery() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.record() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.size()  = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.value( 1 )  = }" )




# -----------------------------------
class InfoAboutQComboBox ( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QComboBox

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QComboBox   " )

        a_srep  = short_str( obj )


        self.add_line(  f"{self.xin}{INDENT2}{a_srep }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.count() = }       " )
        self.add_line(  f"{self.xin}{INDENT2}{obj.maxVisibleItems() = }       " )



# -----------------------------------
class InfoAboutQLineEdit( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QLineEdit



# -----------------------------------
class InfoAboutQTextEdit( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        Usual init
        """
        super( ).__init__(     )
        self.my_class    = QTextEdit

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
        """
        self.add_line(  "custom_info for a qtext_edit" )
        #self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )

        self.add_line(  f"{self.xin}{INDENT2}toPlainText()            = {self.inspect_me.toPlainText() }" )

         #     self.add_line( f"{self.xin}{INDENT2}>{i_value}<" )

# -----------------------------------
class InfoAboutQTableView( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QTableView

    # --------------------------
    def have_info_forxxx( self, a_obj ):

        have_info  = isinstance(  a_obj,  QTableView  )
        return have_info

    #-------------------------
    def custom_info( self ):

        self.add_line(  "custom_info for a QTableView tbd" )
        #self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )
        its             = self.inspect_me

        self.add_line(  f"{self.xin}{INDENT2}currentIndex()             = {self.inspect_me.currentIndex() }" )
        self.add_line(  f"{self.xin}{INDENT2}alternatingRowColors()     = {self.inspect_me.alternatingRowColors() }" )
        self.add_line(  f"{self.xin}{INDENT2}frameWidth()               = {self.inspect_me.frameWidth() }" )
        self.add_line(  f"{self.xin}{INDENT2}hasAutoScroll()            = {self.inspect_me.hasAutoScroll() }" )
        self.add_line(  f"{self.xin}{INDENT2}{its.isSortingEnabled() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{its.maximumHeight() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{its.objectName() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{its.width() = }" )

        # ---- work thr colums which depends on model
        model           = its.model()
        if model is not None:
            column_count = model.columnCount()
            print(f"Number of columns: {column_count}")
        else:
            column_count  = 0
            print("No model set for this QTableView.")

        self.add_line(  f"{self.xin}{INDENT2}model for view             = { model }" )

        ix = 0
        for  ix_col in range( column_count ):

            ix += 1
            if ix > MAX_LIST_ITEMS:
                more_items   = column_count - MAX_LIST_ITEMS
                self.add_line( f"{self.xin}{INDENT}and{more_items} more items.... " )
                break

            self.add_line( f"{self.xin}{INDENT} {ix_col = } {its.isColumnHidden( ix_col ) = }" )

# -----------------------------------
class InfoAboutQAbstractTableModell( InfoAboutBase  ):
    """
    About this class.....

    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QAbstractTableModel

    #-------------------------
    def custom_info( self ):

        obj           = self.inspect_me
        self.add_line(  "custom_info for a QAbstractTableModel" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.rowCount() = }" )

        if False:
            pass
            # row_count       = model.rowCount()
            # column_count    = model.columnCount()
            # for ix_row in range( row_count ):
            #     if ix_row > MAX_LIST_ITEMS:
            #         self.add_line(  f"{self.xin}{INDENT2} and more lines not listed...... " )
            #         break

            #     for ix_col  in range( 3 ):   # should figure out a column count
            #         index     = model.index( ix_row,   ix_col   )
            #         data      = model.data( index )
            #         msg       = f"for {ix_row = } {ix_col = } {index = } {data = }"
            #         self.add_line(  f"{self.xin}{INDENT2} {msg}" )




# -----------------------------------
class InfoAboutTableModel( InfoAboutBase  ):
    """
    About this class.....
    is this to close to relationaltablemodel??
    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QSqlTableModel

    #-------------------------
    def custom_info( self ):

        model           = self.inspect_me
        self.add_line(  "custom_info for a QSqlTableModel" )

        self.add_line(  f"{self.xin}{INDENT2}rowCount()     = {model.rowCount() }" )

        row_count       = model.rowCount()
        column_count    = model.columnCount()
        for ix_row in range( row_count ):
            if ix_row > MAX_LIST_ITEMS:
                self.add_line(  f"{self.xin}{INDENT2} and more lines not listed...... " )
                break

            # check for max ??
            for ix_col  in range( column_count ):   # should figure out a column count
                index     = model.index( ix_row,   ix_col   )
                data      = model.data( index )
                msg       = f"for {ix_row = } {ix_col = } {index = } {data = }"
                self.add_line(  f"{self.xin}{INDENT2} {msg}" )

# -----------------------------------
class InfoAboutQSqlRelationalTableModel( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QSqlRelationalTableModel

    #-------------------------
    def custom_info( self ):
        """
        gen the custom lines
        """
        model           = self.inspect_me
        self.add_line(  "Custom_info for a QSqlRelationalTableModel" )

        # we can get counts and the get ix from name an vise versa also the data
        row_count       = model.rowCount()
        column_count    = model.columnCount()

        self.add_line(  f"{self.xin}{INDENT2}For the model " )
        self.add_line(  f"{self.xin}{INDENT2}  {model.rowCount() = } {model.columnCount() = } " )

        for ix_row in range( row_count ):
            if ix_row > 3* MAX_LIST_ITEMS:
                self.add_line(  f"{self.xin}{INDENT2} and more rows not listed...... " )
                break

            print( "" ) # marker for new row
            c_names         = []
            for ix_col  in range( column_count ):   # should figure out a column count
                index       = model.index( ix_row,   ix_col   )
                data        = model.data( index )
                #field       = model.fieldIndex( ix_col )  # f
                c_header    = model.headerData( ix_col, Qt.Horizontal)
                    # russ not sure this is accurate all the time look at record next mith text
                field       = model.fieldIndex( c_header )  # may be error in some cases
                        # If you're working with a QSqlRelationalTableModel that has relations set, the column name
                        # returned will reflect the field name from the base table, not the related table.
                #field       = model.fieldIndex( c_header )  # might work
                c_names.append( c_header )
                msg       = f"for model {ix_row = } {ix_col = } {c_header = } { field = }  {data = }"
                self.add_line(  f"{self.xin}{INDENT2}{msg}" )

        # self.add_line(  "Custom_info for a QSqlRelationalTableModel" )
        # for ix_col in range(model.columnCount()):
        #     header   = model.headerData( ix_col, Qt.Horizontal)
        #     self.add_line(f"{self.xin}{INDENT2} Column {ix_col}: {header}")

        self.add_line(  f"{self.xin}{INDENT2}For a record .. anything new here -- columns differ " )
        # grabbed fromtab_qsl relational  --- does record have a column count?
        new_record      = model.record()
        c_names         = []
        max_col         = new_record.count()
        for ix_col in range( max_col ):    # seems ok to index past end
            i_name     = new_record.fieldName( ix_col )
            c_names.append( i_name )
            self.add_line( f"{self.xin}{INDENT2}{ix_col = }:     {new_record.fieldName( ix_col ) = } " )
                # chat says still works afteer heder may be changed
        #c_names      = [ "name", "phone_number", "xxx"]
        for i_name in c_names:
            self.add_line( f"{self.xin}{INDENT2}{i_name = }:  {new_record.indexOf( i_name ) = } " )

        # print( "did this get left off ?" )
        # print( f'{ model.fieldIndex( "person_id") = }' )

# ---- main
# --------------------
if __name__ == "__main__":
    #----- for running examples

    info_about     = InfoAbout( )

    info_about.add_defined_inspectors()

    info            = info_about.get_info( 10 * [ 1, 2, 3, 4] ,
                                        msg          = "here is a list with more args",
                                        max_len      = None,
                                        xin          = "",
                                        print_it     = True,
                                        sty          = "",
                                        include_dir  = False,  )
    print( info )

    info            = info_about.get_info( ( "a", "b", "c" ) ,
                                        msg          = "here is a set s",
                                        max_len      = None,
                                        xin          = "",
                                        print_it     = True,
                                        sty          = "",
                                        include_dir  = False,  )
    print( info )


    # ---- next
    # do not construct out of context
    # inspect_this     = QLineEdit()

    # info            = info_about.get_info( inspect_this ,

    #                                     msg          = "here is a list with more args",
    #                                     max_len      = None,
    #                                     xin          = "",
    #                                     print_it     = True,
    #                                     sty          = "",
    #                                     include_dir  = False,  )


    # print( info  )
# --------------------
    #call_tbl()

# ---- eof
