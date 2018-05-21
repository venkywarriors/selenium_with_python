'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver
import io
chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)

driver.get('https://python.org')
 
html = driver.page_source

if(os.path.isfile("pageSource.txt")):
    
    os.remove("pageSource.txt")

with io.FileIO("pageSource.txt", "w") as file:
    file.write(html.encode("utf-8"))

driver.close()