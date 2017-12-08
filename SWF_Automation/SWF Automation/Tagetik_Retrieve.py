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


url = 'https://springswindowfashions.saastagetik.com/prod/5#!/PROD_TGK_SPRINGSWINDOWFASHIONS_001'

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')


service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
#driver = webdriver.Remote(service.service_url, capabilities)
driver = webdriver.Chrome(driver_file)

i = [1]
for x in i:
    driver.get(url)
    break
press(Key.enter)
t = t + 1
print t
        

driver.switch_to_active_element()




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
