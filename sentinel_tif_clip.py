#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:05:03 2019

@author: tamir
"""

# =============================================================================
#   start from new
#     
# =============================================================================
    

import tkinter
from tkinter import filedialog
from glob import glob
import os    # All the operating system commands to break up paths and file names
import sys	
import time
import datetime
from zipfile import ZipFile 
import pandas
from osgeo import gdal
import rasterio
from datetime import datetime as DT


# =============================================================================
#    get the foleder with the images
# =============================================================================
root = tkinter.Tk()
root.withdraw()
tiff_dir = filedialog.askdirectory(parent=root,initialdir="/home/tamir/Documents/sentinel_images_for_burn/processed/indices_products",title='Please select your tiff containing directory')
print(tiff_dir)
os.chdir (tiff_dir)
# =============================================================================
#   import list of tif files
# =============================================================================
tiff_list = glob(os.path.join(tiff_dir, "*.tif"))

# =============================================================================
#   the min max points in utm 32636 s_ is the minimum image that contains the data
# =============================================================================
xmin = '615000'
ymin = '3500000'
xmax = '660000'
ymax = '3450000'

s_xmin = '635000' 
s_ymin = '3500000'
s_xmax = '655000'
s_ymax = '3455000'

# =============================================================================
#   start the loop
# =============================================================================

for i in range(len(tiff_list)):
     # Starting
    t0 = DT.now()
    print("\n   %s - Beginning process" % t0)
    print (i)
    # Import one tiff
    t = tiff_list[i]

# =============================================================================
#   gdal component
# =============================================================================

    ds1 = gdal.Open(t)
    ds2 = gdal.Translate('new.tif', ds, projWin = [xmax, ymax, xmin, ymin])
    dt = gdal.Warp(tiff_list[i], ds1, format=Gtiff, outputBounds=[xmax, ymax, xmin, ymin])
    ds = None

'''

    # Create raster
    OutTileName = str(Count)+'.SomeTileName.tif'
    OutTile = gdal.Warp(OutTileName, Raster, format=RasterFormat, outputBounds=[minX, minY, maxX, maxY], xRes=PixelRes, yRes=PixelRes, dstSRS=Projection, resampleAlg=gdal.GRA_NearestNeighbour, options=['COMPRESS=DEFLATE'])
    OutTile = None # Close dataset

# Close datasets
Raster = None
VectorDataset.Destroy()
print("Done.")



'''



