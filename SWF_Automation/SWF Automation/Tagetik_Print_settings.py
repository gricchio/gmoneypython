'''
Created on Feb 26, 2018

@author: RiccGA
'''
import os
import win32com.client


workbook = 

#create an archive to see what is in the folded -- Need to change name to move files

files = []
os.chdir(moveFiles)
for name in os.listdir(moveFiles):
    if os.path.isfile(os.path.join(moveFiles, name)):
        files.append(name)
for name in os.listdir(recieveFiles):
    if os.path.isfile(os.path.join(recieveFiles, name)):
        files.append(name)




print files


#Dispatch Excel

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

#Open workbook


wb = xl.Workbooks.Open(workbook)