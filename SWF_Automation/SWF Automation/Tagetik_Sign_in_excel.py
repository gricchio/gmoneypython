'''
Created on Sep 22, 2017

@author: riccga
'''
import xlsxwriter as xw
import os
import win32com.client
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller
import time
from pywinauto import application, Desktop

tgtfile = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Home.xlsx'
tagpath = r'C:\Users\riccga\Desktop\Python Exports\Tagetik'

os.chdir(tagpath)

def press(x):
    keyboard.press(x)
    keyboard.release(x)
keyboard = Controller()
select_tag = ['y','1']
login = ['y', '2']

app = application.Application()
app.connect(path = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
"""

app = application.Application()
app.start(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")

time.sleep(7)
press(Key.alt)
print "now"
for item in select_tag:
    press(item)
print "second"
time.sleep(2)
for item in login:
    press(item)

time.sleep(5)
press(Key.enter)
time.sleep(5)
press(Key.enter)
"""

dlg = Desktop(backend="uia").Excel
dlg.Tagetik.click_input()
mouse = Controller()
mouse.press(Button.left)
mouse.release(Button.left)
keyboard = Controller()

press(Key.alt)

for item in login:
    press(item)

time.sleep(5)
press(Key.enter)
time.sleep(5)
press(Key.enter)

#dlg.print_control_identifiers()