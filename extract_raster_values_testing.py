#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:41:37 2019

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
#    grass spacial action
# =============================================================================

try:
    import grass.script as gscript
except ImportError:
    print("""You must be in a running GRASS GIS session.
          Exiting...""")
    sys.exit(1)




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
#   get the shp file
# =============================================================================
root = tkinter.Tk()
root.withdraw()
input_vect = filedialog.askdirectory(parent=root,initialdir="/home/tamir/Documents/sentinel_images_for_burn/processed/indices_products",title='Please select your tiff containing directory')
#vect_name = os.path.splitext(os.path.split(input_vect)[1])[0]
print(input_vect)
print(vect_name)
# =============================================================================
#   import the shp file
# =============================================================================
gscript.run_command('v.import',input_=input_vect,output=vect_name, overwrite=True)


    for i in range(len(tiff_list)):
         # Starting
        t0 = DT.now()
        print("\n   %s - Beginning process" % t0)
        print (i)
        # Import one tiff
        t = tiff_list[i]



# =============================================================================
#   now extract file name procedure
# =============================================================================
    
     
    
        tiff_filename_components=[]
        tiff_filename_components.append(i)
        tiff_filename_components.append(i+1)
        tiff_filename_components.append(tiff_list[i])
        tiff_filename_components.append(os.path.splitext(os.path.split(tiff_filename_components[2])[0])[0])
        tiff_filename_components.append(os.path.splitext(os.path.split(tiff_filename_components[2])[1])[0])
        tiff_filename_components.append(os.path.splitext(os.path.split(tiff_filename_components[2])[1])[1])
        tiff_filename_components.append(os.path.basename((tiff_filename_components[3])))

        tiff_filename_components.append((tiff_filename_components[4])[4:7])
        tiff_filename_components.append((tiff_filename_components[4])[4:7])
        tiff_filename_components.append((tiff_filename_components[4])[7:10])
        tiff_filename_components.append((tiff_filename_components[4])[11:15])
        tiff_filename_components.append((tiff_filename_components[4])[15:17])
        tiff_filename_components.append((tiff_filename_components[4])[17:19])
        tiff_filename_components.append((tiff_filename_components[4])[20:22])
        tiff_filename_components.append((tiff_filename_components[4])[22:23])
    
        namesplit = (tiff_filename_components[4].split("_"))
        tiff_filename_components = ((tiff_filename_components + namesplit))
        
# =============================================================================
#   make the column name
# =============================================================================
 
        col_name = tiff_filename_components[6] +"_"+tiff_filename_components[10]+tiff_filename_components[11]+tiff_filename_components[12]+ "_"+str(i).zfill(3)
        
        
# =============================================================================
#   here is the important stuff
# =============================================================================
       
        

        gscript.run_command('v.what.rast',
                            map_=vect_name, raster=rast_name, column=col_name)
        # Remove the raster
        gscript.run_command('g.remove',
                            type_="rast", name=rast_name, flags="f")
# =============================================================================
#   export the output file
# =============================================================================
    # Loop complete, now export vector attrib table to CSV
    vect_name = tiff_filename_components[6] +"_output"
    gscript.run_command('v.out.ogr',
                        input_=vect_name, output=output_csv, format="CSV")

    # Starting
    t1 = DT.now()
    ttl_secs = (t1 - t0).seconds
    print("\n   %s - Process complet after %d seconds" % (t0, ttl_secs))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        