'''
Created on Oct 9, 2017

@author: riccga
'''
import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 1 Facility Reviews.xlsm'

#Change to project dir
os.chdir(cpu_files)

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#look at combrows