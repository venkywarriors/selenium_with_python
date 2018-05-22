from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

class Sliders():

    def test1(self):
        baseUrl = "https://jqueryui.com/slider/"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")

ff = Sliders()
ff.test1()