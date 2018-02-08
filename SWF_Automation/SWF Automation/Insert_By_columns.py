'''
Created on Jan 31, 2018

@author: riccga
'''

import os
import pandas as pd
import win32com.client

SourceFile = r'C:\Users\riccga\Desktop\Python Exports\Insert Values'
os.chdir(SourceFile)
depts = pd.read_excel("Tag_Dept_Cheatsheet.xlsx")
destination = os.path.join(SourceFile,"Destination.xlsx")
Starting_Cell = "B4"
number_of_rows_to_skip = 7



listofdepts = []



for item in depts["Dept"]:
    listofdepts.append(item)


 
#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'
dest = xl.Workbooks.Open(destination)

#if Excel is already running, then you only need below

dest = win32com.client.GetActiveObject("Excel.Application")

dest.ActiveCell.Select()
insert_cell= Starting_Cell
dest.Range(insert_cell).Select()
for dept in listofdepts:
    dest.ActiveCell.Formula = str(dept)
    dest.ActiveCell.Offset(number_of_rows_to_skip+1,1).Select()
    