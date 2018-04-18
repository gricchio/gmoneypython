'''
Created on Oct 9, 2017

@author: riccga
'''
import os
import win32com.client

cpu_files = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
workbook = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Reynosa 1 Facility Reviews.xlsm'

sheets = ['Assembly Actuals','Component Actuals']
#sheets = ['Assembly Actuals']
#sheets = ['Component Actuals']
col_to_insert = ['C','E','G','J','L','O','R','T','W']
col_before = ['B','D','F','I','K','N','Q','S','V']
#col_to_insert = [3,5,7,10,12,15,18,20,23]
assembly_unit_of_measure_row = 14
chart_gap  = 92
#number_of_charts = 4

#should be 10
'''
MD - 10
R1 - 10
R2 - 6
TJ - 4
Cta - 3
Gry - 1


'''



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
while True:
    try:
        if xl.Worksheets("Assembly Actuals").Range("E14").Value != "Equivalent Units":
            xl.Worksheets("Assembly Actuals").Rows(1).EntireRow.Delete()
        break
    except:
        break
     
while True:
    try:
        if xl.Worksheets("Component Actuals").Range("E14").Value != "Earned Hours":
            xl.Worksheets("Component Actuals").Rows(1).EntireRow.Delete() 
        break
    except:
        break


#Number of Charts - New section

count_assby = 0
count_comps = 0


# Getting the number of assembly depts
wsa = wb.Worksheets("Assembly Actuals")
cola = wsa.Range("E1:E2000")
for cell in cola:
    if cell.Value == "Equivalent Units":
        count_assby = count_assby + 1

print "Number of Assembly departments is: " + str(count_assby)

wsc = wb.Worksheets("Component Actuals")
colc = wsc.Range("E1:E2000")
for cell in colc:
    if cell.Value == "Earned Hours":
        count_comps = count_comps + 1
print "Number of Component departments is: " + str(count_comps)



#insert columns / Formatting


ws = wsa
insert_format(col_to_insert)
for x in range(0,count_assby):
    for column in col_to_insert:
        for row in rows_needed_for_formulas:
            ws.Range(column + str(row + (x*chart_gap))).Formula = "=iferror(offset(" + column + str(row + (x*chart_gap)) + ",0,-1)" + "/" + "offset(" + column + str(assembly_unit_of_measure_row + (x*chart_gap)) + ",0,-1)" +",0)"
          


ws = wsc
insert_format(col_to_insert)
for x in range(0,count_comps):
    for column in col_to_insert:
        for row in rows_needed_for_formulas:
            ws.Range(column + str(row + (x*chart_gap))).Formula = "=iferror(offset(" + column + str(row + (x*chart_gap)) + ",0,-1)" + "/" + "offset(" + column + str(assembly_unit_of_measure_row + (x*chart_gap)) + ",0,-1)" +",0)"
          

  


#all the print settings
chart_start = "A2"
final_row = 98 + (count_assby - 1)*chart_gap
chart_end = "Y" + str(final_row)

#print folder
#used from above

#Dispatch Excel

#usedfrom above

ws = wsa

ws.Activate()

ws.ResetAllPageBreaks()

ws.Application.ActiveWindow.View = 2

ws.PageSetup.PrintArea = ws.Range(chart_start,chart_end).Address

for i in range(0,count_assby):
    first_number = i*chart_gap + 99
    hpagebreak = "A" + str(first_number)    
    xl.ActiveWindow.SelectedSheets.HPageBreaks.Add(Before=ws.Range(str(hpagebreak)))

#all the print settings
chart_start = "A2"
final_row = 98 + (count_comps - 1)*chart_gap
chart_end = "Y" + str(final_row)

ws = wsc

ws.Activate()

ws.ResetAllPageBreaks()

ws.Application.ActiveWindow.View = 2

ws.PageSetup.PrintArea = ws.Range(chart_start,chart_end).Address

for i in range(0,count_comps):
    first_number = i*chart_gap + 99
    hpagebreak = "A" + str(first_number)    
    xl.ActiveWindow.SelectedSheets.HPageBreaks.Add(Before=ws.Range(str(hpagebreak)))

wb.Close(True)
print str(files) + " --- complete"    


