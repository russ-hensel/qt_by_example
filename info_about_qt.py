#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
explore some of the attributes of Q Widgets


"""
# ---- search
"""

non sql, non table

    QTextEdit
    QComboBox
    QListWidget
    QLineEdit
    QWidget

layouts

        QBoxLayout

non sql

    models
        QAbstractTableModel
        QTableWidget            -- model, view or both ?
            object is instance of <class 'PyQt5.QtWidgets.QTableView'> and type <class 'PyQt5.QtWidgets.QTableWidget'>


    views
        QTableView   -- use with ???

sql

    modeles
        QSqlRelationalTableModel
        QSqlTableModel
        QSqlQueryModel

    views

    components
        QSqlField
        QSqlError
        QSqlRecord
        QSqlDatabase
        QSqlQuery




"""

# ---- imports qt

from PyQt5 import QtGui
from PyQt5.QtCore import (QAbstractTableModel,
                          QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTimer,
                          pyqtSlot)

from PyQt5.QtGui import QTextCursor, QTextDocument

from PyQt5.QtSql import (QSqlDatabase,
                         QSqlError,
                         QSqlField,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)

from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QBoxLayout,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
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
                             QVBoxLayout,
                             QWidget)

# ---- end imports

doesitexist   = """

   my_type       =  QSqlTableWidget
       #a_str   = f"{a_str}\n{xin}{INDENT2}database()     = {a_obj.database() }"
       a_str   = f"{a_str}\n{xin}{INDENT2}rowCount()     = {a_obj.rowCount() }"
       # if a_obj.rowCount( ) > 0:

 """

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
        add all here to make available
        should be from most specialized to most general
        """


        self.add_inspector( InfoAboutQSqlRelationalTableModel() )

        self.add_inspector( InfoAboutQSqlTableModel() )

        self.add_inspector( InfoAboutQAbstractTableModel() )
        self.add_inspector( InfoAboutQTableWidget() )
        self.add_inspector( InfoAboutQTableView() )

        self.add_inspector( InfoAboutQTextEdit() )

        self.add_inspector( InfoAboutQLineEdit(  ) )
        self.add_inspector( InfoAboutQComboBox()  )
        self.add_inspector( InfoAboutQWidget()    )

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

    # ------------------------------
    def begin_info( self ):
        """
        this is info for all
        """
        #self.add_line(  "so it begins" )
        self.add_line( f"object is instance of {self.my_class} and type {type( self.inspect_me)}" )

        a_srep      = short_str( self.inspect_me )
        self.add_line( f">>>>>>>>>>{self.xin}{INDENT}>{a_srep}<" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "end of begin " )
        # a_srep  = short_str( a_obj )
        # a_str   = f"{a_str}\n{xin}{INDENT}>{a_srep}<"

        # a_str   = f"{a_str}\n{xin}{INDENT2}type is = { str( type(a_obj) ) }"
        # #a_str   = f"{a_str}\n{xin}{INDENT2}str     = {str( a_obj )}"
        # a_repr  = short_repr( a_obj )
        # a_str   = f"{a_str}\n{xin}{INDENT2}repr    = {a_repr}"

    #-------------------------
    def mid_info( self ):
        """
        this is info for all -- seems to all hav emove to begin.
        """
        #self.add_line(  "so it begins" )
        #self.add_line( f"object is of type {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
        """
        self.add_line( f"{self.xin}{INDENT2}custom_info from info about base to be done " )
        #self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )

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
class InfoAboutQWidget ( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QWidget

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QWidget   " )

        a_srep  = short_str( obj )

        self.add_line(  f"{self.xin}{INDENT2} QWidget {self.details_only = }" )


        if not self.details_only:
            self.add_line(  f"{self.xin}{INDENT2}{a_srep }" )

        # details
        self.add_line(  f"{self.xin}{INDENT2}{obj.hasHeightForWidth() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.height() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isEnabled() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.isVisible() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.layoutDirection() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.maximumHeight() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.maximumSize() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.maximumWidth() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.minimumWidth() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.objectName() = }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.sizeIncrement() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.sizePolicy() = }" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.windowType() = }" )

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

class InfoAboutQSqlRecord( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):
        """
        look at relationaltable see if some stuff should be moved here
        """
        super( ).__init__(     )
        self.my_class    = QSqlRecord

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





        look_into_this = """
        for ix_field in range( 0,field_count ):
            a_str   = f"{a_str}\n{xin}{INDENT2}    {ix_field}: name/value = {a_obj.fieldName( ix_field )} /  {a_obj.field( ix_field ).value() }"
            field   = a_obj.field( ix_field )
            f       = field
            field_info   = ( f"{f.isAutoValue( ) = } {f.isGenerated( ) = } "
                             f"{f.isNull() = }  {f.isReadOnly( ) = } {f.isValid( ) = }    ")

            #a_str   = f"{a_str}\n{xin}{INDENT2}      {ix_field}: field_info = {field_info}"
            a_str   = f"{a_str}\n{xin}{INDENT2}      field_info = {field_info}"   """


# -----------------------------------
class InfoAboutQSqlError( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QSqlError

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlError" )

        self.add_line(  f"{self.xin}{INDENT2}isValid()          = {obj.isValid() }" )
        self.add_line(  f"{self.xin}{INDENT2}databaseText()     = {obj.databaseText() }" )
        self.add_line(  f"{self.xin}{INDENT2}driverText()       = {obj.driverText() }" )
        self.add_line(  f"{self.xin}{INDENT2}driverText()       = {obj.driverText() }" )
        self.add_line(  f"{self.xin}{INDENT2}text()             = {obj.text() }" )

# -----------------------------------
class InfoAboutQSqlField( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QSqlField

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlField" )



        #self.add_line(  f"{self.xin}{INDENT2}type()         = {obj.type() }"   )
        self.add_line(  f"{self.xin}{INDENT2}typeID()       = {obj.typeID() }" )
        self.add_line(  f"{self.xin}{INDENT2}value()        = {obj.value() }"   )
        self.add_line(  f"{self.xin}{INDENT2}length()       = {obj.length() }" )



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
class InfoAboutQSqlQueryModel( InfoAboutBase  ):
    """
    nothing left for us in ia_qt
    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QSqlQueryModel

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QSqlQueryModel" )

        self.add_line(  "{xin}{INDENT2}lastError().isValid()    = {obj.lastError().isValid() }" )
        self.add_line(  "{xin}{INDENT2}lastError().text()       = {obj.lastError().text() }" )
        self.add_line(  "{xin}{INDENT2}rowCount()               = {obj.rowCount() } records" )
        if obj.rowCount( ) > 0:
            print( "need to fix this looper 6835")
            # a_str   = f"{a_str}\n{xin}{INDENT2}... records record(0):"
            # a_record    =  a_obj.record( 0 )
            # str_2       =  q_sql_record( a_record,
            #                             msg      = None,
            #                             max_len  = None,
            #                             xin      = "    ",
            #                             print_it = False,
            #                             sty      = "",
            #                             include_dir  = False,
            #                             details_only = True,
            #                     )

            # a_str   = f"{a_str}{str_2}"

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
class InfoAboutQListWidget ( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QListWidget

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QListWidget" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )


        self.add_line(  f"{self.xin}{INDENT2}count()            = {obj.count() }" )
        self.add_line(  f"{self.xin}{INDENT2}currentItem()      = {obj.currentItem() }" )
        self.add_line(  f"{self.xin}{INDENT2}item( 0 ).text( ) = {obj.item( 0 ).text( ) }" )

        current_item = obj.currentItem()
        if current_item:
            # Retrieve and show the text of the current item
            item_text = current_item.text()
        else:
             item_text = None

        self.add_line(  f"{self.xin}{INDENT2}current_item.text() = {item_text}" )

# -----------------------------------
class InfoAboutQComboBox ( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QComboBox

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        a_obj       = obj  # !! fix me
        self.add_line(  "custom_info about a QComboBox   " )

        # a_srep  = short_str( obj )
        # self.add_line(  f"{self.xin}{INDENT2}{a_srep }" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.count() = }       " )
        self.add_line(  f"{self.xin}{INDENT2}{obj.maxVisibleItems() = }       " )
        self.add_line(  f"{self.xin}{INDENT2}currentText()          = {a_obj.currentText() }"   )
        self.add_line(  f"{self.xin}{INDENT2}currentIndex()         = {a_obj.currentIndex() }"  )

        current_index       = a_obj.currentIndex()
        current_index_text  = a_obj.itemText( current_index )
        self.add_line(  f"{self.xin}{INDENT2}current_index_text     = {current_index_text}" )

        if current_index_text != a_obj.currentText():
            self.add_line(  f"{self.xin} current index text not equal to current text"  )

        for ix in range( a_obj.count()):
            value_at_index =  a_obj.itemText( ix )
            self.add_line(  f"{self.xin}    {INDENT2}value                  = {value_at_index}" )



# -----------------------------------
class InfoAboutQLineEdit( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QLineEdit

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
        """
        obj         = self.inspect_me
        a_obj       = obj  # !! fix me

        self.add_line(  "custom_info for a QLineEdit" )

        self.add_line(  f"{self.xin}{INDENT2}alignment()          = {a_obj.alignment() }"  )
        self.add_line(  f"{self.xin}{INDENT2}cursorPosition()     = {a_obj.cursorPosition() }" )

        self.add_line(  f"{self.xin}{INDENT2}hasAcceptableInput() = {a_obj.hasAcceptableInput() }" )
        self.add_line(  f"{self.xin}{INDENT2}isModified()         = {a_obj.isModified() }" )
        self.add_line(  f"{self.xin}{INDENT2}maxLength()          = {a_obj.maxLength() }" )
        self.add_line(  f"{self.xin}{INDENT2}placeholderText()    = {a_obj.placeholderText() }" )
        self.add_line(  f"{self.xin}{INDENT2}validator()          = {a_obj.validator() }" )
        self.add_line(  f"{self.xin}{INDENT2}text()               = {a_obj.text() }" )

# -----------------------------------
class InfoAboutQTableWidget( InfoAboutBase  ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__(self,   ):
        """
        Usual init
        """
        super( ).__init__(     )
        self.my_class    = QTableWidget

    #-------------------------
    def custom_info( self ):
        """
        this should be custom
                item     = QTableWidgetItem( "Cell ({}, {})".format( i, j) )
                table_widget.setItem(i, j, item)
        """
        self.add_line(  "custom_info for a QTableWidget" )
        #self.add_line( f"object is an instance of {type( self.inspect_me)}" )
        #a_str   = f"{xin}{a_str}for msg = {msg} object isinstance of Sequence"
        #self.add_line(   "" )

        obj   = self.inspect_me

        self.add_line(  f"{self.xin}{INDENT2}{obj.rowCount() =  }" )

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
class InfoAboutQAbstractTableModel( InfoAboutBase  ):
    """
    About this class.....
    nothing left in ia_qt
    """
    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )
        self.my_class    = QAbstractTableModel

    #-------------------------
    def custom_info( self ):

        obj           = self.inspect_me
        a_obj         = obj   # until fixed
        xin           = self.xin
        self.add_line(  "custom_info for a QAbstractTableModel  TableModel... this is incomplete and needs testing " )
        self.add_line(  "data exposed as list of lits of lists compare to QTableWidget" )
        self.add_line(  f"{self.xin}{INDENT2}{obj.rowCount() = }" )
        self.add_line(  f"{xin}{INDENT2}rowCount()               = {a_obj.rowCount() } records"  )
        self.add_line(  f"{xin}{INDENT2}_data                   = {a_obj._data  }    "      )
        self.add_line(  f"{xin}{INDENT2}_headers                = {a_obj._headers }    "    )



# -----------------------------------
class InfoAboutQSqlTableModel( InfoAboutBase  ):
    """
    About this class.....
    is this to close to relationaltablemodel?? or the  QSqlTableModel  isdirty
    """
    #----------- init -----------
    def __init__(self,   ):
        """ """
        super( ).__init__(     )
        self.my_class    = QSqlTableModel

    #-------------------------
    def custom_info( self ):
        """
        info just for this instance type
        """
        model           = self.inspect_me
        a_obj           = model   # needs fix
        obj             = model

        xin             = self.xin

        self.add_line(  "custom_info for a QSqlTableModel " )

        self.add_line(  f"{self.xin}{INDENT2}rowCount()     = {model.rowCount() }" )
        self.add_line(  f"{xin}{INDENT2}database()     = {a_obj.database() }" )

        self.add_line(  f"{xin}{INDENT2}rowCount()     = {a_obj.rowCount() }" )
        self.add_line(  f"{xin}{INDENT2}isDirty()      = {a_obj.isDirty() }" )

        more = """
        # choose onne
        max_dirty  = 5
        max_clean  = 5

        max_dirty  = max_rows
        max_clean  = max_rows

        ix_dirty   = 0
        ix_clean   = 0
        for ix_row in range( 0, a_obj.rowCount() ):
        #if a_obj.rowCount( ) > 0:
            # make an index
            # records do not seem to kno if they are dirty
            ix_col      = 1
            index       = a_obj.index(  ix_row, ix_col )
            is_dirty    = a_obj.isDirty( index )    # apparently field by field so....
            do_record   = False
            if   is_dirty and ( ix_dirty < max_dirty ):
                ix_dirty    += 1
                a_str        = f"{a_str}\n{xin}{INDENT2}index {ix_row}, {ix_col} isDirty()      = {is_dirty}"
                do_record    = True
            elif ( not is_dirty ) and ix_clean < max_clean:
                ix_clean    += 1
                a_str        = f"{a_str}\n{xin}{INDENT2}index {ix_row} {ix_col} isDirty()      = {is_dirty}"
                do_record    = True
            elif ( ix_clean >= max_clean ) and (ix_dirty >= max_dirty ):
                break


        """
        # ---- get based on dataa
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

        # ----- see if blows
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
        # ---- based on record
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

        print( "by records in model ")
        for ix_row in range( obj.rowCount()  ):
            record = obj.record(ix_row)  # obj = model

            for ix in range(record.count()):
                self.add_line( f"{self.xin}{INDENT2}Field by index {ix = } {record.fieldName(ix) = }: {record.value(ix) = }")
            # print( f"{record.value(ix_table_joined)}) {record.value(ix_table_id)})" )
            # record_key    = (record.value(ix_table_joined), record.value(ix_table_id))
            # print( f"{record_key = }")

        # print( "did this get left off ?" )

        # end see if blows ------------------

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

        # for now duplicate with InfoAboutQSqlTableModel
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

class InfoAboutQBoxLayout( InfoAboutBase  ):

    #----------- init -----------
    def __init__(self,   ):

        super( ).__init__(     )  # message
        self.my_class    = QBoxLayout

    #-------------------------
    def custom_info( self ):
        obj         = self.inspect_me
        self.add_line(  "custom_info about a QBoxLayout" )

        self.add_line(  f"{self.xin}{INDENT2}{obj.isOpen() = }" )

        self.add_line(  f"{self.xin}{INDENT2}children ()  = {obj.children () }" )
        self.add_line(  f"{self.xin}{INDENT2}count()      = {obj.count() }"  )

        self.add_line(  f"{self.xin}{INDENT2}dumpObjectInfo() = {obj.dumpObjectInfo() }"  )
        self.add_line(  f"{self.xin}{INDENT2}dumpObjectTree() = {obj.dumpObjectTree() }" )


        # a_str   = f"{a_str}\n{xin}{INDENT2}findChild()          = {a_obj.findChild() }"
        #     not enough arguments

        # a_str   = f"{a_str}\n{xin}{INDENT2}findChildren()    = {a_obj.findChildren() }"
        #     not enough arguments

        self.add_line(  f"{self.xin}{INDENT2}geometry()          = {obj.geometry() }" )
        self.add_line(  f"{self.xin}{INDENT2}isEnabled()         = {obj.isEnabled() }" )




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
