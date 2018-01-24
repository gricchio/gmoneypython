'''
Created on Jan 11, 2018

@author: riccga
'''


import os
import win32com.client
from pydispatch.dispatcher import send

#find my files

moveFiles = r'C:\Users\riccga\Desktop\Python Exports\Move Columns\From'
recieveFiles = r'C:\Users\riccga\Desktop\Python Exports\Move Columns\To'

column = "X:X"


files = []
os.chdir(moveFiles)
for name in os.listdir(moveFiles):
    if os.path.isfile(os.path.join(moveFiles, name)):
        files.append(name)
for name in os.listdir(recieveFiles):
    if os.path.isfile(os.path.join(recieveFiles, name)):
        files.append(name)




print files

send = os.path.join(moveFiles, files[0])
recieve = os.path.join(recieveFiles, files[1])

if len(files)>2:
    print "Too many files in from Folder"
    quit()

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#grab sheet names for send
sheetz1 = []

sendwb = xl.Workbooks.Open(send)

for sheet in sendwb.Sheets:
    sheetz1.append(sheet.Name)

#grab sheet names for receive
rxwb = xl.Workbooks.Open(recieve)

sheetz2 = []

for sheet in rxwb.Sheets:
    sheetz2.append(sheet.Name) 

if len(sheetz1) != len(sheetz2):
    print "too many sheets"
    quit()
#insert new comments

i = 1
for tab in sheetz1:
    column = "X:X"
    new_ones = [1,2,6,12,15]
    if i in new_ones :
        column = "W:W" 
    sendwb.Sheets(tab).Columns(column).Copy()
    rxwb.Sheets(tab).Select()
    rxwb.Sheets(tab).Range(column).Select()
    rxwb.Sheets(tab).Paste()
    i = i + 1
#sendwb.Close(False)
#rxwb.Close(True)

"""
    for sheet in sheets:
        ws = xl.Worksheets(sheet)
        insert_format(col_to_insert)

    for sheet in sheets:
        ws = xl.Worksheets(sheet)
        for x in range(0,number_of_charts):
            for column in col_to_insert:
                for row in rows_needed_for_formulas:
                    ws.Range(column + str(row + (x*chart_gap))).Formula = "=iferror(offset(" + column + str(row + (x*chart_gap)) + ",0,-1)" + "/" + "offset(" + column + str(assembly_unit_of_measure_row + (x*chart_gap)) + ",0,-1)" +",0)"
                  
"""
    #wb.Close(True)  

print str(files) + " --- complete"    
