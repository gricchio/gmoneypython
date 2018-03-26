'''
Created on Feb 26, 2018

@author: RiccGA
'''
import os
import win32com.client

location = r'C:\Users\riccga\Desktop\Python Exports\Print Settings'

print_area = "B6:X925"


#print folder

os.chdir(location)

files = []
os.chdir(location)
for name in os.listdir(location):
    if os.path.isfile(os.path.join(location, name)):
        files.append(name)
print files

files = os.path.join(location, files[0])

#Dispatch Excel
"""
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#Open workbook
wb = xl.Workbooks.Open(files)

"""

#If Excel is already Running -------

wb = win32com.client.GetObject(files)

#If Excel is already Running -------
#"""
ws = wb.Worksheets("Assembly Actuals")

ws.ResetAllPageBreaks()

ws.PageSetup.PrintArea = ws.Range("A2","D4").Address
                   
#ws.HPageBreaks.Add(ws.Cells(print_area))



#ws.Rows("97:97").Select

#ws.ActiveWindow.SelectedSheets.HPageBreaks.Add