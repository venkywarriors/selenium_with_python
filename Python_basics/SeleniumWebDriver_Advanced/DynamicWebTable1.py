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
        time.sleep(5)
        columns = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr[1]/td"))
        rows = len(self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr"))
        print("rows - ",rows)   # rows -  3
        print("columns - ",columns) #columns -  4
        
        for row in range(1,rows):
            for col in range(2,columns):
                values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
                print(" Dynamic web table index {0} ,{1} value is {2} ".format(row, col, values))
                
    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
