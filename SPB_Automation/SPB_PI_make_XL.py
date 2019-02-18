 

import pandas as pd

import os
import xlwings as xw
from math import ceil
import time

start_time = time.time()


#-------------Project Locations
customer_names = r'C:\Users\200460\Desktop\Python Projects\Price List Project\COPA_backup.xlsx'
pi_template = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price Increase Sample.xlsx'
#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_real.xlsx'
price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Master File V1 10-30-2018.xlsx'
#price_data_location = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Price_data_test.xlsx'
project_path = r'C:\Users\200460\Desktop\Python Projects\Price List Project\Completed'
#price_data_location = r'C:\Users\Gino Ricchio\Desktop\Python\Price_data_test.xlsx'
#project_path = r'C:\Users\Gino Ricchio\Desktop\Python\Completed'
#pi_template = r'C:\Users\Gino Ricchio\Desktop\Python\Price Increase Sample.xlsx'

sheet_name = "A005 Final"

#-------------Move to Project Path

os.chdir(project_path)

#-------------Load Data Frame
skipped = []
increase_master = pd.ExcelFile(price_data_location)
master = pd.read_excel(increase_master, sheet_name)
exceptions = []
soldtos = []
for i in master['Customer'].values:
    if i not in soldtos:
        soldtos.append(i)

print "Number of Price Lists Generating:"
print len(soldtos)

customer_names_file = pd.ExcelFile(customer_names)
df_customernumbers = pd.read_excel(customer_names_file, "Backup")
master = master.merge(df_customernumbers,on='Customer')
master = master.set_index(['Customer'])

master.to_excel("Output Master Table.xlsx")


df_customernumbers = df_customernumbers.set_index(['Customer'])
cndt = df_customernumbers.to_dict('series')

wb = xw.App()

for account_name in soldtos:
    try:
        print "Now working on customer number " + str(account_name)
        wb = xw.apps[0].books.open(pi_template)
        ws = wb.sheets[0]
        ws.range('C9').options(index=False, header=False).value = master.loc[[account_name], ['CustomerName']][0:1]
        ws.range('C10').options(index=False, header=False).value = account_name
        df2 = master.loc[[account_name], ['Material','UPC', 'Description', 'UOM', 'Amount', 'New']]
        df2['Delta'] = df2['New'] - df2['Amount']
        df2['Prc CHG'] = df2['Delta'] / df2['Amount']
        df2['Amount'] = df2['Amount'].round(2)
        df2['Delta'] = df2['Delta'].round(2)
        df2['Prc CHG'] = df2['Prc CHG'].round(2)
        rows = len(df2.loc[[account_name]])
        print str(rows) + " SKU's" 
        if rows > 234:
            exceptions.append(account_name)
        number_of_pages = ceil(len(df2.loc[[account_name]]) / float(39))
        for page in range(0,int(number_of_pages)):
            ws.range("B" + str(13+(page*55))).options(index=False, header=False).value = df2.loc[[account_name]][0+page*39 : 39+page*39]
        wb.save(os.path.join(project_path,str(account_name) + " Price Increase 2019.xlsx"))
    except Exception:
        print "Skip Name"
        print account_name
        skipped.append(account_name)
    wb.close()

print "These Sold to's had more than 234 SKU's"

print exceptions

print "Skipped"

print skipped

print "--- %s Minutes ---" % float(((time.time() - start_time))/60)
xw.App.quit(xw.apps.active)