'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
driver.get('http://imgur.com/')
 
images = driver.find_elements_by_tag_name('img')


for image in images:
    print(image.get_attribute('src'))

 
driver.close()

