"""
@package base

Base Page class implementation

It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class PageClassName(BasePage)
"""
from abc import abstractmethod
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Required Parameters:
            driver: WebDriver Object

        Optional Parameters:
            None

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self._validate_page(driver)
        self.driver = driver
        self.util = Util()
        self.bkend = BEConnection()

    def verifyFlashMessage(self, textToVerify, timeout=6):
        """
        Validate the flash message after completing an action

        Required Parameters:
            textToVerify: Text on the flash message that needs to be verified

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        try:
            flashMessageElement = self.waitForElement(locator=".nmbl-flash-message-content", locatorType="css",
                                                      info="flash message", timeout=timeout)
            if flashMessageElement is not None:
                elementText = self.getText(flashMessageElement,
                                           "Getting text on flash message")
                # elementText = self.getText(self.getElementByClassName("flash-message"),
                #                            "Getting text on flash message")
                result = self.util.verifyTextContains(elementText, textToVerify)
                # flashMessageClose = self.getElementByClassName("flash-message-close")
                flashMessageClose = self.getElementByCss(".nmbl-flash-message-close")
                self.clickElement(flashMessageClose, "Flash message 'X' close button", 1)
                return result
            else:
                # If element does not show up before timeout, return False
                return False
        except:
            self.log.error("Failed to get text on flash message")
            print_stack()
            return False

    def verifyModalMessage(self, textToVerify, textLocator, buttonToClickLocator, buttonInfo=""):
        """
        Validate the message on the modal and click Ok/Close button to close the modal

        Required Parameters:
            textToVerify: Text on the modal that needs to be verified
            textLocator: Locator of the message
            buttonToClickLocator: Locator of the button to click on modal

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        try:
            result = False
            elementPresent = self.isElementPresent(textLocator)
            if elementPresent:
                elementText = self.getText(self.getElement(textLocator), "Getting text on modal")
                result = self.util.verifyTextContains(elementText, textToVerify)
            if not result:
                self.util.screenShot("FAIL-Modal-Message-Verification")
            self.clickElement(self.getElement(buttonToClickLocator), buttonInfo)
            return result
        except:
            self.log.error("Failed to get text on modal")
            print_stack()
            return False

    def verifyModalConfirmation(self, buttonLocator, info, locatorType="id"):
        """
        Verify the confirmation modal is present and click the 'Confirmation' button
        'Confirmation' button can be OK/Close/Delete

        Required Parameters:
            buttonLocator: Locator of the button on confirmation modal
            info: Information about the button, usually text on the button

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, className, linkText)

        Returns:
            Boolean
        """
        try:
            elementPresent = self.isElementPresent(buttonLocator, locatorType)
            if elementPresent:
                return self.clickElement(self.getElement(buttonLocator), info)
            return False
        except:
            self.log.error("Failed to find button on confirmation modal")
            print_stack()
            return False

    def verifyFieldErrorMessage(self, locator, textToVerify, locatorType="id"):
        """
        Validate the flash message after completing an action

        Required Parameters:
            locator: Locator of the error message
            textToVerify: Text on the flash message that needs to be verified

        Optional Parameters:
            locatorType: Type of the locator, default is 'id'

        Returns:
            Boolean
        """
        try:
            elementPresent = self.isElementPresent(locator, locatorType)
            if elementPresent:
                elementText = self.getText(self.getElement(locator),
                                       "Getting text on field error message")
                result = self.util.verifyTextContains(elementText, textToVerify)
                return result
            return False
        except:
            self.log.error("Failed to get text on field error message")
            print_stack()
            return False

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Required Parameters:
            titleToVerify: Title on the page that needs to be verified

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        try:
            actualTitle = self.getBrowserTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    @abstractmethod
    def _validate_page(self, driver):
        pass

    """ Regions define functionality available through all page objects """
    # @property
    # def search(self):
    #     from search import SearchRegion
    #     return SearchRegion(self.driver)

class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
