'''
Created on Sep 22, 2017

@author: riccga
'''
import xlsxwriter as xw
import os
import win32com.client
from pynput.keyboard import Controller, Key
import time

tgtfile = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Home.xlsx'
tagpath = r'C:\Users\riccga\Desktop\Python Exports\Tagetik'

os.chdir(tagpath)

def press(x):
    keyboard.press(x)
    keyboard.release(x)
keyboard = Controller()
select_tag = ['y','1']
login = ['y', '2']


xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = False
xl.Workbooks.Add()


time.sleep(10)
press(Key.alt)
print "now"
for item in select_tag:
    press(item)
print "second"
time.sleep(2)
for item in login:
    press(item)