'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
 
driver.maximize_window()
 
driver.implicitly_wait(30)

driver.get('http://www.google.com')
 
driver.close()







