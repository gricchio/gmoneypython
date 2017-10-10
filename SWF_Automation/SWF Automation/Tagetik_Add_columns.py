'''
Created on Oct 9, 2017

@author: riccga
'''
import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 1 Facility Reviews.xlsm'

sheets = ['Assembly Actuals','Component Actuals']
#col_to_insert = ['C','E','G','J','L','O','R','T','W']
col_to_insert = [3,5,7,10,12,15,18,20,23]
assembly_unit_of_measure_row = 14
chart_gap  = 92

rows_needed_for_formulas = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,78,79,80,81,82,86,88,92,93]


def insert_format(col):
    for col in col_to_insert:
        ws.Columns(col).EntireColumn.Insert()
        ws.Columns(col).ColumnWidth = 7.71
        ws.Columns(col).Font.ColorIndex = 16
        ws.Columns(col).NumberFormat = "0.00"


#Change to project dir
os.chdir(cpu_files)

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

xl.Workbooks.Open(workbook)


ws = xl.Worksheets('Assembly Actuals')


#insert columns
"""
for sheet in sheets:
    ws = xl.Worksheets(sheet)
    insert_format(col_to_insert)

"""

ws.Cells(3,8).Formula = "=iferror(" + str() 

"""
for columns in col_to_insert:
    for row in rows_needed_for_formulas:
        




xl.ActiveSheet.Cells(2,7).Value = "Testing"
ws.Cells(3,8).Value = ":-)"
ws.Columns("B").EntireColumn.Insert()
"""