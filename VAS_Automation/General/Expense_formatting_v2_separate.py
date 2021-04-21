'''
Created on Mar 5, 2020

@author: Gino.Ricchio
'''
#Imports
import os 
import xlwings as xw
#hello
#Variables
project_folder = r"C:\Users\gino.ricchio\Desktop\Python Projects\Expense Separation"
break_out = ['PD - Kevin',
            'BUS DEV',
            'EQUIPMENT',
            'FIELD MARKETING',
            'FINANCE',
            'HR',
            'IT',
            'MANAGEMENT',
            'SALES',
            'SUPPORT',
            'WAREHOUSE'
            ]

#Code

os.chdir(project_folder)

files = []
for name in os.listdir(project_folder):
    if os.path.isfile(os.path.join(project_folder, name)):
        files.append(name)

source = xw.Book(files[0])


os.chdir(os.path.join(project_folder,'New items'))

for dept in break_out:
    new = xw.Book()
    if dept == 'PD - Kevin':
        source.sheets['ENGINEERING'].copy(before=new.sheets[0])
        source.sheets['PROD MGMT'].copy(before=new.sheets[0])
    else: print('Only one dept')
    source.sheets[dept].copy(before=new.sheets[0])
    source.sheets['Roll Up'].copy(before=new.sheets[0])
    source.sheets['Consolidated'].copy(before=new.sheets[0])
    new.sheets['Sheet1'].delete()
    new.save(str(dept + '.xlsx'))
    new.close()


