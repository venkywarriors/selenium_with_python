'''
Created on May 30, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
import os
import time

class RunFFTests():

    def test(self):
        
        #executable_path = os.path.abspath('..')  + "\\Drivers\\geckodriver.exe"
        # Instantiate FF Browser Command
        driver = webdriver.Firefox(executable_path=r'C:\\Users\venkateshwara.d\\git\\selenium_with_python\\Python_basics\\Drivers\\geckodriver.exe')
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        
        time.sleep(10)
        driver.quit()

ff = RunFFTests()
ff.test()
