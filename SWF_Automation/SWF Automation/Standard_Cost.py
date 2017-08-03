'''
Created on Aug 2, 2017

@author: riccga
'''

import pandas as pd
import win32com.client
import shutil
import os
import time

start = time.time()

#declarations
index_col = 0
columns_to_pull = 'A:P' #can specify number of cols, individual columns separated Etc.
rows_to_pull = 15
sheet_name = 'Data'
feeder = r'F:\Drive\Python Test Materials\Std Cost Files\Feeder\feeder.xlsx'
#standards_folder = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Std Cost Files'
standards_folder = r'F:\Drive\Python Test Materials\Std Cost Files'
export_loc = r'F:\Drive\Python Test Materials\Std Cost Files\Export'
list_of_files = []

#getstandards
os.chdir(standards_folder)
if not os.path.exists("Export"):
    os.mkdir("Export")

for file in os.listdir(standards_folder):
    if os.path.isfile(file):
        list_of_files.append(file)


standards_matrix = pd.DataFrame()
    
for file in list_of_files:
    year = file[0:5]
    data = pd.read_excel(file, 0, index_col='SKUWHSE',parse_cols= "A:P")
    standards_matrix = standards_matrix.append(data)

#print standards_matrix

#standards_matrix.to_excel(os.path.join(export_loc, 'raw_export.xlsx'))

#look up information

lookup_table = pd.DataFrame()


feeder_data = pd.read_excel(feeder, 0, index_col=0, parse_cols="A:C")

feeder_data['Std_cost'] = feeder_data.Concat.map(standards_matrix.StdTtlCst)

feeder_data.to_excel(os.path.join(export_loc, 'raw_export.xlsx'))

end = time.time()

print"This process took " + str(end-start) + " seconds, Mr. Ricchio"
