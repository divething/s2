#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:28:56 2019

@author: ubu

This is a temporary script file.
"""
#ch
#this code intends to run a batch processing list of algorithms of all the files sentinel files in the folder 

#   toolboxes
import pandas
from osgeo import gdal
import sys






####################################################
#   support files opening###########################
####################################################

#   import pandas

#   sentinel band data - info on spectrak and spatial per band etc
#   inport from csv - 2 options comma delimited , tab delimited and from excel


#   tab
bands_filename = ("/home/ubu/Dropbox/db_code_bank/spectral_response/s2_bands.csv")
bands = pandas.read_csv(bands_filename,sep='\t')
bands.head() # prints out first rows of your data

#    coma
bands_filename_comma = ("/home/ubu/Dropbox/db_code_bank/spectral_response/s2_bands_comma.csv")
bands_comma = pandas.read_csv(bands_filename_comma)
bands.head() # prints out first rows of your data

#   exel read (fucks up the formats)
dataframe = pandas.read_excel("/home/ubu/Dropbox/db_code_bank/spectral_response/bands.xls")




#	open additional files: shp file for clipping




#	open folder



#	make a empty list 


#	make and input the list of files in folder in list 


#	break file names into details: date, sensor, product etc etc





#    for testing here is a file
image_file = "/media/ubu/drive/sentinel/output_images/Subset_S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753_resampled_tif.tif"





##########	loop through list	###############

#	open file 

from osgeo import gdal

#   dataset = gdal.Open("path/to/dataset.tiff", gdal.GA_ReadOnly)

dataset = gdal.Open("/media/ubu/drive/sentinel/output_images/Subset_S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753_resampled_tif.tif", gdal.GA_ReadOnly)

#   define the product - s2a or s2b - 2a or 2b - from the filename

product_type = ("s2b")




#   from osgeo import gdal
#   import sys
# this allows GDAL to throw Python Exceptions
gdal.UseExceptions()

file = "/media/ubu/drive/sentinel/output_images/Subset_S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753_resampled_tif.tif"



#try:
#try:
src_ds = gdal.Open( file )
#except RuntimeError, e:
#    print 'Unable to open INPUT.tif'
#    print e
#    sys.exit(1)

srcband = src_ds.GetRasterBand(1)
#except RuntimeError, e:
#    # for example, try GetRasterBand(10)
#    print 'Band ( %i ) not found' % band_num
#    print e
#    sys.exit(1)














#   open the file
for x in range(1, dataset.RasterCount + 1):
    band = dataset.GetRasterBand(x)
    image_matrix = band.ReadAsArray()















import gdal


# open dataset
ds = gdal.Open('test.tif')












#	optional: convert epsg to utm or israel 2039

#	stck all layers (resample spatially) https://gis.stackexchange.com/questions/80620/using-gdal-python-to-stack-georeferenced-images-of-different-sizes

#	clip layer cy shp file
POLYGON ((34.00929260253906 31.324234008789062, 34.01079559326172 31.324234008789062, 34.01079559326172 31.347789764404297, 34.00929260253906 31.347789764404297, 34.00929260253906 31.324234008789062, 34.00929260253906 31.324234008789062))

#	designate names to layers







##########	calculate indices:  NDVI etc	#################

#	NDVI = (NIR — VIS)/(NIR + VIS)