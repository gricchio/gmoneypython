'''
Created on Aug 2, 2017

@author: riccga
'''

import pandas as pd
import win32com.client
import shutil
import os

#declarations
index_col = 0
columns_to_pull = "A:P" #can specify number of cols, individual columns separated Etc.
rows_to_pull = 100
sheet_name = 'Data'
standards_folder = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Std Cost Files'
list_of_files = []
os.chdir(standards_folder)

if not os.path.exists("Export"):
    os.mkdir("Export")

for file in os.listdir(standards_folder):
    if os.path.isfile(file):
        list_of_files.append(file)


standards_matrix = pd.DataFrame()
    
for file in list_of_files:
    year = file[0:5]
    Stds = pd.read_excel(file, sheetname = sheet_name, index_col=index_col, parse_cols=columns_to_pull)
    standards_matrix.append(Stds)

print standards_matrix.head(5)
print "yolo"
    
    

