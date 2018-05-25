'''
Created on May 23, 2018

@author: venkateshwara.d
'''
from selenium import webdriver
import re
import os

chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("http://www.airindia.in/contact-details.htm")
driver.implicitly_wait(3)

doc = driver.page_source

emails = [email.text for email in driver.find_elements_by_class_name('linkText') if "@" in email.text]
'''emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
list_new = []
for email in emails:
    list_new.append(str(email))
    print(email)'''

driver.quit()

print(emails)
