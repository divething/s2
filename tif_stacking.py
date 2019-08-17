#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:46:05 2019

@author: ubu
"""
from glob import glob
import os    # All the operating system commands to break up paths and file names
import sys	
from osgeo import gdal
import tkinter
from tkinter import filedialog


#   get a folder with images and move into it

root = tkinter.Tk()
root.withdraw()
tifs_path = filedialog.askdirectory(parent=root,initialdir="/media/ubu/drive/sentinel/",title='where is them tiffs')
print(tifs_path)
os.chdir(tifs_path)




#   get the list f images to open - all the tifs in the folder
#   tifs = glob.glob('dir/*.tif')

input_tifs = glob(os.path.join(tifs_path, "*.tif"))


#or for all tifs in a dir -   tifs = ['a.tif', 'b.tif', 'c.tif', 'd.tif'] 


#   use gdal to make a temp file
#   outds = gdal.BuildVRT(outvrt, input_tifs, separate=True)
'''
outds = gdal.BuildVRT('wtf', input_tifs, separate=True)
#   convert to tif
outds = gdal.Translate('outtif', outds,format='GTiff')    
'''

outds = gdal.BuildVRT('wtf', input_tifs, separate=True)
#   convert to tif
gdal.Translate('outtif', outds,format='GTiff')    

