'''
Created on Mar 23, 2020

@author: Gino.Ricchio
'''

import os
import shutil

parent = r'C:\Users\gino.ricchio\Valley Agriculture Software\Finance - Accounting\Month-End Close\01 - Prior Years\2019\Year End Close\KPMG Files\Revenue Sampling'

os.chdir(parent)


source_folders = [
    r'1 - Revenue Credits',
    r'2 - Revenue Debits',
    r'3 - Sales Discounts',
    r'4 - Revenue Cut off Pre YE',
    r'5 - Revenue Cut Off Post YE',
    ]


#Create a new folder to copy items to
for source in source_folders:
    try:
        os.makedirs(os.path.join(parent,source,"Appended"))
    except FileExistsError:
        pass
"""
for folder in source_folders:
    for item in os.listdir(folder):
        if os.path.isfile(os.path.join(parent,folder,item)):
            shutil.copy(os.path.join(parent,folder,item),os.path.join(parent,folder,"Appended"))
"""

#print(os.listdir(os.path.join(parent,source_folders[0],"Appended")))

#make sure to do this right, last time it modified the source, not the appended version

for folder in source_folders:
    os.chdir(os.path.join(parent,folder,"Appended"))
    for item in os.listdir(os.path.join(parent,folder,"Appended")):
        os.rename(item,folder + item)
