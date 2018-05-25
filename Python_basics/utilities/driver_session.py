'''
Created on May 30, 2018
@author: venkateshwara.d
'''
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
