# -*- coding: utf-8 -*-


"""
    parameters    for  qt examples

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main()
# --------------------


import os
import logging
import sys

# ---- local imports
#import string_util
#from   app_global import AppGlobal
#import running_on

# ========================================
class Parameters( ):
    """
    manages parameter values: use it like an ini file but it is code
    """
    # -------
    def choose_mode( self ):
        """
        typically choose one mode
            and if you wish add the plus_test_mode
            if you comment all out all modes you get the default mode which should
            run, perhaps not in the way you want
        """
        self.mode_russ_on_theprof()
        #self.new_user_mode()
        #self.millhouse_1_mode()

        # two of my computers
        #self.mode_millhouse_mint()
        #self.mode_theprof_mint()
        #self.russ_1_mode()

        # --- add on for testing, use as desired edit mode for your needs
        #self.plus_test_mode()


    # ---- ---->> Methods:  one for each mode
    # -------
    def mode_russ_on_theprof( self ):
        """
        a mode for the new user, pretty much empty,
        a new user may experiment here.
        """
        self.mode               = "mode_russ_on_theprof"
        # but do they use the same units ?
        self.qt_width           = 1500
        self.qt_height          = 600    # 700 most of win height
        self.qt_xpos            = 10
        self.qt_ypos            = 10

    # -------
    def new_user_mode( self ):
        """
        a mode for the new user, pretty much empty,
        a new user may experiment here.
        """
        self.mode               = "mode new_user"

    # -------
    def running_on_tweaks(self,  ):
        """
        not a mode, a tweak to other modes , see documentation
        you need to customize this for your own computers, what you may
            find here are customization's for russ and his computers
        use running on tweaks as a more sophisticated
            version of os_tweaks and computer name tweaks which
        may replace them
        this is computer name tweaks code,
            !! find run_on on which uses os or put computer name under this
        """
        pass
        # self.os_tweaks()

        # computer_id    =   self.running_on.computer_id

        # if computer_id == "smithers":
        #     self.win_geometry       = '1450x700+20+20'      # width x height position
        #     self.ex_editor          =  r"D:\apps\Notepad++\notepad++.exe"
        #     self.db_file_name       =  "smithers_db.db"

        # # ---- bulldog
        # elif computer_id == "bulldog":
        #     self.ex_editor          =  r"gedit"
        #     self.db_file_name       =  "bulldog_db.db"


        # elif computer_id == "millhouse":
        #     self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
        #     #self.win_geometry   = '1300x600+20+20'
        #     self.db_file_name       =  "millhouse_db.db"

        # elif computer_id == "millhouse-mint":
        #     #self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
        #     #self.win_geometry   = '1300x600+20+20'

        #     pass

        # # ---- theprof
        # elif computer_id == "theprof":
        #     self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
        #     self.db_file_name       =  "the_prof_db.db"


        # # ---- "russ-thinkpad-p72":
        # elif computer_id == "russ-thinkpad-p72":
        #     self.win_geometry       = '1500x750+20+20'     # width x height position  x, y  good for the prof, mint

        #     self.logging_level      = logging.DEBUG



        # elif computer_id == "bulldog-mint-russ":
        #     self.ex_editor          =  r"xed"


        # else:
        #     print( f"In parameters: no special settings for computer_id {computer_id}" )
        #     if self.running_on.os_is_win:
        #         self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
        #     else:
        #         self.ex_editor          =  r"leafpad"    # Linux raspberry pi maybe

    # -------
    def os_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular operating systems
        you may need to mess with this based on your os setup
        """
        pass
        # if  self.os_win:
        #     self.icon               = r"./images/clipboard_b.ico"
        #         #  very dark greenhouse this has issues on rasPi
        #     self.icon               = r"./images/clipboard_b_red_GGV_icon.ico"
        #         #  looks same as clipboard_b_red_gimp.ico
        #     self.icon               = r"./images/clipboard_b_red_gimp.ico"    # pretty visible -- make black version -- cannot get gimp to do it


        # else:
        #     pass
        #     #self.gui_style          = "linux"

    #
    # -------
    def __init__( self, ):
        """
        Init for instance, usually not modified, except perhaps debug stuff
        ( if any )... but use plus_test_mode()
        may be down in listing because it should not be messed with.
        """
        #AppGlobal.parameters       = self   # register as a global
        self.mode_default()
        self.running_on_tweaks()
        self.choose_mode()

        #rint( self ) # for debugging

    # ------->> default mode, always call
    def mode_default( self ):
        """
        sets up pretty much all settings
        documents the meaning of the modes
        call first, then override as necessary
        good chance these settings will at least let the app run
        """
        self.mode              = "mode_default"
            # name your config, it will show in app title
            # may be changed later in parameter init

        # #--------------- automatic settings -----------------
        # self.running_on   = running_on.RunningOn
        # self.running_on.gather_data()

        # # some of the next all?? should be moved over to RunningOn
        # self.running_on.log_me( logger = None, logger_level = 10, print_flag = False )

        # # this is the path to the main.py program
        # self.py_path                   = self.running_on.py_path

        # self.set_default_path_here     = True
        #     # to make app location the default path in the app, Think True may always be best.
        #     # above may be tricky to reset, but we may have the original dir in running on
        # # no easy way to override this ??
        # if  self.set_default_path_here:     # Now change the directory to location of this file

        #     py_path    = self.running_on.py_path

        #     print( f"Parameters.py: Directory: (  >>{os.getcwd()}<< switch if not '' to >>{py_path}<<")
        #     if py_path != "":
        #         os.chdir( py_path )

        # # so we know our os  could be "linux" or our_os == "linux2"  "darwin"....
        # self.our_os             = self.running_on.our_os
        # self.os_win             = self.running_on.os_win          # boolean True if some version of windows
        # self.computername       = self.running_on.computername    # a name of the computer if we can get it
        # # directory where app was opened, not where it resides
        # self.opening_dir        = self.running_on.opening_dir     # the opening dir before anyone changes it

        # self.platform           = self.our_os           #  redundant

        # ---- appearance size--

        # control initial size and position with:
        self.qt_width           = 1200
        self.qt_height          = 200
        self.qt_xpos            = 10
        self.qt_ypos            = 10

        self.text_editor        = "gedit"
#        self.text_editor        = "xed"



        # qt_xpos     = 10
        # qt_ypos     = 10
        # qt_width    = 3000
        # qt_height   = 600

        # # opens on main monitor
        # qt_xpos     = 10
        # qt_ypos     = 10
        # qt_width    = 1400
        # qt_height   = 700

        self.minimun_useful    =  10


        self.icon               = r"./images/icon_red.png"    # icon for running app


        # self.id_color           = "blue"                # to id the app - not implemented yet



        # self.bg_color_frame     = "yellow"   # "black"  # "#F0F0F0"
            #    "#F0F0F0" seems to be a default light gray "gray" is darker

        # ---- logging
        self.pylogging_fn       = "./logs/app.py_log"   # file name for the python logging
        self.logging_level      = logging.DEBUG         # may be very verbose
        self.logging_level      = logging.INFO
        #self.logging_level      = logging.INFO

        self.logger_id          = "qtex"         # id of app in logging file

        self.gui_text_log_fn    = None   # for edit window if None then no logging
        self.gui_text_log_fn    = "./logs/gui_log.log"

        self.log_gui_text       = False # this is for gui_ext message area
                                             # goes to normal log file  not special one

        self.db_type            = "QSQLITE"
            # the type of database, so far we only support sqllite
        self.db_file_name        = "sample.db"   #  = "sample.db"   =  ":memory:"
        self.db_file_name        = ":memory"   #  = "sample.db"   =  ":memory:"
        # this is the name of a program: its executable with path info.
        # to be used in opening an external editor


        # # if we are writing scratch files to run in a shell or similar.
        # self.scratch_bat       =  r"scratch.bat"   # rel filename
        # self.scratch_py        =  r"scratch.py"    # rel filename

        # control button for editing the readme file
        self.readme_fn          = "readme_rsh.txt"   # or None to suppress in gui
            # a readme file accessable from the main menu


        # or anything else ( will try to shell out may or may not work )
        self.help_fn       =  "./docs/help.txt"   #  >>. this is the path to our main .py file self.py_path + "/" +
        self.help_path     =  "./docs"
            # path leading to all docs and help

        #self.help_file       =  "http://www.opencircuits.com/Python_Smart_ClipBoard"


    # ---------------------
    def to_columns( self, current_str, item_list, format_list = [ "{: <30}", "{:<30}" ], indent = "    "  ):
        """
        for __str__  probably always default format_list
        """
        #rint ( f"item_list {item_list}.............................................................. " )
        line_out  = ""
        for i_item, i_format in zip( item_list, format_list ):
            a_col  = i_format.format( i_item )
            line_out   = f"{indent}{line_out}{a_col}"
        ret_str  = f"{current_str}\n{line_out}"
        return ret_str

    # -----------------------------------
    def __str__( self,   ):
        """
        sometimes it is hard to see where values have come out this may help if printed.
        not complete, add as needed -- compare across applications and code above
        """
        # new_indented    = "\n    "   # but it nice to have some whitespace to see ...
        a_str = "this is the new str\n "
        a_str   = f"{a_str}>>>>>>>>>>* Parameters (some) *<<<<<<<<<<<<"



        return a_str






# =================== eof ==============================
