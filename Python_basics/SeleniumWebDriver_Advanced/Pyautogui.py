'''
Created on May 24, 2018

@author: venkateshwara.d
'''
# pip install PyAutoGUI
import pyautogui
from selenium import webdriver
import time
import os


'''chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
driver=webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get("http://demo.guru99.com/test/upload/")
driver.implicitly_wait(5)
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')'''

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print("screenWidth - {0},screenHeight - {1}".format(screenWidth, screenHeight))
print("currentMouseX - {0},currentMouseY - {1}".format(currentMouseX, currentMouseY))

pyautogui.keyDown('win')
pyautogui.keyDown('m')

pyautogui.keyUp('m')
pyautogui.keyUp('win')

'''pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
'''

# Mouse operation https://pyautogui.readthedocs.io/en/latest/mouse.html
# keyboard operation https://pyautogui.readthedocs.io/en/latest/keyboard.html


