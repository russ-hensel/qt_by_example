Depricated, soon to be deleted, replaced by qt5_by_example 




# qt_by_example  
    which qt, for now QT5 for Python

This repo is obsolete, too much has changed on my machine.  I will create
qt5_by_example to replace this soon; as it is so much better and bigger.  For now
you can leave me messages in the issues section of the repo.
if you are interested in qt5_by_example, messge me here and I will
let you know how to get your hands on it.

The Plan ( some implemented ! )
The new plan for this is to have a have one applications for all the examples with a
key word search that activates a tab that shows the desired widgets in action.  The
code for each tab will largely be limited to that tab so if you copy code from it you
will not be entangled in a larger environment.  A break button on each tab will break
you into the code in the tab you are viewing.  In Spyder ( and I think other IDEs ) this
will also open an editor at the break point, making it really easy to find the code that
the tab illustrates. Once in the debug mode you can set additional breakpoints ( at least in
Spyder ) and continue debuggin even if you did not start the app in the debugger.
This plan will largely replace the old plan ( below ) although the
tab code will remain largely the same.

The old plan for this is to have a small number of applications that illustrate the
use of many of qt's widgets.  It grew out of my efforts to learn qt.  I use it
as a place to first test out code I think I understand, and then experiment a bit
with the code.  It may be useful to have two versions of the code, one close to this distribution
and one for expermentations. Would you like to contribute? Contact me.

Wat in a QT GUI:

This repo currently contains a version of wat ( see qt_wat.py and qt_wat_app.py ) 
that runs wat as a GUI application.  

    wat -- check it out:
    igrek51/wat: Deep inspection of Python objects
    https://github.com/igrek51/wat
    
Wat is used a lot by other Qt by example apps.
You may be interested in Wat even if you are not interested in the rest of this
repo.  It does run in qt, so you need to have qt installed.  You do not
need to run it in a qt app of your own, but you can if you wish.  I will
try to add some material in the wiki.

Install:

There is no install, just download and run in a Python of about 3.10 or higher, PyQt5 and the 
wat-inspector mentioned above.  If it does not run for you let me know and I will try to help out.

Back to the Examples:

The application's code should be simple and contain code that is closely linked to the
appearance of the widgets so that the code for each widget is easy to find.  One wat to find the code
is to use the <break> button found on all the tabs, this will break into the
debugger in the code of the tab page you are viewing.

The code is the examples should be "copy and paste ready" so you can copy it
into your application, tweak it anf be off and running.

Watch for updates and for postings here of any overall change in status.

Status: 
    A bit sad, but not so sad as it was.
    Some percentage of dead code, some waiting for integration
    Repo may be incomplete, but I think will work, let me know.
    I am doing a lot of development on it, it is a moving target
    that shoud be improving quite a bit untill I get into another 
    project.

To run:
    No install, just download and run from your development environment.
    Needs qt5 and wat
        wat may be found at:     igrek51/wat: Deep inspection of Python objects
                                 https://github.com/igrek51/wat

    Try running 
        * qt_widgets.py        -- qt widgets of vaious types
        * qt_sql_widgets.py    -- qt widgets mostly using sql 
        * qt_fitz_book.py      -- code based on book by M. Fitzpatric 
        for wat alone
        * qt_wat.pya_wat_function
        * qt_wat_app.py    
        
Lot more info coming to the Wiki soon, some even there now, mostly
screenshots.

And yes I should learn github markup.





    
