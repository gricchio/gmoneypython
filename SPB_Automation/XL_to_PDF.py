import win32com.client
import os



cpu_files = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Completed\Retail'
PDF_files = r'C:\Users\200460\Desktop\Python Projects\Price List Project\PDF'


os.chdir(cpu_files)
files = []
for name in os.listdir(cpu_files):
    if os.path.isfile(os.path.join(cpu_files, name)):
        files.append(name)

#dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'


for file in files:
    wb = xl.Workbooks.Open(os.path.join(cpu_files,file))
    sheet_count = 0
    
    firsts = ["B13", "B68", "B123", "B178", "B233", "B288"]
    
    wsa = wb.Worksheets("Sheet1")
    
    for row in firsts:
        cola = wsa.Range(row)
        for cell in cola:
            if cell.Value != 0:
                sheet_count = sheet_count + 1
    
    chart_start = "A1"
    chart_gap  = 55
    final_row = 55 + (sheet_count - 1)*chart_gap
    chart_end = "I" + str(final_row)  
    wsa.ResetAllPageBreaks()
    
    wsa.Application.ActiveWindow.View = 2
    
    wsa.PageSetup.PrintArea = wsa.Range(chart_start,chart_end).Address
    
    for i in range(0, sheet_count):
        first_number = i*chart_gap + 56
        hpagebreak = "A" + str(first_number)    
        xl.ActiveWindow.SelectedSheets.HPageBreaks.Add(Before=wsa.Range(str(hpagebreak)))
    wb.Save()
    file = str(file[:len(file)-5])
    xl.ActiveSheet.ExportAsFixedFormat(0,os.path.join(PDF_files, file),0,0,0)
    
    wb.Close(True)