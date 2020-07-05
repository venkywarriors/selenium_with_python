'''
Created on 05-Jul-2020

@author: venkateshwara D
'''
import unittest
import sys

class MyTest(unittest.TestCase):
    def setUp(self):
        self.a = sys.argv[1]
    def runTest(self):
        self.assertEqual(self.a, "1")

unittest.TextTestRunner().run(MyTest())

''' 

In CMD

cd full path to python
python CommandLine.py 2
======================================================================
FAIL: runTest (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "CommandLine.py", line 13, in runTest
    self.assertEqual(self.a, "1")
AssertionError: '2' != '1'
- 2
+ 1

python CommandLine.py 1
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

'''