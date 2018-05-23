'''
Created on May 22, 2018

@author: venkateshwara.d
'''
import unittest
import os
from selenium import webdriver
import time

class DynamicWebTable(unittest.TestCase):

   
    def setUp(self):
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        self.driver=webdriver.Chrome(chrome_driver_path)
        
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://money.rediff.com/gainers/bsc/dailygroupa?")

    def test_count_rows_and_column(self):
        time.sleep(10)
        columns = len(self.driver.find_elements_by_xpath(".//*[@id='leftcontainer']/table/thead/tr/th"))
        rows = len(self.driver.find_elements_by_xpath(".//*[@id='leftcontainer']/table/tbody/tr/td[1]"))
        print("rows - ",rows)
        print("columns - ",columns)

    def tearDown(self):
        # close the browser window
        self.driver.quit()
        
'''for row in range(1,3):
            for col in range(1,3):
                values = self.driver.find_element_by_xpath(".//*[@id='table01']/tbody/tr["+row+"]/td["+col+"]").text
                
               # .//*[@id='table01']/tbody/tr[1]/td[2]
                print(values)
                
                 data=[]
        for row in self.driver.find_elements_by_xpath(".//*[@id='table01']/tbody/tr"):
            tds=row.find_elements_by_tag_name('td')
            if tds: 
                data= [td.text for td in tds]
        print(data)
                
                
                
                '''


if __name__ == '__main__':
    unittest.main(verbosity=2)
