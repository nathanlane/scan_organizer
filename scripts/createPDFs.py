#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script creates a PDF for each one of the folders created by the year-folder.py script.
The PDFs are stored in the Output folder of the Dropbox folder.
"""

import img2pdf, os

os.chdir('/home/felipe/projects/scan_project_nathans/scripts')

# New path where pdf's are going to be stored
path2pdfs = os.path.join(os.pardir,'remote','Output','pdf-by-year')
os.makedirs(path2pdfs, exist_ok=True)

# Path to folders that have the images for each year
path2folders = os.path.join(os.pardir,'local','folders-by-year')

# What years are available
years = os.listdir(path2folders)

# We build the pdf for each year
for y in years:
    
    # Path to the folder that have the images for the current year
    path2year = os.path.join(path2folders,y)
    
    # list the files
    files = os.listdir(path2year)
    
    # get path to the files and sort them
    path2files = [os.path.join(path2year,x) for x in files]
    path2files.sort()
    
    # Create PDF     
    with open(os.path.join(path2pdfs,"{0}.pdf".format(y)),"wb") as f:
        f.write(img2pdf.convert(*path2files))
    
    
    