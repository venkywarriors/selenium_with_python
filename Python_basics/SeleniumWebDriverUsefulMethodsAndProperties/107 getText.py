from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers
import time


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(1)
        driver.quit()


ff = GetText()
ff.test()