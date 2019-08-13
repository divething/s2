#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:25:14 2019

@author: tamir
"""

import tkinter
from tkinter import filedialog



root = tkinter.Tk()
root.withdraw()
dirname = filedialog.askdirectory(parent=root,initialdir="/home/tamir/Documents/",title='Please select a directory')
print(dirname)









################################################################################
    
    
from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

mainloop()

################################################################################
  
    
import os

path = '/home/tamir/Documents/sentinel_images_for_burn/originals'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.zip' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)



#################################################################################
    
    
import glob

#path = 'c:\\projects\\hc2\\'

files2 = [n for n in glob.glob(path + "**/*.txt", recursive=True)]

for n in files:
    print(n)



################################################################################
    
    
  from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

mainloop()

  
    
    
    
    
    
    