'''
Created on Apr 18, 2018

@author: riccga
'''
import os
import win32com.client

location = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'

# in the real one we have to look at column E


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

count_assby = 0
count_comps = 0

"""

#If Excel is already Running -------

wb = win32com.client.GetObject(files)

#If Excel is already Running -------
"""
#new pieces

count_assby = 0
count_comps = 0


# Getting the number of assembly depts
wsa = wb.Worksheets("Assembly Actuals")
cola = wsa.Range("H1:H2000")
for cell in cola:
    if cell.Value == "Equivalent Units":
        count_assby = count_assby + 1

print count_assby

wsc = wb.Worksheets("Component Actuals")
colc = wsc.Range("H1:H2000")
for cell in colc:
    if cell.Value == "Earned Hours":
        count_comps = count_comps + 1
print count_comps



    
