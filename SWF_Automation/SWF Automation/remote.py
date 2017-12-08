'''
Created on Nov 21, 2017

@author: riccga
'''

from pynput.mouse import Button, Controller
import time
import os
from __builtin__ import file


mouse = Controller()

mouse.position = (30,30)

while True:
    mouse.position = (500,500)
    time.sleep(3)
    mouse.move(5,0)
    time.sleep(3)
    mouse.move(0,5)
    time.sleep(3)
    mouse.move(-5,0)
    time.sleep(3)
    mouse.move(0,-5)
    time.sleep(3)
    mouse.press(Button.left)
    time.sleep(3)
    mouse.release(Button.left)
    time.sleep(3)
    
