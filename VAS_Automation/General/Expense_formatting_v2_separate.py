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
            'PROD MGMT',
            'WAREHOUSE'
            ]


#email list
break_out2 = {"PD - Kevin" : "Kevin.Callihan@vas.com",
            "BUS DEV": "Jordan.KraftLambert@vas.com",
            "PROD MGMT": "Brad.Papineau@vas.com",
            "EQUIPMENT": "Lee.Zwahlen@vas.com",
            "FIELD MARKETING": "Alexis.Smith@vas.com",
            "FINANCE": "Joe.Docter@vas.com",
            "HR": "Jennifer.Davidson@vas.com",
            "IT": "German.Rendon@vas.com",
            "MANAGEMENT": "robin.dunkijacobs@vas.com",
            "SALES": "preston.vincent@vas.com",
            "SUPPORT": "eddie.ormonde@vas.com",
            "WAREHOUSE": "Lee.Zwahlen@vas.com"
            }

#send function
import win32com.client

def message_email_self(Message):
    outlook = win32com.client.Dispatch('outlook.application')
    workemail = break_out2[Message]
    mail = outlook.createitem(0)
    mail.To = workemail
    mail.CC = "joe.docter@vas.com;Steve.Smith@vas.com"
    mail.Subject = 'VAS Expense Overview - ' + Message
    mail.body = "Hello, please see the attached document for your monthly expenses. Please let me know if you have any questions. Talk soon, Gino"
    attachment1 = str(r"C:\Users\gino.ricchio\Desktop\Python Projects\Expense Separation\New Items/"+ Message + ".xlsx")
    print(attachment1)
    mail.Attachments.Add(Source=attachment1)
    mail.send
    print("Message Sent")


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
    message_email_self(dept)


