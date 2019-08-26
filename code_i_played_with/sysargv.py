# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this code intends to run a batch processing list of algorithms of all the files sentinel files in the folder 

#	open folder
# Easiest done using the python library 'glob'
# https://docs.python.org/3/library/glob.html
from glob import glob
import os    # All the operating system commands to break up paths and file names
import sys	
## why frm globe import globe  while import os stands alone?

"""
glob needs the full path to the image files
I suggest to get the path as a command line arguement
So this script will be called as "sentinel_code.py <path/to/images>
If no path is given, then the default will be the current working dir

***********************************
TODO for Tamir
    Prepare a test to check for the command line argument
    check out: sys.argv
    https://docs.python.org/3/library/sys.html?highlight=argv#module-sys
    If it exists, set the variable 's2_path' to that path for glob
    If it doesn't exist set s2_path = "./"
    hint: len(sys.argv) > 0
***********************************
"""
#   /media/ubu/drive/github/sentinel/input_images
s2_path = ("/media/ubu/drive/github/sentinel/input_images")
#	/media/ubu/drive/sentinel/input_images
#   s2_path = ("/media/ubu/drive/sentinel/input_images")
s2_list = glob(os.path.join(s2_path, "*.zip"))

print("This is the name of the script: ", sys.argv[0])
print( "Number of arguments: ", len(sys.argv))
print( "The arguments are: " , str(sys.argv))

sys.argv[1]
str((sys.argv)[2])
