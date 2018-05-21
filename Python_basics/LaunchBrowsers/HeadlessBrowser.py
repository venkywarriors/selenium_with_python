'''
Created on May 21, 2018

@author: venkateshwara.d
'''
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory


# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")

driver.close()


 

