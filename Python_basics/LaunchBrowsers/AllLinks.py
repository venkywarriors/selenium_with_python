'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)


driver.get('https://www.w3.org/')
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))
    
    
driver.close()    