'''
Created on Jan 9, 2017

@author: riccga
'''

import win32com.client
import os
import time 
import shutil

Server_location = r'G:\Groups\FP&A\2017\Live Files\Facility Files'

SourceFolder = r'C:\Users\riccga\Desktop\Python Exports\Facility Files\Previous'
current_time = time.strftime("%I:%M:%S")
current_date = time.strftime("%m") + "-" + time.strftime("%d") + "-" + time.strftime("%Y")
destination = r'C:\Users\riccga\Desktop\Python Exports\Facility Files'

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
    

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

def add_path(filename):
    filenames = list_files(filename)
    files = []
    for entity in filenames:
        string = os.path.join(SourceFolder,entity)
        files.append(string)
    return files

def add_serverpath(filename):
    filenames = list_files(filename)
    files = []
    for entity in filenames:
        string = os.path.join(Server_location,entity)
        files.append(string)
    return files

print("Hello, please wait while I move your files")


for sheet in add_serverpath(Server_location):
    shutil.copy(sheet,SourceFolder)
    print sheet

print ('Removing Thumbs.db')

os.remove(os.path.join(SourceFolder,'Thumbs.db'))


print "Moved files from " + Server_location + "to " + destination

print ('Files Complete')

message_email_self("Files pulled to local PC")


