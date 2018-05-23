'''
Created on May 22, 2018

@author: venkateshwara.d
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("http://demo.guru99.com/test/upload/")
driver.implicitly_wait(5)
        
        # enter the file path onto the file-selection input field
uploadElement  = driver.find_element(By.ID, "uploadfile_0")

time.sleep(10)

uploadElement.send_keys("D:\\webtable.JPG")

time.sleep(2)
driver.find_element(By.ID, "terms").click()
        # click the "UploadFile" button
driver.find_element(By.NAME, "send").click()

driver.quit()