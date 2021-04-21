

break_out = {"PD - Kevin" : "gino.ricchio@vas.com",
            'BUS DEV': 'gino.ricchio@vas.com',
            'EQUIPMENT': 'gino.ricchio@vas.com',
            'FIELD MARKETING': 'gino.ricchio@vas.com',
            'FINANCE': 'gino.ricchio@vas.com',
            'HR': 'gino.ricchio@vas.com',
            'IT': 'gino.ricchio@vas.com',
            'MANAGEMENT': 'gino.ricchio@vas.com',
            'SALES': 'gino.ricchio@vas.com',
            'SUPPORT': 'gino.ricchio@vas.com',
            'WAREHOUSE': 'gino.ricchio@vas.com'
            }


import win32com.client

def message_email_self(Message):
    outlook = win32com.client.Dispatch('outlook.application')
    workemail = 'gino.ricchio@vas.com'
    mail = outlook.createitem(0)
    mail.To = workemail
    mail.Subject = 'VAS Expense Overview - Previous Month'
    mail.body = "Hello, please see the attached document for your monthly expenses. I look forward to reviewing with you in the near future. Talk soon, Gino"
    attachment1 = r"C:\Users\gino.ricchio\Desktop\Python Projects\Expense Separation\VAS Expense Mar.xlsx"    
    mail.Attachments.Add(Source=attachment1)
    mail.send
    print("Message Sent")

message_email_self("Hello, please see the attacehd document for your monthly expenses. I look forward to reviewing with you in the near future.")
