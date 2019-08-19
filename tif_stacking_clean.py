#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:46:05 2019

@author: ubu
"""
from glob import glob
""" 
=====================================
MS Comment #1
Make sure that you have the python3 glob package installed.
i.e. sudo apt install python3-glob
=========================================
""" 
import os    # All the operating system commands to break up paths and file names
import sys	
from osgeo import gdal

""" 
=====================================
MS Comment #2
The line below is not the way to work.
The path to the GTiff files should be **passed as an argument** on the command line
Always try to avoid hard coding paths, config parameters etc. into your scripts.  
=========================================
""" 
tifs_path = ("/media/ubu/drive/sentinel/tif_test")


#   set up the output directories etc
outvrt = glob(os.path.join(tifs_path, "/vsimem/stacked_vrt.vrt"))#/vsimem is special in-memory virtual "directory"
outtif = glob(os.path.join(tifs_path, "/vsimem/stacked_tiff.vrt"))

#import glob
#tifs = glob.glob('dir/*.tif')
"""
=====================================
MS Comment #3
glob returns a list
=========================================
""" 
input_tifs = glob(os.path.join(tifs_path, "*.tif"))


#or for all tifs in a dir -   tifs = ['a.tif', 'b.tif', 'c.tif', 'd.tif'] 

#   outds = gdal.BuildVRT(outvrt, input_tifs, separate=True)
""" 
=====================================
MS Comment #4
You have setup variable outvrt and input_tifs. To use a variable in the function
it must **not** be quoted. When you use quotes, you're passing a string, not the variable 
=========================================
""" 
outds = gdal.BuildVRT("outvrt", "input_tifs", separate=True)
#   convert to tif
outds = gdal.Translate(outtif, outds,format='tiff')    
