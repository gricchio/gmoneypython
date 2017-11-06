'''
Created on Oct 9, 2017

@author: riccga
'''
import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 1 Facility Reviews.xlsm'

sheets = ['Assembly Actuals','Component Actuals']
#sheets = ['Component Actuals']
col_to_insert = ['C','E','G','J','L','O','R','T','W']
col_before = ['B','D','F','I','K','N','Q','S','V']
#col_to_insert = [3,5,7,10,12,15,18,20,23]
assembly_unit_of_measure_row = 14
chart_gap  = 92
number_of_charts = 6
#should be 10

rows_needed_for_formulas = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,78,79,80,81,82,86,88,92,93]


def insert_format(col):
    for col in col_to_insert:
        ws.Columns(col).EntireColumn.Insert()
        ws.Columns(col).ColumnWidth = 7.71
        ws.Columns(col).Font.ColorIndex = 16
        ws.Columns(col).NumberFormat = "0.00"


#Change to project dir
os.chdir(cpu_files)

#build file dispatch

files = []
for name in os.listdir(cpu_files):
    if os.path.isfile(os.path.join(cpu_files, name)):
        files.append(name)

print files

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'


for file in files:
    wb = xl.Workbooks.Open(os.path.join(cpu_files,file))
    
#insert columns / Formatting

    for sheet in sheets:
        ws = xl.Worksheets(sheet)
        insert_format(col_to_insert)

    for sheet in sheets:
        ws = xl.Worksheets(sheet)
        for x in range(0,number_of_charts):
            for column in col_to_insert:
                for row in rows_needed_for_formulas:
                    ws.Range(column + str(row + (x*chart_gap))).Formula = "=iferror(offset(" + column + str(row + (x*chart_gap)) + ",0,-1)" + "/" + "offset(" + column + str(assembly_unit_of_measure_row + (x*chart_gap)) + ",0,-1)" +",0)"
                  

    wb.Close(True)  
    
    

"""


ws.Cells(3,8).Formula = "=iferror("+ "B" + str(86) + "/" + "C" + str(14) +",0)"




xl.ActiveSheet.Cells(2,7).Value = "Testing"
ws.Cells(3,8).Value = ":-)"
ws.Columns("B").EntireColumn.Insert()
"""
