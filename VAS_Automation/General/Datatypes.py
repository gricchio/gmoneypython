import pandas
import os

#Get to Project Directory
project_folder = r'C:\Users\gino.ricchio\Desktop\Python Projects\iReports'
os.chdir(project_folder)

#Open File
folder = os.listdir(project_folder)[0]
os.chdir(os.path.join(project_folder,folder))

reports = os.listdir(os.getcwd())

df1 = pandas.read_csv(reports[0])

df3 = pandas.Series(df1.dtypes, name=reports[0])


for report in reports[1:]:
    df2 = pandas.read_csv(report)
    df4 = pandas.Series(df2.dtypes, name=report)
    df3 = pandas.concat([df3,df4], axis = 1)
    

df3.to_csv(os.path.join(project_folder,'exporttypes.csv'))
