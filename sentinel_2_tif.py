'''
gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2

gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:20m:EPSG_32636 20m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2

gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:60m:EPSG_32636 60m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2
'''     
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

# =============================================================================
#    get the foleder with the images
# =============================================================================


root = tkinter.Tk()
root.withdraw()
s2_path = filedialog.askdirectory(parent=root,initialdir="/home/tamir/Documents/sentinel_images_for_burn/snap_input_images",title='Please select a directory')
print(s2_path)
os.chdir (s2_path)
# =============================================================================
#    make a list of images
# =============================================================================
s2_list_zip = glob(os.path.join(s2_path, "*.zip"))

# =============================================================================
#    parameters for making the band list
# =============================================================================

# 10m band names    
band_list = []
band_list.append("B02_10m")
band_list.append("B03_10m")
band_list.append("B04_10m")
band_list.append("B08_10m")
band_list.append("AOT_10m")
band_list.append("WVP_10m")
# 20m band names    
band_list.append("B05_20m")
band_list.append("B06_20m")
band_list.append("B07_20m")
band_list.append("08A_20m")
band_list.append("B011_20m")
band_list.append("B012_20m")
band_list.append("TCI_20m")
band_list.append("SCL_20m")
# 60m band names    
band_list.append("B01_60m")
band_list.append("B09_60m")
#   additional products


number_of_bands = len (band_list)


# =============================================================================
# =============================================================================
# =============================================================================
#   open image in gdal loop
# =============================================================================
# =============================================================================
# =============================================================================

number_of_images = len (s2_list_zip)
xml_component = 'MTD_MSIL2A.xml'
    
    

for i in range(number_of_images):    
# =============================================================================
#    getting the file name components 
# =============================================================================    
    s2_file_components=[]
    s2_file_components.append(i)
    s2_file_components.append(i+1)
    s2_file_components.append(s2_list_zip[i])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[0])[0])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[1])[0])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[1])[1])
    s2_file_components.append((s2_file_components[4])[4:7])
    s2_file_components.append((s2_file_components[4])[4:7])
    s2_file_components.append((s2_file_components[4])[7:10])
    s2_file_components.append((s2_file_components[4])[11:15])
    s2_file_components.append((s2_file_components[4])[15:17])
    s2_file_components.append((s2_file_components[4])[17:19])
    s2_file_components.append((s2_file_components[4])[20:22])
    s2_file_components.append((s2_file_components[4])[22:23])
    namesplit = (s2_file_components[4].split("_"))
    s2_file_components = ((s2_file_components + namesplit))
    
# =============================================================================
#    making the list of jp2 files 
# =============================================================================
    

    s = "_";
    ss = "";
    band_2_open = []
    band_jp2 = []
    for k in range(number_of_bands):
        seq = ((s2_file_components[8]),(s2_file_components[19]),(s2_file_components[16]),(band_list[k]))
        band_2_open.append(s.join( seq ))
        seq = ((band_2_open[k]),".jp2")
        band_jp2.append(ss.join(seq))

# =============================================================================
#     building the names of the files to be open in the temp folder
# =============================================================================
   
    
    input_file_name = os.path.join((s2_file_components[3]),"temp",(s2_file_components[4]),".SAFE","GRANULE",(s2_file_components[21]),"IMG_DATA","R10m",band)
    
    
    
    
    
    
'''
this worked!!!!!!  
    
  tamir@deb:~/Documents/sentinel_images_for_burn/snap_input_images/temp$ gdal_translate SENTINEL2_L2A:S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2
  
  tamir@deb:~/Documents/sentinel_images_for_burn/snap_input_images$ gdalinfo S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.zip

  
  
'''
    
    
    
'''
    
  ds = gdal.Open(sys.argv[1]); open(sys.argv[2], 'wb').write(ds.GetMetadata('xml:VRT')[0].encode('utf-8')) SENTINEL2_L2A:/home/tamir/Documents/sentinel_images_for_burn/snap_input_images/S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.zip/S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.SAFE/MTD_MSIL2A.xml:10m:EPSG_32632 10m.vrt  
    
    
s2_file_components.append(os.path.join((s2_file_components[2]),(s2_file_components[4]),".SAFE",xml_component))
input_file_name = os.path.join((s2_file_components[2]),(s2_file_components[4]),".SAFE",xml_component)



    gdal.Open(sys.argv[1]); open(sys.argv[2], 'wb').write(ds.GetMetadata('xml:VRT')[0].encode('utf-8')) SENTINEL2_L1C:(s2_file_components[6]):10m:EPSG_32632 10m.vrt

    ds = gdal_translate SENTINEL2_L2A:/home/tamir/Documents/sentinel_images_for_burn/snap_input_images/S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.zip/S2B_MSIL2A_20180131T082149_N0206_R121_T36RXV_20180131T120612.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2
    
    

input_B01_name = os.path.join((s2_file_components[2]),(s2_file_components[4]),".SAFE","GRANULE",)


'''     
