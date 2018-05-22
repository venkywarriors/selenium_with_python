"""
@package utilities

DriverSession class implementation

It provides the  WebDriver Session to the desired class
No object creation is needed as the methods are static

@author Anil Tomar <anil.tomar@nimblestorage.com>
@version 1.0
@copyright Nimble Storage, Inc

Example:
    from utilities.driver_session import DriverSession as DS
    DS.getDriver().<desired driver method>
"""
class DriverSession():

    driver = None

    @staticmethod
    def setDriver(driver):
        """
        Set the WebDriver object

        Required Parameters:
            driver: WebDriver object to set

        Optional Parameters:
            None

        Returns:
            None
        """
        DriverSession.driver = driver

    @staticmethod
    def getDriver():
        """
        Get the WebDriver object

        Required Parameters:
           None

        Optional Parameters:
            None

        Returns:
            'WebDriver Object'
        """
        return DriverSession.driver
