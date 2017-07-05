'''
Created on Feb 24, 2017

@author: riccga
'''
import win32com.client
import shutil
import os
import pandas as pd


SourceFolder = r'C:\Users\riccga\Desktop\Python Exports\Mecho Inventory Project'
os.chdir(SourceFolder)
if not os.path.exists("Export"):
    os.mkdir("Export")
destination = r'C:\Users\riccga\Desktop\Python Exports\Mecho Inventory Project\Export'
Server_folder = r'G:\Groups\Everyone\2016 FRN Reynosa Mecho\Inventory Takeover\Inventory cutover test'

index_col = 0
columns_to_pull = "Q:W" #can specify number of cols, individual columns separated Etc.
rows_to_pull = 100
sheet_name = 'Validation'


class filestructure(object):
    def __init__(self,path):
        self.path = path
        self.filesnames = []
        for name in os.listdir(self.path):
            if os.path.isfile(os.path.join(path,name)):
                self.filesnames.append(name)
        self.filelocations = []
        for name in self.filesnames:
            string = os.path.join(SourceFolder,name)
            self.filelocations.append(string)

        return None

raw_data = filestructure(SourceFolder)
combined = pd.DataFrame()

for file in raw_data.filesnames:
    data = pd.read_excel(file, sheetname = sheet_name, index_col=index_col, parse_cols=columns_to_pull).head(rows_to_pull)
    data2 = pd.read_excel(file, sheetname = sheet_name, index_col= 14, parse_cols= "H:W").head(rows_to_pull)
    data['Validation Notes'] = data2['Other notes for validation'].values
    data['File'] = '=hyperlink("' + os.path.join(SourceFolder,file) + '")'
    #data['File'] = '=hyperlink("' + os.path.join(Server_folder,file) + '")'
    combined = combined.append(data)
    print file + " - Appended"
    


combined.to_excel(os.path.join(destination,'raw_export.xlsx'))   
