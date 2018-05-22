from selenium import webdriver
import os

class RunChromeTestsWindows():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        driverLocation = "C:\\Users\\Anil Tomar\\PycharmProjects\\libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTestsWindows()
chromeTest.test()