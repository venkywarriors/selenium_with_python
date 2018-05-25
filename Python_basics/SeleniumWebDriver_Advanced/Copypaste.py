'''
Created on May 24, 2018

@author: venkateshwara.d
'''
import sys
import subprocess
import pyperclip
import clipboard
import ctypes

#pip install pyperclip

'''
pyperclip.copy('Hello world!')
string = pyperclip.paste()
print(string)
'''
# pip install clipboard

'''
clipboard.copy("abc")  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboard
print(text)
'''
def winGetClipboard():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(13) # CF_UNICODETEXT
    data = ctypes.c_wchar_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()
    return data
    
print (winGetClipboard())
