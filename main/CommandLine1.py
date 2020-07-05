'''
Created on 05-Jul-2020

@author: venkateshwara D
'''
import sys
import unittest

class MyTest(unittest.TestCase):
    USERNAME = "jemima"
    PASSWORD = "password"

    def test_logins_or_something(self):
        print('username : {}'.format(self.USERNAME))
        print('password : {}'.format(self.PASSWORD))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        MyTest.USERNAME = sys.argv.pop()
        MyTest.PASSWORD = sys.argv.pop()
    unittest.main()
    
''' 

In CMD

cd full path to python
python CommandLine1.py ausername apassword
username : apassword
password : ausername
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK

'''    