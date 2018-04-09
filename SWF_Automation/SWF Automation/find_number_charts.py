'''
Created on Apr 7, 2018

@author: RiccGA
'''
import os
import win32com.client

location = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'

#change to folder

os.chdir(location)

files = []
os.chdir(location)
for name in os.listdir(location):
    if os.path.isfile(os.path.join(location, name)):
        files.append(name)
print files

files = os.path.join(location, files[0])


"""
#instance excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#Open workbook
wb = xl.Workbooks.Open(files)

"""

#If Excel is already Running -------

wb = win32com.client.GetObject(files)

#If Excel is already Running -------

ws = wb.Worksheets("Assembly Actuals")

if ws.Range("H14").Value != "Equivalent Units":
    ws.Rows(3).EntireRow.Delete()

number_of_charts = []

for cell in range(0,10,1):
    if ws.Range("H" + str(cell*92+14)).Value == "Equivalent Units":
        number_of_charts.append(cell)

print number_of_charts
