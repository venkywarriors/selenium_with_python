from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,
                                           "(//div[@class='datepicker-cal-month'])[1]//button[text()='30']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

ff = CalendarSelection()
ff.test1()