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
service = service.Service(r'C:\Users\riccga\Google Drive\Python Test Materials\WebInteract\Drivers\chromedriver.exe')

#import selenium.webdriver.ie.service as service
#service = service.Service(r'C:\Users\riccga\Google Drive\Python Test Materials\WebInteract\Drivers\IEDriverServer.exe')


#url = 'https://lottery.broadwaydirect.com/show/hamilton-chicago/'
url = 'http://www.google.com'
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get(url)

#element = 'class'
Xpath = '//*[@id="lst-ib"]'

xpathlist1 = driver.find_element_by_xpath(Xpath)

#xpathlist1 = driver.find_elements_by_xpath('//*[@' + element + ']')

"""
for ii in xpathlist1[25:50]:
    print ii.get_attribute(element)

object = 'thing_t3_5y1a1x'


"""

xpathlist1.text('Gino')

#driver.close()
