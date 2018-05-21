'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver


# get the path of IEDriverServer
pathIE = os.path.dirname(__file__)
ie_driver_path = pathIE + "\IEDriverServer.exe"

# create a new Internet Explorer session
driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")


'''from selenium import webdriver
import time

browser_name = {'browserName': 'opera'}
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=browser_name)
time.sleep(2)
driver.get('http://www.baidu.com')
print(driver.current_url)
driver.close()'''