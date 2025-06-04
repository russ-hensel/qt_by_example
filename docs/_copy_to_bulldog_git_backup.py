# -*- coding: utf-8 -*-



"""

r"D:\Russ\0000\python00\python3\_projects\cmd_assist"


r"D:\for_gitlab\cmd_assist"

J:\git_backup_and_run
J:\git_backup_and_run\for_gitlab

D:\for_gitlab


should exclued .git directory


"""


import  sys

# I normally do not install the backup app, so I need to point to code, you will need to adjust for your system
sys.path.append( "D:/Russ/0000/python00/python3/_projects/backup" )
sys.path.append( "D:/Russ/0000/python00/python3/_projects/rshlib" )

import directory_backup
import file_filters


"""
this file is not the application, it is tucked away here as app  = directory_backup.App(  )
"""
app         = directory_backup.App(  )
app_state   = app.app_state



# this is a shortcut way to setup both the source and destination
# app.parameters.copy_from_source_here_to( "data"  )   # see parameters.py
# if not using the above then: you need these 4:


app_state.source_dir               = r"D:\for_github"  # needed
app_state.source_media_id          = "ignore"      # safety check, if set to ignore, media_id is not checked, defaults to ignore so you can skip

app_state.dest_dir                 = r"J:\git_backup_and_run\for_github"
app_state.dest_media_id            = "ignore"      #  as above but for destination



#lots more things you can set see app_state code comments for more info on meaning

app_state.backup_name              = "from gitlab to git backup and run "   #  will have a default name


#app_state.log_detail_fn            = self.parameters.log_detail_fn     # default from parameter file, else you can set
#app_state.log_summary_fn           = self.parameters.log_summary_fn    # default from parameter file, else you can set



# ------------------>>>>>> file filter
filter_object                     = file_filters.FFAll() # but is also default
app_state.file_filter_object      = filter_object
# --- or name starts with
#filter_object                     = file_filters.FFNameStartsWith(  )
#filter_object.list_of_starts_with =  "_"
#filter_object.include_true        = False
#app_state.file_filter_object      = filter_object
# ------------------ <<<<< end of file filter


# ------------------ >>>>>> dir filter
# app_state.dir_filter_object       = file_filters.DFAll()   # default to DFAll() else you can

filter_object                     = file_filters.DFNameStartsWith(  )
filter_object.list_of_starts_with = [   ".g", ".vs"  ]   # for .git and .vscode watch out for othes
filter_object.include_true        = False       # will exclude
app_state.dir_filter_object       = filter_object   #
# ------------------ <<<<< end of DIR filter

# --------------------

app_state.do_src_dest_match       = True   # default to True, you can change -- check source dest tails match

app_state.max_dir_depth           = -1     # default to -1   -1 is not limit to depth else what it says

#app_state.minus_dir                = 0    # default to 0 not sure what it means

#app_state.simulate_mode_flag    = self.parameters.simulate_mode_flag   # default in parameters -- True, no actually copy simulate

#app_state.log_skipped_flag      = self.parameters.log_skipped_flag     # default in parameters -- True, log when skipping a file

# run it

app.run_gui()

"""
clean up
"""
app.clean_up()   # cant this be moved inside run_gui ?? probably


#======================= Notes: ========================

"""
You might want to keep some notes here


"""