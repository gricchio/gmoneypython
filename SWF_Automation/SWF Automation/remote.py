'''
Created on Nov 21, 2017

@author: riccga
'''

import win32com.client
import time
import os
from __builtin__ import file

loc = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'
excel_sheet = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files\Middleton.xlsm'


for t in range(0, 1000):
    time.sleep(3)
    Application = win32com.client.Dispatch("Excel.Application")
    Application.Visible = 1
    Application.DisplayAlerts = 'false'
    wb = Application.Workbooks.Open(excel_sheet)
    time.sleep(2)
    Application.Quit()
