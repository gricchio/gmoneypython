import pandas as pd
import os

project_folder = r'C:\Users\gino.ricchio\Desktop\Python Projects\Comments'
upload_file = r'Comments_sample.xlsx'

#change to Project Directory


os.chdir(project_folder)

#open File

df1 = pd.read_excel(upload_file)



df2 = pd.DataFrame() 

df2['Account Number'] = df1['NAV account number']
df2['Comment1'] = df1['Comment1']

df2 = df2.set_index('Account Number')

print(df2.head(5))