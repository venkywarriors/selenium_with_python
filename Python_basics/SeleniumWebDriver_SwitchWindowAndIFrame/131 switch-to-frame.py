from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using Id

        # Switch to frame using name

        # Switch to frame using numbers

        # Search course

        # Switch back to the parent frame
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")


ff = SwitchToFrame()
ff.test()
