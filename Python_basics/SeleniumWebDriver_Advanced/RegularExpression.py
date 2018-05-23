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

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
list_new = []
for email in emails:
    list_new.extend(str(email))
    print(email)


driver.quit()

print(list_new)

'''
console output :
call.del@airindia.in
call.del@airindia.in
flyingreturnsbase.ai@iclployalty.com

['c', 'a', 'l', 'l', '.', 'd', 'e', 'l', '@', 'a', 'i', 'r', 'i', 'n', 'd', 'i', 'a', '.', 'i', 'n', 'c', 
'a', 'l', 'l', '.', 'd', 'e', 'l', '@', 'a', 'i', 'r', 'i', 'n', 'd', 'i', 'a', '.', 'i', 'n', 'c
 'i', 'n', 'd', 'i', 'a', '.', 'i', 'n', 'c', 'a', 'l', 'l', '.', 'b', 'o', 'm', '@', 'a', 'i', 'r', 'i', 'n', 'd', 'i']
 
My Excepted output :

['call.del@airindia.in','call.del@airindia.in','flyingreturnsbase.ai@iclployalty.com']


'''
