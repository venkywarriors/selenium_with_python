'''
Created on May 24, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplicitWaitType
import time
import os
from selenium.webdriver.common.keys import Keys

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab").click()
        driver.find_element(By.ID, "flight-origin").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing").send_keys("12/24/2016")
        returnDate = driver.find_element(By.ID, "flight-returning")
        returnDate.clear()
        returnDate.send_keys("12/26/2016")
        returnDate.send_keys(Keys.RETURN)

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()
