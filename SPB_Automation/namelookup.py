import pandas as pd

customer_names = r'C:\Users\200460\Desktop\Python Projects\Price List Project\COPA_backup.xlsx'

cn = pd.ExcelFile(customer_names)
cnmaster = pd.read_excel(cn, "Backup")

c_name = cnmaster.loc[cnmaster['CustomerName'] == 100083]

print c_name