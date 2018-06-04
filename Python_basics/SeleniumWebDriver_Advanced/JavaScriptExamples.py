'''
Created on May 23, 2018

@author: venkateshwara.d
'''
from selenium import webdriver
from time import sleep
import unittest
import datetime
import os

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.abspath('..')  + "\\Drivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        print("------------------------------------------------------------------")
        print("Test Environment Created")
        print("Run Started at :" + str(datetime.datetime.now()))

    def test_NavigateMercury(self):

        print("Navigating to URL")
        self.driver.execute_script("window.location = 'https://www.makemytrip.com'")
        self.driver.maximize_window()
        sleep(2)
        # Refreshing the page using javaScript
        print("Refreshing the page")
        self.driver.execute_script("history.go(0)")
        sleep(2)
        # Page title using javaScript
        print("Page title is :"+self.driver.execute_script("return document.title;"))

        search = self.driver.execute_script("return document.getElementById('searchBtn');")
        print("Search button class :"+search.get_attribute("class"))
        sleep(2)

        print("Scrolling down to coordinates (300,2000)")
        self.driver.execute_script("window.scrollBy(300,2000)")
        sleep(2)

        print("Scrolling down to a element")
        ele = self.driver.find_element_by_xpath("//*[contains(text(),'Follow us')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        print("Scrolled successfully to :"+ele.text)
        sleep(2)
        # Highlighted elements using javaScript
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele, "background:yellow; color: Red; border: 4px dotted solid yellow;")
        print("Highlighted elements :"+ele.text)
        sleep(2)
        # click using javaScript
        twt = self.driver.find_element_by_xpath("//*[contains(text(),'Twitter')]")
        self.driver.execute_script("arguments[0].click();",twt)
        print("Clicked in Twitter link")
        sleep(2)

    def tearDown(self):
        if (self.driver!= None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
