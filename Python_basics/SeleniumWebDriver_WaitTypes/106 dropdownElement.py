from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.select import Select

class AirbnbExercise1():

    def test(self):
        baseUrl = "https://www.airbnb.com/"
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Elements and design has changed on Airbnb website after the lecture was made
        searchBox = driver.find_element(By.NAME, "location")
        searchBox.send_keys("Hawaii")

        when = driver.find_element(By.XPATH,
                                   "(//button//span[text()='Anytime'])[2]")
        when.click()
        time.sleep(2)

        checkin = driver.find_element(By.XPATH,
                                      "(//div[contains(@class,'CalendarMonth') and @data-visible='true']//div[text()='30']//parent::button)[1]")
        checkin.click()

        checkout = driver.find_element(By.XPATH,
                                      "(//div[contains(@class,'CalendarMonth') and @data-visible='true']//div[text()='30']//parent::button)[2]")
        checkout.click()

        showInstant = driver.find_elements(By.XPATH, "//span[text()='Show Instant Book Listings']")
        if len(showInstant) > 0:
            showInstant[0].click()

        dropdownElement = driver.find_element(By.XPATH,
                                              "(//span[text()='1 guest'])[2]")
        #sel = Select(dropdownElement)
        #sel.select_by_visible_text("2 Guests")
        # It is updated to <button> tag
        # We can only use Select Class with <select> tag
        dropdownElement.click()
        adultPlusButton = driver.find_element(By.XPATH,
                                              "(//button[@aria-controls='StepIncrementerRow-value-GuestCountFilter-via-SearchBarLarge-adults'])[2]")
        adultPlusButton.click()
        # You might have issues because of slow connection that you might not even notice
        # Try to run files multiple times

        # Search button does not exist on the next page, so we can comment it
        # time.sleep(2)
        # This element has changed on Airbnb website after the lecture was made
        # searchButton = driver.find_element(By.XPATH,
        #                                    "//button//span[text()='Search']")
        # searchButton.click()

ff = AirbnbExercise1()
ff.test()