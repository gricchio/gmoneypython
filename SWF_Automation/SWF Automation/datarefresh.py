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
current_year = "2017"

file_list = []

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

def xl_open(workbook):
    Application = win32com.client.Dispatch("Excel.Application")
    Application.Visible = 1
    Application.DisplayAlerts = 'false'
    Application.Workbooks.open(workbook)

def update_date(i):
    cut = i[:-15]
    new = cut + "" + current_date + ".xlsx"
    #took out the space above^^   
    return new

def message_email_self(Message):
    outlook = win32com.client.Dispatch('outlook.application')
    mycell = '2629942040@mms.att.net'
    workemail = 'gino.ricchio@springswindowfashions.com'
    mail = outlook.createitem(0)
    mail.To = workemail
    mail.Subject = 'Sent by Python'
    mail.body = Message
    mail.GetInspector
    mail.send
    print "Message Sent"

message_email_self('File Update has begin for - ' + SourceFolder)

print("Hello, please wait while I refresh your files!")

Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = 1
Application.DisplayAlerts = False


for cpu in add_path(SourceFolder):
    Workbook = Application.Workbooks.open(cpu)
    currentname = Application.ActiveWorkbook.name
    Workbook.RefreshAll()
    time.sleep(540)
    oldname = currentname
    new_name = update_date(oldname)
    Workbook.SaveAs(destination + "/" + new_name)
    Workbook.Close()
    file_list.append(new_name + ' -- Done')
    print (new_name + ' -- Done') 

print ('Files Complete')
Application.quit()

message_email_self('Your information is ready Mr. Ricchio'+"\n"+"\n"+"\n".join(file_list))

