'''
Created on Oct 9, 2017

@author: riccga
'''
import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 1 Facility Reviews.xlsm'

sheets = ['Assembly Actuals','Component Actuals']
insert_list = ['C','E','G','J','L','O','R','T','W']

def insert_format(col):
    for col in insert_list:
        ws.Columns(col).EntireColumn.Insert()
        ws.Columns(col).ColumnWidth = 7.71
        ws.Columns(col).Font.ColorIndex = 16


#Change to project dir
os.chdir(cpu_files)

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

xl.Workbooks.Open(workbook)

ws = xl.Worksheets('Assembly Actuals')


#insert columns
for sheet in sheets:
    ws = xl.Worksheets(sheet)
    insert_format(insert_list)
    
ws.Columns("C").Copy()
ws.Columns("O").PasteSpecial(Paste= "xlPasteFormats")



"""
xl.ActiveSheet.Cells(2,7).Value = "Testing"
ws.Cells(3,8).Value = ":-)"
ws.Columns("B").EntireColumn.Insert()
"""