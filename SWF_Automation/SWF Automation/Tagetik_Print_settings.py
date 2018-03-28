'''
Created on Feb 26, 2018

@author: RiccGA
'''
import os
import win32com.client

location = r'C:\Users\riccga\Desktop\Python Exports\Print Settings'

print_area = "B6:X925"

chart_gap  = 92
number_of_charts = 10

chart_start = "A2"
final_row = 98 + (number_of_charts - 1)*chart_gap
chart_end = "Y" + str(final_row)




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
#"""
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#Open workbook
wb = xl.Workbooks.Open(files)


"""

#If Excel is already Running -------

wb = win32com.client.GetObject(files)

#If Excel is already Running -------
"""
ws = wb.Worksheets("Assembly Actuals")

ws.ResetAllPageBreaks()

ws.Application.ActiveWindow.View = 2

ws.PageSetup.PrintArea = ws.Range(chart_start,chart_end).Address

for i in range(0,number_of_charts):
    first_number = i*chart_gap + 99
    hpagebreak = "A" + str(first_number)    
    xl.ActiveWindow.SelectedSheets.HPageBreaks.Add(Before=ws.Range(str(hpagebreak)))
    
    
    
    
    
    
    
    
    
    