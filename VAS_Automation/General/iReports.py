import pandas
import os

#Get to Project Directory
project_folder = r'C:\Users\gino.ricchio\Desktop\Python Projects\iReports'
os.chdir(project_folder)

#Open File
folder = os.listdir(project_folder)[0]
os.chdir(os.path.join(project_folder,folder))

reports = os.listdir(os.getcwd())



result = pandas.DataFrame()
df1 = pandas.read_csv(reports[0])

for report in reports:
    df2 = pandas.read_csv(report)
    print(report)
    print(df2.columns)
    df2 = df2.astype({'Herdcode': object}, errors= 'ignore')
    df1 = pandas.merge(df1,df2, how= "outer")

df1.to_csv(os.path.join(project_folder,'export.csv'))
