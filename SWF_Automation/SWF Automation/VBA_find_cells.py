'''
Created on Apr 10, 2018

@author: riccga
'''


import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 2 March - final.xlsm'
#Change to project dir
os.chdir(cpu_files)

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'


wb = xl.Workbooks.Open(workbook)
    
ws = xl.Worksheets("Assembly Actuals")

NumWords = ws.Application.WorksheetFunction.CountIf("Worksheets("Assembly Actuals").Range("H1:H1200").Value","Equivalent Units")

print NumWords