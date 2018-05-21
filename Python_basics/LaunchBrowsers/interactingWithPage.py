import os
from selenium import webdriver

chrome_driver_path = os.path.dirname(__file__)  + "\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)


driver.get('http://codepad.org')
 
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.")


text = driver.find_element_by_xpath("//*[@id='editor-form']/table/tbody/tr[1]/td/span").text
print(text)

print (driver.current_url)



driver.close()
#driver.forward()
#driver.back()
#driver.minimize_window()
#driver.maximize_window()
#driver.refresh()
#driver.set_page_load_timeout(20)#seconds
#driver.delete_all_cookies()
