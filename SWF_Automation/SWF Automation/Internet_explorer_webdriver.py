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

def xpath_select_click(x):
    y = driver.find_element_by_xpath(x)
    y.click()
    time.sleep(5)
    
def xpath_click(x):
    y = driver.find_element_by_xpath(x)
    y.click()

service = r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\IEDriverServer.exe'
url = 'https://springswindowfashions.saastagetik.com/prod/5#!/PROD_TGK_SPRINGSWINDOWFASHIONS_001'

curr_Scenario = '2017ACT - 2017 ACTUAL'
curr_pd = '11 - November'

#xpaths

#   Main Menus
forecast_submenu = r'//*[@id="tgk.main.workarea"]/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div[1]/div'
actual_submenu = r'//*[@id="tgk.main.workarea"]/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div'

## Actual Selections

midd_actuals = r'//*[@id="web.vaadin.ui.components.DefaultTgkWindow.mainLayout"]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/table/tbody/tr[12]/td[2]/div/div/div/div[2]'


###Actuals Menu

actuals_Scenario = r'//*[@id="gwt-uid-58"]/div/div/div/div/div/input'
actuals_PD = r'//*[@id="gwt-uid-60"]/div/div/div/div/div/input'
actuals_menu = [actuals_Scenario, actuals_PD]


driver = webdriver.Ie(service)
driver.get(url)

taco = [0,1]

for i in taco:
    time.sleep(3)
    press(Key.enter)

time.sleep(8)

##forecasting = driver.find_element_by_xpath(actual_submenu)
##forecasting.click()

process = [actual_submenu, midd_actuals]

for i in process:
    xpath_select_click(i)

time.sleep(3)
xpath_click(actuals_Scenario)

keyboard.type(curr_Scenario)

xpath_click(actuals_PD)
keyboard.type(curr_pd)
press(Key.enter)


