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

#feeder = r'F:\Drive\Python Test Materials\Std Cost Files\Feeder\feeder.xlsx'
#standards_folder = r'F:\Drive\Python Test Materials\Std Cost Files'
#export_loc = r'F:\Drive\Python Test Materials\Std Cost Files\Export'

standards_folder = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project'
feeder = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Feeder\feeder.xlsx'
export_loc = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Export'
stds_16 = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Std Cost Files\2016 - Costs.xlsx'
stds_17 = r'C:\Users\riccga\Desktop\Python Exports\Standard Cost Project\Std Cost Files\2017 - Costs.xlsx'

#getstandards
os.chdir(export_loc)
if not os.path.exists("Export"):
    os.mkdir("Export")


standards_matrix_16 = pd.DataFrame()
standards_matrix_17 = pd.DataFrame()
    
data = pd.read_excel(stds_16, 0, index_col='SKUWHSE',parse_cols= "A:P")
standards_matrix_16 = standards_matrix_16.append(data)

data2 = pd.read_excel(stds_17, 0, index_col='SKUWHSE',parse_cols= "A:P")
standards_matrix_17 = standards_matrix_17.append(data2)




#standards_matrix.to_excel(os.path.join(export_loc, 'raw_export.xlsx'))

#look up information

lookup_table = pd.DataFrame()


feeder_data = pd.read_excel(feeder, 0, index_col=0, parse_cols="A:G")

feeder_data['Std_cost_16'] = feeder_data.Concat.map(standards_matrix_16.StdTtlCst)
feeder_data['Std_cost_17'] = feeder_data.Concat.map(standards_matrix_17.StdTtlCst)


feeder_data.to_excel(os.path.join(export_loc, 'raw_export.xlsx'))

end = time.time()

print"This process took " + str(end-start) + " seconds, Mr. Ricchio"
