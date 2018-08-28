#! python
'''
This file loops through the directory where the scans are and give them consistent names that can be ordered (files that are names R1_x will be named R10_x).
'''
import os
import re
import shutil

dir = '../remote/Input/microfilms-scans/R1'

files = os.listdir(dir)

for file in files:
    if bool(re.match('R1_[0-9]+',file)):
        capture = re.match('R1_([0-9]+)',file).group(1)
        print('Change name to R10_{0}'.format(capture))
        new_name = 'R10_{0}.tif'.format(capture)
        file_path     = os.path.join(dir,file)
        new_name_path = os.path.join(dir,new_name)
        shutil.move(file_path,new_name_path)
