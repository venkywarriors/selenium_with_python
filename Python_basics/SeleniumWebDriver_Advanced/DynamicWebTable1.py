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
        print("rows - ",rows)
        print("columns - ",columns)
        for row in range(1,3):
            for col in range(1,3):
                values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+row+"]/td["+col+"]").text
                
               # .//*[@id='table01']/tbody/tr[1]/td[2]
                print(values)


    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
         ''' data=[]
        for row in range(rows):
            column=row.find_elements_by_tag_name('td')
            if column:
                data= [td.text for td in column]
            for col in range(len(column)):
                values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+row+"]/td["+col+"]").text
                print(values)
            
        
        print(data)'''  


if __name__ == '__main__':
    unittest.main(verbosity=2)