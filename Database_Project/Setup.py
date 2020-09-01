import os
import pandas

os.chdir(r'C:\Users\gino.ricchio\Desktop\Python Projects\Database')
book1 = 'book1.xlsx'
book2 = 'book2.xlsx'


df1 = pandas.read_excel(book1)

print(df1.head(5))

df2 = pandas.read_excel(book2)

print(df2.head(5))

result = pandas.merge(df1,df2)

result.to_csv('database.csv')

