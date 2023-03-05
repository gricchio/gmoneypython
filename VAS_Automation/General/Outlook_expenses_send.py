
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
    mail.Subject = 'VAS Expense Overview - Previous Month'
    mail.body = "Hello, please see the attached document for your monthly expenses. I look forward to reviewing with you in the near future. Talk soon, Gino"
    attachment1 = str(r"C:\Users\gino.ricchio\Desktop\Python Projects\Expense Separation\New Items/"+ Message + ".xlsx")
    print(attachment1)
    mail.Attachments.Add(Source=attachment1)
    mail.send
    print("Message Sent")

message_email_self('BUS DEV')
