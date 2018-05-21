from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

ff = ByDemo()
ff.test()