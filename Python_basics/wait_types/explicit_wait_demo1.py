from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys



class ExplicitWaitDemo1():

    def test(self):
        baseUrl = "http://www.expedia.com"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.XPATH, ".//*[@id='flight-destination-hp-flight']").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2018")
        returnDate = driver.find_element(By.XPATH, "//input[@id='flight-returning-hp-flight']")
        returnDate.clear()
        returnDate.send_keys("12/26/2018")
        returnDate.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//select[@name='sort']")))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo1()
ff.test()