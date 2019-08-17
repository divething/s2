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

>>>>>>>>>
    ubu@ubu:~$ sudo apt install python3-glob
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    E: Unable to locate package python3-glob
    ubu@ubu:~$ 

import glob works in python (in spyder)....

=========================================
""" 



import os    # All the operating system commands to break up paths and file names
import sys	
from osgeo import gdal
import tkinter
from tkinter import filedialog


""" 
=====================================
MS Comment #2
The line below is not the way to work.
The path to the GTiff files should be **passed as an argument** on the command line
Always try to avoid hard coding paths, config parameters etc. into your scripts.  

>>>>>>>>>>
was a temperery measure - i was gonna do the following (which works)

=========================================
""" 
#       tifs_path = ("/media/ubu/drive/sentinel/tif_test")



root = tkinter.Tk()
root.withdraw()
tifs_path = filedialog.askdirectory(parent=root,initialdir="/media/ubu/drive/sentinel/",title='where is them tiffs')
print(tifs_path)
os.chdir(tifs_path)







#   set up the output directories etc
#outvrt = glob(os.path.join(tifs_path, "/vsimem/stacked_vrt.vrt"))#/vsimem is special in-memory virtual "directory"
#outtif = glob(os.path.join(tifs_path, "/vsimem/stacked_tiff.vrt"))

#import glob
#tifs = glob.glob('dir/*.tif')
"""
=====================================
MS Comment #3
glob returns a list
>>>>>>>>
thats whet i wanted isnt it? the input for the next command gdal.BuildVRT - is a list of files....

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

>>>>>>>>>>>>>>>>>>>>>>>>>>>
ok so heres the problem when i do without '  i get an error although i have defined outvrt earlier and its an empty list (maybe thats the problem?)
so 
input_tifs is a list with 5 images as str:
    ['/media/ubu/drive/sentinel/tif_test/MOD09GA.A2017251.state_1km_1.tif', '/media/ubu/drive/sentinel/tif_test/MOD09GA.A2017248.state_1km_1.tif', '/media/ubu/drive/sentinel/tif_test/MOD09GA.A2017249.state_1km_1.tif', '/media/ubu/drive/sentinel/tif_test/MOD09GA.A2017250.state_1km_1.tif', '/media/ubu/drive/sentinel/tif_test/MOD09GA.A2017247.state_1km_1.tif']

outvrt and also outtif ate both empty lists that show [] as their values

but when i run it as u=you suggeted i get 

outds = gdal.BuildVRT(outvrt, input_tifs, separate=True)

Traceback (most recent call last):

  File "<ipython-input-30-9c9d0bb0b396>", line 1, in <module>
    outds = gdal.BuildVRT(outvrt, input_tifs, separate=True)

  File "/usr/lib/python3/dist-packages/osgeo/gdal.py", line 1269, in BuildVRT
    return BuildVRTInternalNames(destName, srcDSNamesTab, opts, callback, callback_data)

  File "/usr/lib/python3/dist-packages/osgeo/gdal.py", line 3510, in BuildVRTInternalNames
    return _gdal.BuildVRTInternalNames(*args)

RuntimeError: not a string

so

i than tried the following alternative:

outds = gdal.BuildVRT('wtf', input_tifs, separate=True)

and it worked... (i think - there was no error)






=========================================
""" 
outds = gdal.BuildVRT('wtf', input_tifs, separate=True)
#   convert to tif
outds = gdal.Translate('outtif', outds,format='GTiff')    


'''
so im happy to say that at this stage - everything worked and i have a product.

very little help from you - i have a usfule pieace of code.... who would have thought
i think i need to kill



#   set up the output directories etc
outvrt = glob(os.path.join(tifs_path, "/vsimem/stacked_vrt.vrt"))#/vsimem is special in-memory virtual "directory"
outtif = glob(os.path.join(tifs_path, "/vsimem/stacked_tiff.vrt"))

as they do nothing (i just copied them from an example thinking they are the important)


see the final code tif_stacking.py
'''



