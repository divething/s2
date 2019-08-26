#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:06:56 2019

@author: ubu
"""

s2_name_safe = '/media/ubu/drive/sentinel/extracted_images/S2B_MSIL2A_20190426T081609_N0211_R121_T36RXV_20190426T115053.SAFE'



from osgeo import gdal
dataset = gdal.Open(s2_name_safe, gdal.GA_ReadOnly)
subdatasets = dataset.GetSubDatasets()
dataset = None


import sys
from osgeo import gdal
ds = gdal.Open(sys.argv[1])
open(sys.argv[2], 'wb').write(ds.GetMetadata('xml:VRT')[0].encode('utf-8'))
 \
SENTINEL2_L1C:S2A_OPER_MTD_SAFL1C_PDMC_20150818T101440_R022_V20150813T102406_20150813T102406.xml:10m:EPSG_32632 10m.vrt
         
                 gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2
    
    



gdalbuildvrt -separate stack.vrt lsat1.tif lsat2.tif ...

#	Should give you a gdal dataset that is 'stacked and is covers the extent of all images. If you need a tif after that, use

gdal_translate stack.vrt stack.tif
    
    
    
    


import s2reader
