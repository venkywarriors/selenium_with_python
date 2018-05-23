'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver
import time

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
driver.get('http://codepad.org')
 
# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button.click()
 
# type text
text_area = driver.find_element_by_id('textarea')
time.sleep(3)

text_area.clear()

text_area.send_keys("print('Hello World')")

# click submit button
submit_button = driver.find_element_by_css_selector(".g-recaptcha") 
submit_button.click()

driver.close()

