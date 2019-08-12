#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:35:37 2019

this function unzips a file

inputs:
s2_list_zip 
img_no
s2_path


its asking for <s2_list_zip> which is a list of files and you need to specify 
the number ofthe file in the the list or loop <img_no>
it will create a filder in a in "temp" folder within the path <s2_path>









@author: ubu
"""


###########################################################
### unzipping
##############################################

# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_to_zip = s2_list_zip[img_no]
  
# opening the zip file in READ mode 
#   with ZipFile("/media/ubu/drive/github/sentinel/input_images/S2B_MSIL2A_20190506T081609_N0212_R121_T36RXV_20190506T113753.zip", 'r') as zip: 

with ZipFile(file_to_zip, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall(os.path.join(s2_path, "temp") ) 
    print('Done!') 

#############################################################
