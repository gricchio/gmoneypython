'''
Created on Feb 3, 2017

@author: riccga
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import selenium

import selenium.webdriver.chrome.service as service
from selenium.webdriver.support.expected_conditions import _find_element,\
    _find_elements
service = service.Service(r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\chromedriver.exe')

#import selenium.webdriver.ie.service as service
#service = service.Service(r'C:\Users\riccga\Google Drive\Python Test Materials\WebInteract\Drivers\IEDriverServer.exe')

def find_xpath(x):
    element = driver.find_element_by_xpath(x)
    return element


url = 'https://lottery.broadwaydirect.com/show/hamilton-chicago/'
#url = 'http://www.reddit.com'

service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get(url)

#Click the enter button

Lotterybutton = '//*[@id="1489109400"]/div[5]/a'
Button = find_xpath(Lotterybutton)
Button.click()

#Enter Information
#select input area
z = 12
count = 0
#set count to tab 12 times



#enter information
input.send_keys("Hello World")
firstname.send_keys(Keys.TAB)




#driver.close()
