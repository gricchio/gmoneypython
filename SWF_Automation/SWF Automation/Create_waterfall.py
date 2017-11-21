'''
Created on Nov 9, 2017

@author: riccga
'''
import win32com.client
import shutil
import os
import pandas as pd


SourceFolder = r'C:\Users\riccga\Desktop\Python Exports\Waterfalls'
os.chdir(SourceFolder)
if not os.path.exists("Export"):
    os.mkdir("Export")
destination = r'C:\Users\riccga\Desktop\Python Exports\Waterfalls\Export'
Server_folder = r'G:\Groups\Everyone\2016 FRN Reynosa Mecho\Inventory Takeover\Inventory cutover test'

index_col = 0
columns_to_pull = "Q:W" #can specify number of cols, individual columns separated Etc.
rows_to_pull = 100
sheet_name = 'Fixed - GRY'



for file in raw_data.filesnames:
    data = pd.read_excel(file, sheetname = sheet_name, index_col=index_col, parse_cols=columns_to_pull).head(rows_to_pull)
    data2 = pd.read_excel(file, sheetname = sheet_name, index_col= 14, parse_cols= "H:W").head(rows_to_pull)
    data['Validation Notes'] = data2['Other notes for validation'].values
    data['File'] = '=hyperlink("' + os.path.join(SourceFolder,file) + '")'
    #data['File'] = '=hyperlink("' + os.path.join(Server_folder,file) + '")'
    combined = combined.append(data)
    print file + " - Appended"
    


combined.to_excel(os.path.join(destination,'raw_export.xlsx'))   
