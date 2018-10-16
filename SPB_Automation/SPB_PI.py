 

import pandas as pd

import os
import xlwings as xw
import win32com.client


#-------------Project Locations

#pi_template = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price Increase Sample.xlsx'
#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
#project_path = r'C:\Users\200460\Desktop\Python Projects\Price List Project'
price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
project_path = r'C:\Users\Gino Ricchio\Desktop\Python\Completed'
pi_template = r'C:\Users\Gino Ricchio\Desktop\Python\Price Increase Sample.xlsx'

#-------------Move to Project Path

os.chdir(project_path)

#-------------Load Data Frame

increase_master = pd.ExcelFile(price_data_location)
df = pd.read_excel(increase_master, "Sheet1")
soldtos = []
for i in df['Soldto'].values:
    if i not in soldtos:
        soldtos.append(i)

df = df.set_index(['Soldto'])
df['Delta'] = df['NEW'] - df['OLD']
df['Prc CHG'] = df['Delta'] / df['OLD']

df['OLD'] = df['OLD'].round(2)
df['Delta'] = df['Delta'].round(2)
df['Prc CHG'] = df['Prc CHG'].round(2)

for account_name in soldtos:
    print "Now working on customer number " + str(account_name)
    wb = xw.Book(pi_template)
    ws = wb.sheets[0]
    ws.range('C9').value = account_name
    ws.range('C10').value = account_name
    ws.range('B13').options(index=False, header=False).value = df.loc[account_name]
    wb.save(os.path.join(project_path,str(account_name) + ".xlsx"))
#xw.apps[0].quit()