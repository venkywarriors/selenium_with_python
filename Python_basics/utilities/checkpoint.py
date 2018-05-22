"""
@package utilities

CheckPoint class implementation

It provides functionality to assert the result
and take screenshot on failure of a test case

This class is initialized in guibasetestcase class
This should only be used in the test case class and not in the page class

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import traceback
import unittest
from utilities.util import Util
import utilities.custom_logger as cl

class CheckPoint(unittest.TestCase):

    def __init__(self):
        """
        Inits CheckPoint class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        super(CheckPoint, self).__init__()
        self.statusMap = {}
        self.util = Util()
        self.log = cl.customLogger()

    def setStatus(self, key, value):
        """
        Set status of the map which keeps track of the verification points

        Required Parameters:
            key: <Test Name>.<Result Message>
            value: Test Result (Pass / Fail)

        Optional Parameters:
            None

        Returns:
            None
        """
        self.statusMap[key] = value

    def clearStatus(self):
        """
        Clear status of the map which keeps track of the verification points

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.statusMap.clear()
        self.log.info("Clear result status of previous test")

    def mark(self, testName, result, resultMessage):
        """
        Mark the result of the verification point in a test case

        Required Parameters:
            testName: Name of the test case
            result: Result of the test case (Boolean)
            resultMessage: Result message that needs to be logged

        Optional Parameters:
            None

        Returns:
            None
        """
        testName = testName.lower()
        mapKey = testName + "." + resultMessage
        try:
            if result:
                self.setStatus(mapKey, "PASS")
                self.log.info("Verification successful :: " + resultMessage)
            else:
                self.setStatus(mapKey, "FAIL")
                self.util.screenShot("FAIL" + mapKey)
                self.log.info("Verification failed :: " + resultMessage)
        except:
            self.log.info("### Exception Occurred !!!")
            self.setStatus(mapKey, "FAIL")
            traceback.print_stack()

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final checkPoint of the test case

        Required Parameters:
            testName: Name of the test case
            result: Result of the test case (Boolean)
            resultMessage: Result message that needs to be logged

        Optional Parameters:
            None

        Returns:
            None
        """
        testName = testName.lower()
        mapKey = testName + "." + resultMessage
        try:
            if result is not None:
                if result:
                    self.setStatus(mapKey, "PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.setStatus(mapKey, "FAIL")
                    self.util.screenShot("FAIL" + mapKey)
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)
            else:
                self.setStatus(mapKey, "FAIL")
                self.log.error("### Exception Occurred, Result is None !!!")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                self.log.error("Result value :: " + str(result))
        except:
            self.setStatus(mapKey, "FAIL")
            self.log.error("### Exception Occurred !!!")
            self.util.screenShot("FAIL" + mapKey)
            traceback.print_stack()

        resultList = []
        for key in self.statusMap:
            resultList.append(self.statusMap[key])
            self.log.info(self.statusMap[key] + " :: " + key)

        if "FAIL" in resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.assertTrue(False)
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.assertTrue(True)