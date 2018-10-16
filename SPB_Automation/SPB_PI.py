 

import pandas as pd

import os
import xlwings as xw
import win32com.client


 
#pi_template = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price Increase Sample.xlsx'
#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
#project_path = r'C:\Users\200460\Desktop\Python Projects\Price List Project'
price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
project_path = r'C:\Users\Gino Ricchio\Desktop\Python'
pi_template = r'C:\Users\Gino Ricchio\Desktop\Python\Price Increase Sample.xlsx'

os.chdir(project_path)
increase_master = pd.ExcelFile(price_data_location)

df = pd.read_excel(increase_master, "Sheet1")
soldtos = []
for i in df['Soldto'].values:
    if i not in soldtos:
        soldtos.append(i)

#print df.head(20)
#print soldtos
df = df.set_index(['Soldto'])
df['Delta'] = df['NEW'] - df['OLD']
df['Prc CHG'] = df['Delta'] / df['OLD']

df['OLD'] = df['OLD'].round(2)
df['Delta'] = df['Delta'].round(2)
df['Prc CHG'] = df['Prc CHG'].round(2)


print df.loc[912019]

wb = xw.Book(pi_template)
ws = wb.sheets[0]
ws.range('B13').options(index=False, header=False).value = df.loc[7021991]

#xw.apps[0].quit()



"""
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'
wb = xl.Workbooks.Open(pi_template)
sheet = wb.Worksheets(1)
sheet.Range('B13:I51').Value = df.loc[912019]
"""



"""
#If Excel is already Running -------

wb = win32com.client.GetObject(pi_template)

#If Excel is already Running -------

"""