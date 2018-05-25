'''
Created on May 23, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
import time
import os

#   --- best example program for driver.close() and driver.quit()

class SwitchToNewTab():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()
        driver.get(baseUrl)

        time.sleep(2)
        driver.execute_script("window.open('https://google.co.in','new window')")
        print("opened a new tab1")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(3)
        print("opened a new tab2")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[2])
        driver.get("http://stackoverflow.com")
        time.sleep(3)
        print("opened a new tab3")
        # close the active tab
        driver.close()
            
ff = SwitchToNewTab()
ff.test1()
