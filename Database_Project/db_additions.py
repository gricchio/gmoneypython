import os
import pandas

os.chdir(r'C:\Users\gino.ricchio\Desktop\Python Projects\Database')

database = 'database.csv'

df = pandas.read_csv(database, index_col= 0)

print(df.head(5))