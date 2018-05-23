'''
Created on May 22, 2018

@author: venkateshwara.d
'''
import unittest
import os
from selenium import webdriver
import time

class DynamicWebTable1(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        cls.driver=webdriver.Chrome(chrome_driver_path)
        
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://qavalidation.com/demo/")

    def test_get_table_data(self):
        time.sleep(10)
        columns = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr[1]/td"))
        rows = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr"))
        print("rows - ",rows)   # rows -  3
        print("columns - ",columns) #columns -  4
        
        for row in range(rows):
            for col in range(columns):
                values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+row+"]/td["+col+"]").text
                print(" Dynamic web table index {row} ,{col} value is {values} ".format(row, col, values))
                
    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        
'''
Getting console error

test_get_table_data (__main__.DynamicWebTable1) ... rows -  3
columns -  4
ERROR

======================================================================
ERROR: test_get_table_data (__main__.DynamicWebTable1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\venkateshwara.d\git\selenium_with_python\Python_basics\SeleniumWebDriver_Advanced\DynamicWebTable1.py", line 34, in test_get_table_data
    values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+row+"]/td["+col+"]").text
TypeError: must be str, not int

----------------------------------------------------------------------
Ran 1 test in 36.211s

FAILED (errors=1)'''


if __name__ == '__main__':
    unittest.main(verbosity=2)