'''
Created on May 22, 2018

@author: venkateshwara.d
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
import pyperclip

class UploadingFIle():

    def test(self):
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()
        #driver.get("http://demo.guru99.com/test/upload/")
        driver.implicitly_wait(5)
        
        # enter the file path onto the file-selection input field
        uploadElement  = driver.find_element(By.ID, "uploadfile_0")
        uploadElement.click()
        time.sleep(10)
        filename = os.path.dirname(__file__)  + "\\128 Interview-Questions.pdf"
        print(filename)
        uploadElement.send_keys(filename)
        

        pyperclip.copy('This is copied to the clipboard.')
 
        pyperclip.paste()
        # check the "I accept the terms of service" check box
        time.sleep(2)
        driver.find_element(By.ID, "terms").click()
        # click the "UploadFile" button
        driver.find_element(By.NAME, "send").click()



ff = UploadingFIle()
ff.test()