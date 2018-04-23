'''
Created on Apr 23, 2018

@author: riccga

'''


import pandas as pd
import win32com.client
import shutil
import os
import time

start = time.time()

Sources = r'C:\Users\riccga\Desktop\Python Exports\Vlookup\Sources'
lookupmaterial = r'C:\Users\riccga\Desktop\Python Exports\Vlookup\Data'

os.chdir(lookupmaterial)

#File Name then sheet name
base = os.listdir(os.getcwd())
ref = 'Sheet1'

reference_file = pd.read_excel(base[0], sheet_name=ref)

#print reference_file.head(5)


os.chdir(Sources)
sourcesdir = os.listdir(os.getcwd())
ref2 = 'Sheet1'

lookuptable = pd.read_excel(sourcesdir[0], sheet_name=ref2)

#print lookuptable.head(5)

final = pd.merge(reference_file, lookuptable, how='left', left_on='Person', right_on='Person')

print final