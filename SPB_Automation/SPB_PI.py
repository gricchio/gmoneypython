 

import pandas as pd

import os
import xlwings as xw



#-------------Project Locations

pi_template = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price Increase Sample.xlsx'
price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_real.xlsx'
#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
project_path = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Completed'
#price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
#project_path = r'C:\Users\Gino Ricchio\Desktop\Python\Completed'
#pi_template = r'C:\Users\Gino Ricchio\Desktop\Python\Price Increase Sample.xlsx'

#-------------Move to Project Path

os.chdir(project_path)

#-------------Load Data Frame

increase_master = pd.ExcelFile(price_data_location)
master = pd.read_excel(increase_master, "CustomerMaterial")

soldtos = []
for i in master['Customer'].values:
    if i not in soldtos:
        soldtos.append(i)
print len(soldtos)
master = master.set_index(['Customer'])

for account_name in soldtos[0:3]:
    print "Now working on customer number " + str(account_name)
    wb = xw.Book(pi_template)
    ws = wb.sheets[0]
    ws.range('C9').value = account_name
    ws.range('C10').value = account_name
    #need to add 'UPC' in lieu of DCHL
    df2 = master.loc[[account_name], ['Item','DChl', 'Description', 'UOM', 'PR00', 'NEW']]
    df2['Delta'] = df2['NEW'] - df2['PR00']
    df2['Prc CHG'] = df2['Delta'] / df2['PR00']
    df2['PR00'] = df2['PR00'].round(2)
    df2['Delta'] = df2['Delta'].round(2)
    df2['Prc CHG'] = df2['Prc CHG'].round(2)
    ws.range('B13').options(index=False, header=False).value = df2.loc[[account_name]]
    wb.save(os.path.join(project_path,str(account_name) + " Price Increase 2019.xlsx"))
    wb.close()
