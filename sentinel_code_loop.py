# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




#this code intends to run a batch processing list of algorithms of all the files sentinel files in the folder 
#################################################################
###     step 1.0     choosing the folder                  #####
#################################################################

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




root = tkinter.Tk()
root.withdraw()
s2_path = filedialog.askdirectory(parent=root,initialdir="/home/tamir/Documents/",title='Please select a directory')
print(s2_path)


#################################################################
###     step 1.1     making a list of images                  #####
#################################################################


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
#               s2_path = ("/media/ubu/drive/github/sentinel/input_images")
#	/media/ubu/drive/sentinel/input_images
#   s2_path = ("/media/ubu/drive/sentinel/input_images")
s2_list_zip = glob(os.path.join(s2_path, "*.zip"))

print("This is the name of the script: ", sys.argv[0])
print( "Number of arguments: ", len(sys.argv))
print( "The arguments are: " , str(sys.argv))




###########################################################
### unzipping
##############################################
temp_path = (os.path.join(s2_path, "temp") )
# importing required modules 
from zipfile import ZipFile 




for zipping in s2_list_zip:
    # specifying the zip file name 
    # file_to_zip = s2_list_zip(zipping)
  
    # opening the zip file in READ mode 
    #   with ZipFile("/media/ubu/drive/github/sentinel/input_images/S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753.zip", 'r') as zip: 

    with ZipFile(zipping, 'r') as zip: 
    # printing all the contents of the zip file 
        zip.printdir() 
  
    # extracting all the files 
        print('Extracting all the files now...') 
    
        zip.extractall(temp_path) 
        print('Done!') 


###############################################################################
###############################################################################
###############################################################################
#   processing loop should start here

# this is the database/table/matrix - it should have each of the folloing steps fill in tha columns.  
#   the rows should be one row per image




#####################################################################
###     step 1.2     breaking image name to make an image name, date, type, etc    #####
#####################################################################



s2_list_safe = glob(os.path.join(temp_path, "*.SAFE"))
# Are we working with the raw "*.SAFE" compressed format?
# or extracted *.tif ??

#	make and input the list of files in folder in list 
number_of_images = len (s2_list_safe)
col_label = ["index","processed","complet",'path', 'file', 'format','mission' , 'type_&_level', 'time_capture', 'tile_n', 'tile_r', 'tile_utm', 'time_prcessing','image_type','processing_level','yyyy', 'mm','dd','hh','min','time']
image_table = pandas.DataFrame(columns=col_label, index=range(number_of_images))
test = pandas.DataFrame(columns=col_label, index=range(number_of_images))
test1 = []
for i in range(number_of_images):
    '''
    s2_path = (os.path.splitext(os.path.split(s2_file_safe)[0])[0])
    s2_name = (os.path.splitext(os.path.split(s2_file_safe)[1])[0])
    s2_name_format = (os.path.splitext(os.path.split(s2_file_safe)[1])[1])
    s2_name_full = (os.path.splitext(os.path.split(s2_file_safe)[1])[1])
'''    
    print (s2_list_safe)
    print (i)
    
    s2_file_components=[]
    s2_file_components.append(i)
    s2_file_components.append(i+1)
    s2_file_components.append(s2_list_safe[i])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[0])[0])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[1])[0])
#    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[0])[1])
    s2_file_components.append(os.path.splitext(os.path.split(s2_file_components[2])[1])[1])

    """
    ***********************************
    TODO for Tamir:
        Why do I need the subset index [1] and [0] above ?
        
        in the first part    os.path.split()[1] it takes everthing after the last /
        in the second part   os.path.splitext() [0]     it wants everything up to the suffix 
        so now we have only the file name
        
    ***********************************
    """
    

#	break file names into details: date, sensor, product etc etc
    #   s2_file_components = "_".split(s2_name)
    # Now we have:
    # s2_file_components[0] is the mission
    namesplit = (s2_file_components[4].split("_"))
    s2_file_components = ((s2_file_components + namesplit))
#################################################################
    #   extracting details from the file name - im expecting each to be a column in the database
#   option 1
#   another way to split a string of regular order
#   S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753
    '''
        #   an unsessery step but nice to know i can do that
        mission = s2_name[0:3]
        type = s2_name[4:7]
        level = s2_name[7:9]
        yyyy = s2_name[11:15]
        mm = s2_name[15:17]
        dd = s2_name[17:19]
        hh = s2_name[20:22]
        min = s2_name[22:23]
        # s2_file_components[1] is the level
            # s2_file_components[2] is the acquisition date string
            # s2_file_components[3] is the processing number
            # s2_file_components[4] is the orbit number
            # s2_file_components[5] is the tile number
    '''


#   making a table of all these detils 
    #database.append([s2_name[0:3]])
    
#    s2_file_components.append(s2_file_components[1])
#    s2_file_components.append((s2_file_components))
    s2_file_components.append((s2_file_components[4])[4:7])
    s2_file_components.append((s2_file_components[4])[7:10])
    #s2_file_components.append(s2_name[9:11])
    s2_file_components.append((s2_file_components[4])[11:15])
    s2_file_components.append((s2_file_components[4])[15:17])
    s2_file_components.append((s2_file_components[4])[17:19])
    s2_file_components.append((s2_file_components[4])[20:22])
    s2_file_components.append((s2_file_components[4])[22:23])


#############################################################
#   extracting the date components from the date and time string
#############################################################
    """
    ***********************************
    TODO for Tamir:
        Convert the date string to an actual python date object
        Hint: see the strptime function in datetime module
        https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strptime
    
    
    for exampla
    20190506T081609 is the string. 
    formatting components are:
    %Y
    %m
    %d
    T
    %H
    %M
    %S
    
    to test it:
        
    IN[21]: datetime.datetime.strptime("20190506T081609", "%Y%m%dT%H%M%S")
    Out[21]: datetime.datetime(2019, 5, 6, 8, 16, 9)
    
      
    ***********************************
    """
    import time
    import datetime
    inputime = (s2_file_components[4])[11:25]
    datetime.datetime.strptime(inputime, "%Y%m%dT%H%M%S")
    
    s2_file_components.append(datetime.datetime.strptime(inputime, "%Y%m%dT%H%M%S"))


########################################################################
###     sorting out all the data in one table.
########################################################################
    '''
    
    this is my attempt in filling in the table withthe data - its crap
    
    
    os.path.split(s2_file_safe)[n]
    
    (s2_file_safe)[x]
    givs the file with its path
    '/home/tamir/Documents/sentinel_images_for_burn/originals/temp/S2A_MSIL2A_20180416T081601_N0207_R121_T36RXV_20180416T103632.SAFE'
    
    os.path.split((s2_file_safe)[0])
    ('/home/tamir/Documents/sentinel_images_for_burn/originals/temp',
     'S2A_MSIL2A_20180416T081601_N0207_R121_T36RXV_20180416T103632.SAFE')
    splits the above into the path and the file
    
    
    '''    
#    img_database.append (os.path.split((s2_file_safe)[0]))
#    fObj = pandas.DataFrame(img_database)
#    dfObj = pandas.DataFrame(img_database, columns = ['img_path' , 'img_name'])
#    
#
#    import pandas
##   fObj = pandas.DataFrame(img_database)
    
    image_table.loc[i,:] = s2_file_components.copy()

    test.loc[i,:] = s2_file_components

#    image_table = pandas.DataFrame([s2_file_components], columns =  col_label)
#    test = pandas.DataFrame([s2_file_components], index = [i], columns =  col_label)
#    test1.append(s2_file_components, ignore_index=True)
#    test.loc[count].s2_file_components
#    del s2_file_components
#
    img_4rom_list = gdal.Open(s2_file_components[2], gdal.GA_ReadOnly)
    img_4rom_list.GetRasterBand(1)



/media/ubu/drive/sentinel/input_images/temp/S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753.SAFE/GRANULE/L2A_T36RXV_A011301_20190506T082328/IMG_DATA/R10m/T36RXV_20190506T081609_B02_10m.jp2
/media/ubu/drive/sentinel/input_images/temp/S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753.SAFE
b2_path

########################################################
###     step 3  opening a file                     #####
########################################################
import sys
from osgeo import gdal
#   cd s2_save_path
for l in range(number_of_images):#  here we start the second loop that creates processs the images
    img = gdal.Open(image_table.loc[l,3], gdal.GA_ReadOnly)









'''

examples that didn't work for me for various reasons
=======================================================
here are some code in gdasl that work:
step 1 export an image directly from a zip (how it comes out from sentinel hub) to layers in tif format in 3 batches - 10m resolution and than 20 and 60
    gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2

   alternatively can be made into vrt so not to take space in the hd
  
 gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.vrt -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2   
    
 so now we have band in three files at different resolutions  
    
    



python -c "import sys; from osgeo import gdal; ds = gdal.Open(sys.argv[1]); open(sys.argv[2], 'wb').write(ds.GetMetadata('xml:VRT')[0].encode('utf-8'))" \
         SENTINEL2_L1C:S2A_OPER_MTD_SAFL1C_PDMC_20150818T101440_R022_V20150813T102406_20150813T102406.xml:10m:EPSG_32632 10m.vrt 
   
======================================================

rasterio

band2 = rasterio.open(s2_path+'T11SKB_20180825T183909_B02.jp2', driver='JP2OpenJPEG')



#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
%matplotlib inline

#import bands as separate 1 band raster
imagePath = '../Sentinel2/GRANULE/L1C_T11SKB_A007675_20180825T184430/IMG_DATA/'
band2 = rasterio.open(imagePath+'T11SKB_20180825T183909_B02.jp2', driver='JP2OpenJPEG') 




'''




'''



from osgeo import gdal

#   dataset = gdal.Open("path/to/dataset.tiff", gdal.GA_ReadOnly)

img = gdal.Open(s2_name_safe, gdal.GA_ReadOnly)

gdal.GDALTranslateOptions.









fig = plt.figure(figsize=(10, 10))
fig.set_facecolor('white')
plt.imshow(ndvi, cmap='RdYlGn') # Typically the color map for NDVI maps are the Red to Yellow to Green
plt.title('NDVI')
plt.show()




'''















##########	loop through list	###############

#	open file 

#	optional: convert epsg to utm or israel 2039

#	stck all layers (resample spatially) https://gis.stackexchange.com/questions/80620/using-gdal-python-to-stack-georeferenced-images-of-different-sizes

#	clip layer cy shp file
# POLYGON ((34.00929260253906 31.324234008789062, 34.01079559326172 31.324234008789062, 34.01079559326172 31.347789764404297, 34.00929260253906 31.347789764404297, 34.00929260253906 31.324234008789062, 34.00929260253906 31.324234008789062))

#	designate names to layers







##########	calculate indices:  NDVI etc	#################

#	NDVI = (NIR — VIS)/(NIR + VIS)
