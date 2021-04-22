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


#email list
break_out2 = {"PD - Kevin" : "gino.ricchio@vas.com",
            "BUS DEV": "ginoricchio@gmail.com",
            "EQUIPMENT": "gino.ricchio@vas.com",
            "FIELD MARKETING": "gino.ricchio@vas.com",
            "FINANCE": "gino.ricchio@vas.com",
            "HR": "gino.ricchio@vas.com",
            "IT": "gino.ricchio@vas.com",
            "MANAGEMENT": "gino.ricchio@vas.com",
            "SALES": "gino.ricchio@vas.com",
            "SUPPORT": "gino.ricchio@vas.com",
            "WAREHOUSE": "gino.ricchio@vas.com"
            }

#send function
import win32com.client

def message_email_self(Message):
    outlook = win32com.client.Dispatch('outlook.application')
    workemail = break_out2[Message]
    mail = outlook.createitem(0)
    mail.To = workemail
    mail.Subject = 'VAS Expense Overview - ' + Message
    mail.body = "Hello, please see the attached document for your monthly expenses. I look forward to reviewing with you in the near future. Talk soon, Gino"
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


