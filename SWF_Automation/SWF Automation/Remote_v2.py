'''
Created on Jan 3, 2018

@author: RiccGA
'''
from pynput.mouse import Button, Controller
import time
import os
from __builtin__ import file


mouse = Controller()
slp = 1
mouse.position = (30,30)

x = "go"
y = raw_input()

while x == "go":
    mouse.position = (500,500)
    time.sleep(slp)
    mouse.move(5,0)
    time.sleep(slp)
    mouse.move(0,5)
    time.sleep(slp)
    mouse.move(-5,0)
    time.sleep(slp)
    mouse.move(0,-5)
    time.sleep(slp)
    mouse.press(Button.left)
    time.sleep(slp)
    mouse.release(Button.left)
    time.sleep(slp)
    if y == "stop":
        break
    
    
