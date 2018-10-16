 

import pandas as pd

import os

import win32com.client

 
pi_template = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price Increase Sample.xlsx'
price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
project_path = r'C:\Users\200460\Desktop\Python Projects\Price List Project'
#price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
#project_path = r'C:\Users\Gino Ricchio\Desktop\Python'


os.chdir(project_path)
increase_master = pd.ExcelFile(price_data_location)

df = pd.read_excel(increase_master, "Sheet1")
soldtos = []
for i in df['Soldto'].values:
    if i not in soldtos:
        soldtos.append(i)

print df.head(20)
print soldtos
df = df.set_index(['Soldto'])
df['Delta'] = df['NEW'] - df['OLD']
#print df.loc[912019]

print "this is Gino"
"""
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'
wb = xl.Workbooks.Open(pi_template)
"""


