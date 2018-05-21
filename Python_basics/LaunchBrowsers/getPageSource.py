'''
Created on May 21, 2018

@author: venkateshwara.d
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
        self.driver=webdriver.Chrome(chrome_driver_path)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()