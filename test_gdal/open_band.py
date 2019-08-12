#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:29:36 2019

@author: ubu
"""

from osgeo import gdal
import sys
# this allows GDAL to throw Python Exceptions
gdal.UseExceptions()

file = "/media/ubu/drive/sentinel/output_images/Subset_S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753_resampled_tif.tif"



#try:
src_ds = gdal.Open( file )
#except RuntimeError, e:
#    print 'Unable to open INPUT.tif'
#    print e
#    sys.exit(1)

#try:
srcband = src_ds.GetRasterBand(1)
#except RuntimeError, e:
#    # for example, try GetRasterBand(10)
#    print 'Band ( %i ) not found' % band_num
#    print e
#    sys.exit(1)