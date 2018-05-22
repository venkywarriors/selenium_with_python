"""
@package base

Selenium Driver class implementation

This uses the driver instance and wraps all the selenium provided actions in methods with proper logging.
It acts as a central location to all the selenium actions.

This class needs to be inherited by the base page class
and any other class like table class
This should not be directly inherited in page classes

Example:
    Class BasePage(SeleniumDriver)
"""
import time
import traceback
from base.configreader import ConfigReader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as e
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

from selenium.webdriver.support.select import Select
from utilities.util import Util

import utilities.custom_logger as cl
import logging


class SeleniumDriver(object):

    def __init__(self, driver):
        """
        Inits Selenium Driver class with driver

        Required Parameters:
            driver: webdriver instance

        Optional Parameters:
            None

        Returns:
            A SeleniumDriver object

        Examples:
            super(ClassName, self).__init__(driver)
            super().__init__(driver)
        """
        self.driver = driver
        # Delete these two if they have no effect after a run
        # self.cfg = ConfigReader()
        # self.cfg.configRead()
        self.log = cl.customLogger(logging.INFO)
        self.util = Util()

    def getDriver(self):
        """
        Get the webdriver instance

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            webdriver instance
        """
        driver = self.driver
        return driver

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

    def getBrowserTitle(self):
        """
        Get title of current page on the web application

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            Title of the current page
        """
        title = self.driver.title
        self.log.info("Title of the current page is :: " + title)
        return title

    def getBrowserURL(self):
        """
        Get URL of current page on the web application

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            Current page URL
        """
        browserURL = self.driver.current_url
        self.log.info("Current browser url is :: " + browserURL)
        return browserURL

    def navigateBrowserBack(self):
        """
        Go one page back

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.driver.back()

    def navigateBrowserForward(self):
        """
        Go one page forward

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.driver.forward()

    def clickElement(self, element, info, timeToWait=0):
        """
        Click Element

        Required Parameters:
            element: Element to click
            info: Information about the element, usually text on the element

        Optional Parameters:
            timeToWait: Time you want to wait after clicking the element

        Returns:
            boolean
        """
        if element is not None:
            try:
                element.click()
                self.log.info("clicked on element :: " + info)
                self.log.info("Waiting after clicking the element for "
                              + str(timeToWait) + " seconds")
                time.sleep(timeToWait)
                return True
            except:
                self.log.error("Failed to click element :: " +  info)
                traceback.print_stack()
                return False
        else:
            self.log.error("Element :: " + info +  " reference to none")
            return False

    def clickWhenReady(self, locator, locatorType="id", info="", timeout=10, pollFrequency=0.5, timeToWait=0):
        """
        Click Element when it's clickable

        Required Parameters:
            locator: locator of the element to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
            info: Information about the element, usually text on the element
            timeout: Maximum time you want to wait for the element
            pollFrequency: Frequency to poll for the element
            timeToWait: Time you want to wait after clicking the element

        Returns:
            boolean
        """
        element = self.waitForElement(locator, locatorType=locatorType, waitType="clickable",
                                      timeout=timeout, pollFrequency=pollFrequency)
        self.clickElement(element, info, timeToWait=timeToWait)

    def doubleClick(self, element, info):
        """
        Double Click Element

        Required Parameters:
            element: Element to double click
            info: Information about the element, usually text on the element

        Optional Parameters:
            None

        Returns:
            None
        """
        try:
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            self.log.info("Double clicked on element :: " + info)
        except:
            self.log.error("Double click failed on element :: " +  info)
            traceback.print_stack()

    def rightClick(self, element, itemLocator, info):
        """
        Right Click Element

        Required Parameters:
            element: Element to right click
            itemLocator: Locator of item that needs to be clicked after right click
            info: Information about the element, usually text on the element

        Optional Parameters:
            None

        Returns:
            None
        """
        try:
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            self.log.info("Right clicked on element :: " +  info)
            element_to_click = self.driver.find_element_by_xpath(itemLocator)
            self.clickElement(element_to_click, "Selected Item")
        except:
            self.log.error("Right clicked failed on element :: " +  info)
            traceback.print_stack()

    def sendKeys(self, element, data, info, clear=True, timeToWait=0):
        """
        Send keys to element (Usually to text field)

        Required Parameters:
            element: Element to send keys
            data: Data (text) that needs to be sent
            info: Information about the element, text on the element

        Optional Parameters:
            clear: Provide False if you don't want to clear the text field before sending data
            timeToWait: Time you want to wait after sending data to the element

        Returns:
            boolean
        """
        if element is not None:
            try:
                if clear is True:
                    element.clear()
                element.send_keys(data)
                self.log.info("Send keys --> :: '" + data + "' on element :: " +  info)
                self.log.info("Waiting after sending data to the element for "
                              + str(timeToWait) + " seconds")
                time.sleep(timeToWait)
                return True
            except:
                self.log.error("Failed to send keys --> :: '" + data + "' on element :: " +  info)
                traceback.print_stack()
                return False
        else:
            self.log.error("Element :: " + info +  " reference to none")
            return False

    def keyPress(self, key, info):
        """
        Press a key on the keyboard

        Required Parameters:
            key: Key that needs to be pressed
            info: Information about the key, key name

        Optional Parameters:
            None

        Returns:
            None
        """
        try:
            actions = ActionChains(self.driver)
            actions.key_down(key).perform()
            self.log.info("Keypress " + info)
        except:
            self.log.error("Keypress Failed " + info)
            traceback.print_stack()


    def getText(self, element, info):
        """
        Get 'Text' on an element

        Required Parameters:
            element: Element Object
            info: Information about the element, text on the element

        Optional Parameters:
            None

        Returns:
            Text of element
        """
        if element is not None:
            try:
                text = element.text
                if len(text) == 0:
                    text = element.get_attribute("innerHTML")
                if len(text) != 0:
                    self.log.info("Getting text on element :: " +  info)
                    self.log.info("The text is :: '" + text + "'")
            except:
                text = None
                self.log.error("Failed to get text on element " + info)
                traceback.print_stack()
        else:
            return None
        return text.strip()

    def getValue(self, element, info):
        """
        Get 'Value' of an element, a text field

        Required Parameters:
            element: Element Object
            info: Information about the element, label/name of the element

        Optional Parameters:
            None

        Returns:
            Text of element
        """
        if element is not None:
            try:
                value = element.get_attribute("value")
                if len(value) is not 0:
                    self.log.info("Getting value of element :: " +  info)
                    self.log.info("The value is :: '" + value + "'")
            except:
                value = None
                self.log.error("Failed to get value of element " + info)
                traceback.print_stack()
        else:
            return None
        return value

    def isElementPresent(self, locator, locatorType="id"):
        """
        Check if element is present

        Required Parameters:
            locator: Locator of the element to check

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, className, linkText)

        Returns:
            Boolean
        """
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                self.driver.find_element_by_id(locator)
            elif locatorType == "xpath":
                self.driver.find_element_by_xpath(locator)
            elif locatorType == "css":
                self.driver.find_element_by_css_selector(locator)
            elif locatorType == "classname":
                self.driver.find_element_by_class_name(locator)
            elif locatorType == "linktext":
                self.driver.find_element_by_link_text(locator)
            else:
                self.log.warning("Locator type " + locatorType + " not correct/supported")
                return False
            self.log.info("Element " + locator + " successfully appeared on page")
            return True
        except e.NoSuchElementException:
            self.log.warning("Element " + locator + " not appeared on page")
            return False

    def isEnabled(self, element, info):
        """
        Check if element is enabled

        Required Parameters:
            element: Element to verify if it's enabled
            info: Information about the element, usually text on the element

        Optional Parameters:
            None

        Returns:
            boolean
        """
        enabled = False
        if element is not None:
            try:
                enabled = element.is_enabled()
                if enabled:
                    self.log.info("Element :: '" + info + "' is enabled")
                else:
                    self.log.info("Element :: '" + info + "' is not enabled")
            except:
                self.log.error("Element :: '" + info + "' state could not be found")
                traceback.print_stack()
        return enabled

    def isDisplayed(self, element=None, info="", locator="", locatorType="id"):
        """
        Check if element is displayed

        Required Parameters:
            None

        Optional Parameters:
            element: Element to verify if it's displayed
            info: Information about the element, usually text on the element
            locator: Locator of the element to check
            locatorType: Type of the locator(id(default), xpath, css, className, linkText)

        Returns:
            boolean
        """
        if locator:
            element = self.getElement(locator, locatorType=locatorType)
        displayed = False
        if element is not None:
            try:
                displayed = element.is_displayed()
                if displayed:
                    self.log.info("Element :: '" + info + "' is displayed")
                else:
                    self.log.info("Element :: '" + info + "' is not displayed")
            except:
                self.log.warning("Element :: '" + info + "' state could not be found")
                traceback.print_stack()
        return displayed

    def isSelected(self, element, info):
        """
        Check if element is selected, element could be checkbox or radio button

        Required Parameters:
            element: Element to verify if it's selected
            info: Information about the element, usually text on the element

        Optional Parameters:
            None

        Returns:
            boolean
        """
        selected = False
        if element is not None:
            try:
                selected = element.is_selected()
                if selected:
                    self.log.info("Element :: '" + info + "' is selected")
                else:
                    self.log.info("Element :: '" + info + "' is not selected")
            except:
                self.log.error("Element :: '" + info + "' state could not be found")
                traceback.print_stack()
        return selected

    def getSelectedValue(self, element, info):
        """
        Get Selected value from a Select dropdown list

        Required Parameters:
            element: Select dropdown element
            info: Information about the element, text on the element

        Optional Parameters:
            None

        Returns:
            Selected value from dropdown
        """
        try:
            select = Select(element)
            option = select.first_selected_option
            self.log.info("Option found in dropdown:: '" + info + "'")
            self.log.info("Selected value of the dropdown is: " + str(option.text))
            return option.text
        except:
            self.log.error("Could not find option from dropdown:: '" + info + "'")
            traceback.print_stack()
            return False

    def isDropdownValueSelected(self, dropdownElement, optionToCheck, info=""):
        """
        Check if the option is selected from dropdown list

        Required Parameters:
            dropdownElement: Select dropdown element
            optionToCheck: Option to check
            info: Information about the element, text on the element

        Optional Parameters:
            None

        Returns:
            boolean
        """
        try:
            self.log.info("Option to check from dropdown:: '" + optionToCheck + "'")
            selectedOption = self.getSelectedValue(dropdownElement, info)
            return (optionToCheck == str(selectedOption))
        except:
            self.log.error("Could not find option from dropdown:: '" + info + "'")
            traceback.print_stack()
            return False

    def check(self, element, info, timeToWait=0):
        """
        Select Checkbox

        Required Parameters:
            element: Element to check
            info: Information about the element, usually text on the element

        Optional Parameters:
            timeToWait: Time you want to wait after checking the element

        Returns:
            None
        """
        if self.isSelected(element, info) is False:
            self.clickElement(element, info)
            self.log.info("Element :: '" + info + "' is checked")
            self.log.info("Waiting after checking the element for "
                          + str(timeToWait) + " seconds")
            time.sleep(timeToWait)
        else:
            self.log.info("Element :: '" + info + "' was already checked")

    def unCheck(self, element, info, timeToWait=0):
        """
        Deselect Checkbox

        Required Parameters:
            element: Element to uncheck
            info: Information about the element, usually text on the element

        Optional Parameters:
            timeToWait: Time you want to wait after un-checking the element

        Returns:
            None
        """
        if self.isSelected(element, info):
            self.clickElement(element, info)
            self.log.info("Element :: '" + info + "' is unchecked")
            self.log.info("Waiting after un-checking the element for "
                          + str(timeToWait) + " seconds")
            time.sleep(timeToWait)
        else:
            self.log.info("Element :: '" + info + "' was already unchecked")

    def selectDropdown(self, dropDownElement, optionToSelect, info,
                       byValue=False, byIndex=False, timeToWait=0):
        """
        Select option from a dropdown (default by visible text)

        Required Parameters:
            dropDownElement: Dropdown element
            optionToSelect: Option to select from the dropdown (Visible Text / Value / Index)
            info: Information about the optionToSelect, usually text on the optionToSelect

        Optional Parameters:
            byValue: Provide True if you want to select by value
            byIndex: Provide True if you want to select by index
            timeToWait: Time you want to wait after selecting the element

        Returns:
            None
        """
        try:
            select = Select(dropDownElement)

            if byValue:
                select.select_by_value(optionToSelect)
            elif byIndex:
                select.select_by_index(optionToSelect)
            else:
                select.select_by_visible_text(optionToSelect)
            self.log.info("Selected option --> :: '" + optionToSelect + "' from dropdown:: '" + info + "'")
            self.log.info("Waiting after selecting the element for " + str(timeToWait) + " seconds")
            time.sleep(timeToWait)
            return True
        except:
            self.log.error("Could not select option --> :: '" + optionToSelect + "' from dropdown:: '" + info + "'")
            traceback.print_stack()
            return False

    def getDropdownOptions(self, dropDownElement, info):
        """
        Get all options from a dropdown

        Required Parameters:
            dropDownElement: Dropdown element
            info: Information about the dropdown element

        Optional Parameters:
            None

        Returns:
            List of options
        """
        try:
            select = Select(dropDownElement)
            options = select.options
            self.log.info("Options found from dropdown:: '" + info + "'")
            self.log.info("These are the options: " + str(options))
            return options
        except:
            self.log.error("Could not find all options from dropdown:: '" + info + "'")
            traceback.print_stack()

    def getDropdownOptionsTextList(self, dropDownElement, info):
        """
        Get list of visible text of all options from a dropdown

        Required Parameters:
            dropDownElement: Dropdown element
            info: Information about the dropdown element

        Optional Parameters:
            None

        Returns:
            List of visible text of options
        """
        options = self.getDropdownOptions(dropDownElement, info)
        try:
            textList = []
            for option in options:
                textList.append(self.getText(option, "Option Text"))
            self.log.info("Options list from dropdown:: '" + info + "' is: " + str(textList))
            return textList
        except:
            self.log.error("Could not find options text list from dropdown:: '" + info + "'")
            traceback.print_stack()

    def switchToWindow(self, info):
        """
        Switch to Window

        Required Parameters:
            info: Information about the window

        Optional Parameters:
            None

        Returns:
            None
        """
        try:
            currentHandle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle not in currentHandle:
                    switchHandle = handle
                    self.driver.switch_to_window(handle)
                    self.log.info("Switched to window:: '" + info + "'")
                    return switchHandle
        except:
            self.log.error("Could not find window handles to switch:: '" + info + "'")
            traceback.print_stack()
            return False

    def closeCurrentWindow(self, info, handleToClose):
        """
        Close the current window.

        Required Parameters:
            info: Information about the window

        Optional Parameters:
            None

        Returns:
            None
        """
        try:
            handles = self.driver.window_handles
            for handle in handles:
                if handle not in self.driver.current_window_handle:
                    mainHandle = handle
                if handle in handleToClose:
                    self.driver.close()
            self.log.info("Closed current window:: '" + info + "'")
            self.driver.switch_to_window(mainHandle)
            return True
        except:
            self.log.error("Could not find window handle to close:: '" + info + "'")
            traceback.print_stack()
            return False

    def submitForm(self, element, info):
        """
        Submit Form

        Required Parameters:
            element: Element that needs to be submitted
            info: Information about the element, usually text on the element

        Optional Parameters:
            None

        Returns:
            None
        """
        if element is not None:
            try:
                element.submit()
                self.log.info("Element :: '" + info + "' is submitted")
            except:
                self.log.error("Element :: '" + info + "' is not submitted")
                traceback.print_stack()
        else:
            self.log.info("Element :: " + info +  " reference to none")

    def getElement(self, locator, locatorType="id"):
        """
        Get element for a provided locator

        Required Parameters:
            locator: locator of the element to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)

        Returns:
            Element Object
        """
        element = None
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                element = self.driver.find_element_by_id(locator)
            elif locatorType == "name":
                element = self.driver.find_element_by_name(locator)
            elif locatorType == "xpath":
                element = self.driver.find_element_by_xpath(locator)
            elif locatorType == "css":
                element = self.driver.find_element_by_css_selector(locator)
            elif locatorType == "classname":
                element = self.driver.find_element_by_class_name(locator)
            elif locatorType == "linktext":
                element = self.driver.find_element_by_link_text(locator)
            elif locatorType == "tag":
                element = self.driver.find_element_by_tag_name(locator)
            else:
                self.log.warning("Locator type " + locatorType + " not correct/supported")
            self.log.info("Element found with locator :: " + locator)
        except e.NoSuchElementException:
            self.log.error("Element not found with locator :: " + locator)
            traceback.print_stack()
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get elementList list for a provided locator

        Required Parameters:
            locator: locator of the element list to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)

        Returns:
            Element List
        """
        elementList = None
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                elementList = self.driver.find_elements_by_id(locator)
            elif locatorType == "name":
                elementList = self.driver.find_elements_by_name(locator)
            elif locatorType == "xpath":
                elementList = self.driver.find_elements_by_xpath(locator)
            elif locatorType == "css":
                elementList = self.driver.find_elements_by_css_selector(locator)
            elif locatorType == "classname":
                elementList = self.driver.find_elements_by_class_name(locator)
            elif locatorType == "linktext":
                elementList = self.driver.find_elements_by_link_text(locator)
            elif locatorType == "tag":
                elementList = self.driver.find_elements_by_tag_name(locator)
            else:
                self.log.warning("Locator type " + locatorType + " not correct/supported")
            self.log.info("Element list found with locator :: " + locator)
        except e.NoSuchElementException:
            self.log.error("Element list not found with locator :: " + locator)
            traceback.print_stack()
        return elementList

    def getElementListByAttribute(self, attributeName, attributeValue):
        """
        Get elementList list for a provided attribute name and value

        Required Parameters:
            attributeName: Name of the attribute
            attributeValue: Value of the attribute

        Optional Parameters:
            None

        Returns:
            Element List
        """
        elementList = None
        try:
            elementList = self.driver.find_elements_by_css_selector("[" + attributeName + "='" + attributeValue + "']")
        except e.NoSuchElementException:
            self.log.error("Element list not found with attribute :: " +
                           attributeName + " and value :: " + attributeValue)
            traceback.print_stack()
        return elementList

    def returnByType(self, locatorType):
        """
        Returns 'By' type of the locator provided

        Required Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)

        Optional Parameters:
            None

        Returns:
            'By' type
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.warning("Locator type " + locatorType + " not correct/supported")
            return False

    def waitForElement(self, locator, locatorType="id", info="", waitType="visible", timeout=10, pollFrequency=0.5):
        """
        Wait for element to present

        Required Parameters:
            locator: locator of the element to find

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
            timeout: Maximum time you want to wait for the element
            pollFrequency: Frequency to poll for the element

        Returns:
            Boolean
        """
        startTime = int(round(time.time() * 1000))
        element = None
        try:
            byType = self.returnByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element '" + info + "' to be visible and clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if waitType == "visible":
                element = wait.until(EC.visibility_of_element_located((byType, locator)))
            elif waitType == "clickable":
                element = wait.until(EC.element_to_be_clickable((byType, locator)))
            else:
                self.log.warning("WaitType not supported or incorrect")
            endTime = int(round(time.time() * 1000))
            duration = (endTime - startTime) / 1000.00
            self.log.info("Element '" + info +
                          "' appeared on the web page after :: " + "{0:.2f}".format(duration) + " :: seconds")
        except:
            self.log.error("Element '" + info +
                           "' not appeared on the web page after :: " + str(timeout) + " :: seconds")
        return element

    def waitForLoading(self, locator, locatorType="id", timeout=20):
        """
        Wait for loading to complete

        Required Parameters:
            locator: locator of the loading element

        Optional Parameters:
            locatorType: Type of the locator(id(default), xpath, css, classname, linktext)
            timeout: Maximum time you want to wait for the loading to complete

        Returns:
            None
        """
        startTime = int(round(time.time() * 1000))
        timeToQuit = 0
        if self.isElementPresent(locator, locatorType=locatorType):
            self.log.info("Loading mask appeared, waiting for it to disappear...")
        else:
            self.util.sleep(2, "loading mask to appear...")
        while self.isElementPresent(locator, locatorType=locatorType):
            if timeToQuit < timeout:
                self.util.sleep(1, "loading mask to disappear...")
                timeToQuit += 1
            else:
                self.log.error("Loading mask did not disappear after :: " + str(timeout) + " :: seconds")
                break
        else:
            endTime = int(round(time.time() * 1000))
            duration = (endTime - startTime) / 1000.00
            self.log.info("Loading mask disappeared in :: " + "{0:.2f}".format(duration) + " :: seconds")

    def getElementById(self, id):
        """
        Get element by id

        Required Parameters:
            id: id of the element to find

        Optional Parameters:
            None

        Returns:
            Element Object
        """
        element = None
        try:
            element = self.driver.find_element_by_id(id)
            self.log.info("Element found with id :: " + id)
        except e.NoSuchElementException:
            self.log.error("Element not found with id :: " + id)
            traceback.print_stack()
        return element

    def getElementListById(self, id):
        """
        Get element list by id

        Required Parameters:
            id: id of the element list to find

        Optional Parameters:
            None

        Returns:
            Element List Object
        """
        elements = None
        try:
            elements = self.driver.find_elements_by_css_selector("[id=" + id + "]")
            self.log.info("Elements found with id :: " + id)
        except:
            self.log.error("Elements not found with id :: " + id)
            traceback.print_stack()
        return elements

    def getElementByXpath(self, xpath):
        """
        Get element by xpath

        Required Parameters:
            xpath: xpath of the element to find

        Optional Parameters:
            None

        Returns:
            Element Object
        """
        element = None
        try:
            element = self.driver.find_element_by_xpath(xpath)
            self.log.info("Element found with xpath :: " + xpath)
        except:
            self.log.error("Element found with not :: " + xpath)
            traceback.print_stack()
        return element

    def getElementListByXpath(self, xpath):
        """
        Get element list by xpath

        Required Parameters:
            xpath: xpath of the element list to find

        Optional Parameters:
            None

        Returns:
            Element List Object
        """
        elements = None
        try:
            elements = self.driver.find_elements_by_xpath(xpath)
            self.log.info("Elements found with xpath :: " + xpath)
        except:
            self.log.error("Elements not found with xpath :: " + xpath)
            traceback.print_stack()
        return elements

    def getElementByCss(self, css):
        """
        Get element by css

        Required Parameters:
            css: css of the element to find

        Optional Parameters:
            None

        Returns:
            Element Object
        """
        element = None
        try:
            element = self.driver.find_element_by_css_selector(css)
            self.log.info("Element found with css :: " + css)
        except:
            self.log.error("Element not found with css :: " + css)
            traceback.print_stack()
        return element

    def getElementListByCss(self, css):
        """
        Get element list by css

        Required Parameters:
            css: css of the element list to find

        Optional Parameters:
            None

        Returns:
            Element List Object
        """
        elements = None
        try:
            elements = self.driver.find_elements_by_css_selector(css)
            self.log.info("Elements found with css :: " + css)
        except:
            self.log.error("Elements not found with css :: " + css)
            traceback.print_stack()
        return elements

    def getElementByTagName(self, tagName, parentId=None):
        """
        Get element by tag name

        Required Parameters:
            tagName: tagName of the element to find

        Optional Parameters:
            None

        Returns:
            Element Object
        """
        element = None
        try:
            if parentId is not None:
                element = self.getElementById(parentId).find_element_by_tag_name(tagName)
                self.log.info("Element found with parent id :: '" + parentId + "' and tag name :: " + tagName)
            else:
                element = self.driver.find_element_by_tag_name(tagName)
                self.log.info("Element found with tag name :: " + tagName)
        except:
            self.log.error("Element not found with parent id :: '" + parentId + "' and tag name :: " + tagName)
            traceback.print_stack()
        return element

    def getElementListByTagName(self, tagName, parentId=None):
        """
        Get element list by tag name

        Required Parameters:
            tagName: tagName of the element list to find

        Optional Parameters:
            None

        Returns:
            Element List Object
        """
        elementsList = []
        try:
            if parentId is not None:
                elementsList = self.getElementById(parentId).find_elements_by_tag_name(tagName)
                self.log.info("Elements found with parent id :: '" + parentId + "' and tag name :: " + tagName)
            else:
                elementsList = self.driver.find_elements_by_tag_name(tagName)
                self.log.info("Elements found with tag name :: " + tagName)
        except:
            self.log.error("Elements not found with parent id :: '" + parentId + "' and tag name :: " + tagName)
            traceback.print_stack()
        return elementsList

    def getElementByTagAndText(self, tagName, text, parentId=None):
        """
        Get element by tag name and text

        Required Parameters:
            tagName: tagName of the element to find
            text: Text on the element

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element Object
        """
        elementsList = self.getElementListByTagName(tagName, parentId)
        self.log.info("Element found with tag name :: " + tagName + " and text :: " + text)
        element = None
        try:
            for e in elementsList:
                tempText = e.text
                self.log.info("Element text is :: " + tempText)
                if self.util.verifyTextMatch(tempText, text):
                    element = e
                    self.log.info("Element added to the list :: " + tempText)
        except:
            self.log.error("Element not found with tag name :: " + tagName + " and text :: " + text)
            traceback.print_stack()
        return element

    def getElementListByTagAndText(self, tagName, text, parentId=None):
        """
        Get element list by tag name and text

        Required Parameters:
            tagName: tagName of the element to find
            text: Text on the element

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element Object
        """
        elementsList = self.getElementListByTagName(tagName, parentId)
        self.log.info("Elements found with tag name :: " + tagName + " and text :: " + text)
        webElementsList = []
        try:
            for e in elementsList:
                tempText = e.text
                self.log.info("Element text is :: " + tempText)
                if self.util.verifyTextMatch(tempText, text):
                    webElementsList.append(e)
                    self.log.info("Element added to the list :: " + tempText)
        except:
            self.log.error("Elements not found with tag name :: " + tagName + " and text :: " + text)
            traceback.print_stack()

        return webElementsList

    def getSubElementListByTagName(self, tagName, parentElement):
        """
        Get sub element list by tag name

        Required Parameters:
            tagName: tagName of the element to find
            parentElement: Parent element under which sub elements exist

        Optional Parameters:
            None

        Returns:
            Element List Object
        """
        elementsList = []
        try:
            if parentElement is not None:
                elementsList = parentElement.find_elements_by_tag_name(tagName)
                self.log.info("Elements found under parent :: '" +
                              parentElement.text + "' and tag name :: " + tagName)
            else:
                self.log.error("Parent element reference to none")
        except:
            self.log.error("Element not found under parent :: '" +
                          parentElement.text + "' and tag name :: " + tagName)
            traceback.print_stack()
        return elementsList

    def getElementByLink(self, linkText):
        """
        Get element by link text

        Required Parameters:
            linkText: Link text on the element to find

        Optional Parameters:
            None

        Returns:
            Element Object
        """
        element = None
        try:
            element = self.driver.find_element_by_link_text(linkText)
            self.log.info("Element found with link text :: " + linkText)
        except:
            self.log.error("Element not found with link text :: " + linkText)
            traceback.print_stack()
        return element

    def getElementByPartialLink(self, partialText, parentId=None):
        """
        Get element by partial link text

        Required Parameters:
            partialText: Partial link text on the element to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element Object
        """
        element = None
        try:
            if parentId is not None:
                element = self.getElementById(parentId).find_element_by_partial_link_text(partialText)
                self.log.info("Element found with parent id :: " + parentId + " and partial link :: " + partialText)
            else:
                element = self.driver.find_element_by_partial_link_text(partialText)
                self.log.info("Element found with partial link :: " + partialText)
        except:
            self.log.error("Element not found with parent id :: " + parentId + " and partial link :: " + partialText)
            traceback.print_stack()
        return element

    def getElementByClassName(self, className, parentId=None):
        """
        Get element by class name

        Required Parameters:
            className: Class name of the element to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element Object
        """
        element = None
        try:
            if parentId is not None:
                element = self.getElementById(parentId).find_element_by_class_name(className)
                self.log.info("Element found with parent id :: " + parentId + " and class name :: " + className)
            else:
                element = self.driver.find_element_by_class_name(className)
                self.log.info("Element found with class name :: " + className)
        except:
            self.log.error("Element not found with parent id :: " + parentId + " and class name :: " + className)
            traceback.print_stack()
        return element

    def getElementListByClassName(self, className, parentId=None):
        """
        Get element list by class name

        Required Parameters:
            className: Class name of the element list to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element List Object
        """
        elementsList = []
        try:
            if parentId is not None:
                elementsList = self.getElementById(parentId).find_elements_by_class_name(className)
                self.log.info("Elements found with parent id :: " + parentId + " and class name :: " + className)
            else:
                elementsList = self.driver.find_element_by_class_name(className)
                self.log.info("Elements found with class name :: " + className)
        except:
            self.log.error("Elements not found with parent id :: " + parentId + " and class name :: " + className)
            traceback.print_stack()
        return elementsList

    def getElementByClassAndTagName(self, className, tagName, parentId=""):
        """
        Get element by class name and tag name

        Required Parameters:
            className: Class name of the element to find
            tagName: Tag name of the element to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element List Object
        """
        parentElement = self.getElementByClassName(className, parentId)
        return parentElement.find_element_by_tag_name(tagName)

    def getElementsTextListByClassName(self, className, parentId=None):
        """
        Get list of text on elements by class name

        Required Parameters:
            className: Class name of the elements to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            List object of text on elements
        """
        elementTextList = self.getElementListByClassName(className, parentId)
        for e in elementTextList:
            self.log.info("Element text is :: " + e.text)
            elementTextList.append(e.text)
        return elementTextList

    def getElementsTextListByTagName(self, tagName, parentId=None):
        """
        Get list of text on elements by tag name

        Required Parameters:
            tagName: Tag name of the elements to find

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            List object of text on elements
        """
        elementTextList = self.getElementListByTagName(tagName, parentId)
        for e in elementTextList:
            self.log.info("Element text is :: " + e.text)
            elementTextList.append(e.text)
        return elementTextList

    def getItemIndexByClassNameAndText(self, className, itemText, match=True, parentId=None):
        """
        Get index of element by class name and text
        If multiple elements exist with the same class name
        This method can be used to find the index of an element

        Required Parameters:
            className: Class name of the element to find
            itemText: Text on element

        Optional Parameters:
            parentId: id of the parent element, if available
            match: Provide False if you want to check for text contains instead of exact match

        Returns:
            List object of text on elements
        """
        index = -1
        elementsList = self.getElementListByClassName(className, parentId)
        length = len(elementsList)
        for i in range(length):
            text = elementsList[i].text.strip()
            self.log.info("Element text is :: " + text)
            if match:
                if self.util.verifyTextMatch(text, itemText):
                    index = i
                    break
            else:
                if self.util.verifyTextContains(text, itemText):
                    index = i
                    break
        self.log.info("The item " + itemText + " is at location " + index)
        return index

    def getItemIndexByTagName(self, tagName, itemText, match=True, parentId=None):
        """
        Get index of element by tag name and text
        If multiple elements exist with the same tag name
        This method can be used to find the index of an element

        Required Parameters:
            tagName: Tag name of the elements to find
            itemText: Text on element

        Optional Parameters:
            parentId: id of the parent element, if available
            match: Provide False if you want to check for text contains instead of exact match

        Returns:
            List object of text on elements
        """
        index = -1
        elementsList = self.getElementListByTagName(tagName, parentId)
        length = len(elementsList)
        for i in range(length):
            text = elementsList[i].text.strip()
            self.log.info("Element text is :: " + text)
            if match:
                if self.util.verifyTextMatch(text, itemText):
                    index = i
                    break
            else:
                if self.util.verifyTextContains(text, itemText):
                    index = i
                    break
        self.log.info("The item " + itemText + " is at location :: " + index)
        return index

    def getElementButton(self, buttonText, parentId=None):
        """
        Get a button by text

        Required Parameters:
            buttonText: Text on button

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            Element Button
        """
        return self.getElementByTagAndText("button", buttonText, parentId)

    def isButtonDisabled(self, buttonText, info, parentId=None):
        """
        Check if button is disabled

        Required Parameters:
            buttonText: Text on button
            info: Information about the element, usually text on the element

        Optional Parameters:
            parentId: id of the parent element, if available

        Returns:
            List object of text on elements
        """
        return self.isEnabled(self.getElementButton(buttonText, parentId), info)

    def getElementAttributeValue(self, element, attribute):
        """
        Get value of the attribute of element

        Required Parameters:
            element: Element with which attribute is associated
            attribute: attribute whose value to find

        Optional Parameters:
            None

        Returns:
            Value of the attribute
        """
        return element.get_attribute(attribute)

    def verifyElementTextContains(self, locator, expectedText):
        """
        Check if the element contains the text

        Required Parameters:
            locator: Locator of the element
            expectedText: Text needs to be checked in element

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        element = self.getElement(locator)
        actualText = element.text
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION CONTAINS !!!")
            return False

    def verifyElementTextMatch(self, locator, expectedText):
        """
        Check if the element matches the text

        Required Parameters:
            locator: Locator of the element
            expectedText: Text needs to be checked in element

        Optional Parameters:
            None

        Returns:
            Boolean
        """
        element = self.getElement(locator)
        actualText = element.text
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False