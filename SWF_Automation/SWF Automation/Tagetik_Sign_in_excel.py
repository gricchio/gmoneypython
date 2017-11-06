'''
Created on Sep 22, 2017

@author: riccga
'''
import xlsxwriter as xw
import os
import win32com.client
from pynput.keyboard import Controller, Key
import time

budget_files = r''

drop_data = r"C:\Users\riccga\Desktop\Python Exports\Tagetik\Budget\AOP Evaluation data drop master.xlsx"
eval_template = r"C:\Users\riccga\Desktop\Python Exports\Tagetik\Budget\PPT AOP Eval Summary - Template v3 - Macro.xlsm"

tagpath = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Budget'

os.chdir(tagpath)

def press(x):
    keyboard.press(x)
    keyboard.release(x)
keyboard = Controller()



"""
app = application.Application()
app.connect(path = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
"""

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
xl.DisplayAlerts = 'false'

time.sleep(9)

time.sleep(5)
press(Key.enter)
time.sleep(5)
press(Key.enter)



