'''
Created on Jan 30, 2017

@author: riccga
'''
import win32com.client

def message_email_self(Message):
    outlook = win32com.client.Dispatch('outlook.application')
    mycell = '2629942040@mms.att.net'
    workemail = 'gino.ricchio@springswindowfashions.com'
    mail = outlook.createitem(0)
    mail.To = workemail
    mail.Subject = 'Sent by Python'
    mail.body = Message
    mail.send
    print "Message Sent"

message_email_self("This is a Test Email")