#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this shows wat_inspector being call from a script that is not inside
a qt application.

Note the setup code that allows it to work.

"""

import time
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QMenu, QAction, QSizePolicy

#import qt_wat_app.py
import wat_inspector




def a_function():
    """ """
    print( "start" )
    time.sleep( .1 )
    #app.exec()
    something_local   = 1
    a_local_list      = [1,2,3,4]
    wat_inspector.go(
         msg            = "inspect from a_function",
         a_locals       = locals(),
         a_globals      = globals(), )
    print( "started")
    #app.exec()
    return

# --------------------
if __name__ == "__main__":



   # global app

    TEXT_EDITOR     = "xed"
    app             = QApplication( sys.argv )
    dialog          = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog
    a_function()
    print( "edn function 1")
    #a_function()
    # window          = QtWidgetExamples()
    # window.show()
    #sys.exit(
    #app.exec()

    #sys.exit( 0 )