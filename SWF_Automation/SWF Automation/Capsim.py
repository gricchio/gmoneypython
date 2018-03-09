'''
Created on Mar 8, 2018

@author: RiccGA
'''
'''
Created on Sep 15, 2017

@author: RiccGA
'''
import time
from selenium import webdriver
import selenium
import selenium.webdriver.chrome.service as service
from pynput.keyboard import Controller, Key

service = service.Service(r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\chromedriver.exe')
driver_file = r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\chromedriver.exe'
#import selenium.webdriver.ie.service as service
#service = service.Service(r'C:\Users\riccga\Desktop\Python Exports\Github\gmoneypython\SWF_Automation\WebInteract\Drivers\IEDriverServer.exe')

def find_xpath(x):
    element = driver.find_element_by_xpath(x)
    return element

def press(x):
    keyboard.press(x)
    keyboard.release(x)
keyboard = Controller()


url = 'https://ww2.capsim.com/login/'

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')

passw = "hello"

service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
#driver = webdriver.Remote(service.service_url, capabilities)
driver = webdriver.Chrome(driver_file)

try:
    driver.get(url)
except Exception:
    pass

driver.switch_to_active_element()

login = find_xpath('//*[@id="username"]')
login.click()
login.send_keys("gricchio@wisc.edu")

login = find_xpath('//*[@id="password"]')
login.click()
login.send_keys(passw)

press(Key.enter)

time.sleep(5)

logout = find_xpath('//*[@id="header-tabs-inner"]/div[1]/a')
logout.click()

#Click the enter button
"""
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

"""


#driver.close()
