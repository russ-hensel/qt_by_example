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
        """
        info  = None
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
            info = "no_info"

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

    # def have_info_for( self, obj ):
    #     """ """
    #     have_info  = isinstance(  obj, self.my_class  )
    #     return have_info

    # ------------------------
    def get_info( self,
                    inspect_me,
                    *,
                    msg      = None,
                    max_len  = None,
                    xin      = "",
                    print_it = True,
                    sty      = "",
                    include_dir  = False,  ):
        """ """
        self.reset()

        self.inspect_me     = inspect_me
        self.msg            = msg
        self.max_len        = max_len
        self.xin            = xin
        self.print_it       = print_it
        self.sty            = sty
        self.include_dir    = include_dir

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
        msg       = f"directory (non standard items):"
        #print( msg )

        the_dir         = self.inspect_me.__dir__()
        reduced_dir     = [ i_dir  for   i_dir in the_dir if i_dir not in common_dir_items ]
        reduced_dir.sort()
        current_str = ""
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
        self.add_line(  "so it begins" )
        self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        self.add_line(   "" )

    #-------------------------
    def custom_infoxx( self ):
        """
        this should be custom
        """
        self.add_line(  "custom_info" )
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


    # -----------------------------------
    def bar( self, ):
        """
        Purpose:
        Args:
        Return:
        """
        ret_val = "bar"
        return ret_val
    def _private(self):
        """
        """
        ret_val = "_private"
        return ret_val




# -----------------------------------
class InfoAboutList( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        Usual init see class doc string
        """
        super( ).__init__(     )  # message
        self.my_class    = list

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
        """
        self.add_line(  "custom_info for a list" )

        # list out some items
        ix = 0
        for  i_value in self.inspect_me:
            self.add_line( f"{self.xin}{INDENT2}>{i_value}<" )

            #a_str   = f"{a_str}\n{xin}{INDENT2}{i_value}"
            ix += 1
            if ix > MAX_LIST_ITEMS:
                more_items   = len(self.inspect_me) - MAX_LIST_ITEMS
                self.add_line( f"{self.xin}{INDENT}and{more_items} more items.... " )
                #a_str   = f"{a_str}\n{xin}{INDENT}and {len(a_obj) - max_items} more items.... "

                break
    # --------------------------
    def have_info_for( self, a_obj ):
        """
        """
        have_info  = isinstance(  a_obj, list  )
        return have_info

# -----------------------------------
class InfoAboutQLineEdit( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        Usual init see class doc string
        """
        super( ).__init__(     )  # message
        # this is the constructor run when you create
        # like  app = AppClass( 55 )

    # --------------------------
    def have_info_for( self, a_obj ):
        """
        """
        have_info  = isinstance(  a_obj, QLineEdit  )
        return have_info

    # called by str( instance of AppClass )
    def __str__(self):
        return "App Class __str__" + " self.arg = " + str( self.arg )
    # -----------------------------------
    def get_infoxxx( self,     msg             = None,
                            *,
                            max_len         = None,
                            xin             = "",
                            print_it        = True,
                            sty             = "",
                            include_dir     = False, ):
        """
        Purpose:
        Args:
        Return:
        """

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
    # --------------------------
    def have_info_for( self, a_obj ):
        """
        """
        have_info  = isinstance(  a_obj, QTextEdit  )
        return have_info

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

        # # list out some items
        # ix = 0
        # for  i_value in self.inspect_me:
        #     self.add_line( f"{self.xin}{INDENT2}>{i_value}<" )


        #     #a_str   = f"{a_str}\n{xin}{INDENT2}{i_value}"
        #     ix += 1
        #     if ix > MAX_LIST_ITEMS:
        #         more_items   = len(self.inspect_me) - MAX_LIST_ITEMS
        #         self.add_line( f"{self.xin}{INDENT}and{more_items} more items.... " )
        #         #a_str   = f"{a_str}\n{xin}{INDENT}and {len(a_obj) - max_items} more items.... "

        #         break


# ---- main
# --------------------
if __name__ == "__main__":
    #----- for running examples

    info_about     = InfoAbout( )

    an_inspector   = InfoAboutQLineEdit(  )
    info_about.add_inspector( an_inspector )

    an_inspector   = InfoAboutList(  )
    info_about.add_inspector( an_inspector )


    info            = info_about.get_info( 10 * [ 1, 2, 3, 4] ,
                                        msg          = "here is a list with more args",
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


    print( info  )
# --------------------
    #call_tbl()

# ---- eof