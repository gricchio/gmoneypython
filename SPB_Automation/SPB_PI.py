 

import pandas as pd

import os

import win32com.client

 

#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
#project_path = r'C:\Users\200460\Desktop\Python Projects\PrList Project'
price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
project_path = r'C:\Users\Gino Ricchio\Desktop\Python'


os.chdir(project_path)
increase_master = pd.ExcelFile(price_data_location)

df = pd.read_excel(increase_master, "Sheet1")
soldtos = []
for i in df['Soldto'].values:
    if i not in soldtos:
        soldtos.append(i)

print df.head(20)

df = df.set_index(['Soldto'])


#print df.loc[912019]
print soldtos


