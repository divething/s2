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

tifs_path = ("/media/ubu/drive/sentinel/tif_test")



'''
 test_vrt= ["gdalbuildvrt", "-separate", 'NDVI_test'+ ".vrt"]
    image_list =  glob.glob('*/*band1.tif')
      for myfile in image_list:
        test_vrt.append(myfile)
        subprocess.call(test_vrt)
    img2tiff =["gdal_translate","test.vrt", "test_composite.tif"]
    subprocess.call(img2tiff)
'''



#####################
#   version 2
#####################

'''
the original looks like this:
from osgeo import gdal
outvrt = '/vsimem/stacked.vrt' #/vsimem is special in-memory virtual "directory"
outtif = '/tmp/stacked.tif'
tifs = ['a.tif', 'b.tif', 'c.tif', 'd.tif'] 
#or for all tifs in a dir
#import glob
#tifs = glob.glob('dir/*.tif')

outds = gdal.BuildVRT(outvrt, tifs, separate=True)
outds = gdal.Translate(outtif, outds)
'''
#   set up the output directories etc
outvrt = glob(os.path.join(tifs_path, "/vsimem/stacked_vrt.vrt"))#/vsimem is special in-memory virtual "directory"
outtif = glob(os.path.join(tifs_path, "/vsimem/stacked_tiff.vrt"))

#import glob
#tifs = glob.glob('dir/*.tif')
input_tifs = glob(os.path.join(tifs_path, "*.tif"))


#or for all tifs in a dir -   tifs = ['a.tif', 'b.tif', 'c.tif', 'd.tif'] 

#   outds = gdal.BuildVRT(outvrt, input_tifs, separate=True)
outds = gdal.BuildVRT("outvrt", "input_tifs", separate=True)
#   convert to tif
outds = gdal.Translate(outtif, outds,format='tiff')    