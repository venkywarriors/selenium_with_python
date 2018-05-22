"""
@package base

GUIBaseTestCase class implementation

This class consists of all the initialization, setup and teardown functionality

This class is inherited by all the test classes
It should not be used by creating an object instance

Example:
    class ClassName(GUIBaseTestCase)
"""
from base.webdriverfactory import WebDriverFactory
import time
import utilities.custom_logger as cl
import unittest
from utilities.checkpoint import CheckPoint
from utilities.util import Util
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    driver = None
    startTime = int(round(time.time() * 1000))
    testStartTime = int(round(time.time() * 1000))
    log = cl.customLogger()
    util = Util()
    checkPoint = CheckPoint()


    @classmethod
    def setUpClass(cls):
        """
        SetUp to initialize webdriver session, pages and other needed objects

        Returns:
            None
        """
        # Get webdriver instance
        # browser should be read from the arguments
        if browser == "iexplorer":
            cls.driver = webdriver.Ie()
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        elif browser == "chrome":
            cls.driver = webdriver.Chrome()
        else:
            cls.driver = webdriver.PhantomJS()

        # Similarly I want to get operating system also from command line

        cls.startTime = int(round(time.time() * 1000))


    def refresh(self):
        """
        Refresh current page on the web application

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.driver.refresh()
        self.log.info("The current browser location was refreshed")

    def initializePages(self):
        """
        Initialize pages

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        pass

    def setUp(self):
        """
        This method executes before every method in the test class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.testStartTime = int(round(time.time() * 1000))
        self.checkPoint.clearStatus()
        self.log.info("***"*30)
        self.log.info("Test Started --> :: " + self._testMethodName)
        self.log.info("***"*30)

    def tearDown(self, refresh=True):
        """
        This method executes after every method in the test class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.log.info("***"*30)
        self.log.info("Test Ended --> :: " + self._testMethodName)
        testEndTime = int(round(time.time() * 1000))
        testDuration = (testEndTime - self.testStartTime) / 1000.00
        self.log.info("Time taken to execute test method :: " + "{0:.2f}".format(testDuration) + " :: seconds")
        self.log.info("***"*30)
        # self.checkPoint.clearStatus()
        if refresh:
            self.refresh()
            self.log.info("Page reload after the test case")


    @classmethod
    def tearDownClass(self):
        """
        TearDown to clean up anything that is need to cleaned up after the test class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        endTime = int(round(time.time() * 1000))
        duration = (endTime - self.startTime) / 1000.00
        timeUnit = "seconds"
        if duration > 60.00:
            duration = duration / 60.0
            timeUnit = "minutes"
        # close the browser window
        self.driver.quit()
        self.log.info("Driver quit, session closed")
        self.log.info("***" * 30)
        self.log.info("Total Time taken to execute test suite :: " + "{0:.2f}".format(duration) + " :: " + timeUnit)
        self.log.info("***" * 30)
