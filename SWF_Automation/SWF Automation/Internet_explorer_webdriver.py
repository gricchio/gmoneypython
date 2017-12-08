'''
Created on Dec 8, 2017

@author: RiccGA
'''
import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key


def press(x):
    keyboard.press(x)
    keyboard.release(x)
keyboard = Controller()


service = r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\IEDriverServer.exe'

url = 'https://springswindowfashions.saastagetik.com/prod/5#!/PROD_TGK_SPRINGSWINDOWFASHIONS_001'

#xpaths




driver = webdriver.Ie(service)
driver.get(url)

taco = [0,1]

for i in taco:
    time.sleep(3)
    press(Key.enter)

time.sleep(5)

forecasting = driver.find_element_by_xpath(r'//*[@id="tgk.main.workarea"]/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div[1]/div')

forecasting.click()