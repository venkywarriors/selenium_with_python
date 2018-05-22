"""
@package utilities

Util class implementation

All most commonly used utilities should be implemented in this class

This class is initialized in basepage class and guibasetestcase class
There is no need to create an object instance in page classes and test case classes

@author Anil Tomar <anil.tomar@nimblestorage.com>
@version 1.0
@copyright Nimble Storage, Inc

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
from base.configreader import ConfigReader
from utilities.driver_session import DriverSession as DS
import utilities.custom_logger as cl


class Util(object):
    def __init__(self):
        """
        Inits Util class

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        self.log = cl.customLogger()

    def screenShot(self, issueType):
        """
        Takes screenshot of the current open web page

        Required Parameters:
            issueType: FAIL/ERROR/WARNING

        Optional Parameters:
            None

        Returns:
            None
        """
        fileName = str(round(time.time() * 1000)) + "." + issueType + ".png"
        screenshotDirectory = self.readConfig(option="screenshot_directory",
                                              section="Platform", fileName="testenvironment.ini")
        # destinationFile = screenshotDirectory + "/" + fileName
        scriptDirectory = os.path.dirname(__file__)
        relativePath = screenshotDirectory + fileName
        destinationFile = os.path.join(scriptDirectory, relativePath)
        destinationDirectory = os.path.join(scriptDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            DS.getDriver().save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            self.log.info("Not a directory issue")
            traceback.print_stack()
        except FileNotFoundError:
            self.log.info("File not found issue")
            traceback.print_stack()

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time

        Required Parameters:
            sec: Number of seconds to wait

        Optional Parameters:
            info: Info message to be logged

        Returns:
            None
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        Required Parameters:
            length: Length of string, number of characters string should have

        Optional Parameters:
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types

        Returns:
            None
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name

        Required Parameters:
            None

        Optional Parameters:
            charCount: Number of characters name should have. Default is 10.

        Returns:
            None
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getValidEmail(self, firstCount=10, secondCount=10):
        """
        Get a valid email id

        Required Parameters:
            None

        Optional Parameters:
            firstCount: Number of characters before @ symbol. Default is 10.
            secondCount: Number of characters after @ symbol. Default is 10.

        Returns:
            None
        """
        return self.getUniqueName(firstCount) + "@" + self.getUniqueName(secondCount) + ".com"

    def getValidEmailList(self, listSize=5, firstCount=10, secondCount=10):
        """
        Get a list of valid email ids

        Required Parameters:
            None

        Optional Parameters:
            listSize: Number of email ids. Default is 5 email in a list
            firstCount: Number of characters before @ symbol. Default is 10.
            secondCount: Number of characters after @ symbol. Default is 10.

        Returns:
            None
        """
        emailList = []
        for i in range(0, listSize):
            emailList.append(self.getUniqueName(firstCount) + "@" + self.getUniqueName(secondCount) + ".com")
        return emailList

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Required Parameters:
            None

        Optional Parameters:
            listSize: Number of email ids. Default is 5 email in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list

        Returns:
            None
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def getInvalidEmail(self, firstCount=10, secondCount=10):
        """
        Get an invalid email id

        Required Parameters:
            None

        Optional Parameters:
            firstCount: Number of characters before @ symbol. Default is 10.
            secondCount: Number of characters after @ symbol. Default is 10.

        Returns:
            None
        """
        incorrectFormat = "--.."
        return self.getUniqueName(firstCount) + incorrectFormat + "__++@" + self.getUniqueName(secondCount) + \
               incorrectFormat + ".com" + incorrectFormat + "!@#$%^&*()_+-="

    def getValidServerName(self, firstCount=10, secondCount=10):
        """
        Get a valid server name
        If maximum allowed length is 255
        firstCount + secondCount can't be greater than 250

        Required Parameters:
            None

        Optional Parameters:
            firstCount: Number of characters before "." symbol. Default is 10.
            secondCount: Number of characters after "." symbol. Default is 10.

        Returns:
            None
        """
        return self.getUniqueName(firstCount) + "-" + self.getUniqueName(secondCount) + ".com"

    def getInvalidServerName(self, firstCount=10, secondCount=10):
        """
        Get an invalid email id

        Required Parameters:
            None

        Optional Parameters:
            firstCount: Number of characters before "." symbol. Default is 10.
            secondCount: Number of characters after "." symbol. Default is 10.

        Returns:
            None
        """
        incorrectFormat = "!@#$%^&*()_+-="
        return self.getUniqueName(firstCount) + incorrectFormat + "." + self.getUniqueName(secondCount) + \
               incorrectFormat + ".com"

    def getValidPort(self, count=4):
        """
        Get a valid port number

        Required Parameters:
            None

        Optional Parameters:
            count: Number of digits in a port. Default is 4.

        Returns:
            None
        """
        maxValidPort = "65535"
        port = self.getAlphaNumeric(count, 'digits')
        if int(port) > 65535:
            return maxValidPort
        return port

    def getInvalidPort(self, count=10):
        """
        Get an invalid port number

        Required Parameters:
            None

        Optional Parameters:
            count: Number of digits in a port. Default is 10.

        Returns:
            None
        """
        return "-" + str(self.getAlphaNumeric(count, 'digits'))

    def getDefaultUsername(self):
        """
        Get default username

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        return "admin"

    def getDefaultPassword(self):
        """
        Get default password

        Required Parameters:
            None

        Optional Parameters:
           None

        Returns:
            None
        """
        return "admin"

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Required Parameters:
            expectedList: Expected List
            actualList: Actual List

        Optional Parameters:
            None

        Returns:
            None
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Required Parameters:
            expectedList: Expected List
            actualList: Actual List

        Optional Parameters:
            None

        Returns:
            None
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Required Parameters:
            expectedList: Expected Text
            actualList: Actual Text

        Optional Parameters:
            None

        Returns:
            None
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Required Parameters:
            expectedList: Expected Text
            actualList: Actual Text

        Optional Parameters:
            None

        Returns:
            None
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def readConfig(self, option, section="FieldErrors", fileName="messages.ini"):
        """
        Read configuration file

        Required Parameters:
            option: Option to read from the file
            section: Section in which option exist
            fileName: Configuration file name, default is messages.ini

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        self.cfg = ConfigReader(fileName=fileName)
        self.cfg.configRead()
        return self.cfg.getConfiguration(section, option)

    def getArrayName(self):
        """
        Get Array Name

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            Array Name String
        """
        return self.readConfig(option="array_name", section="Array",
                               fileName="testenvironment.ini")

    def readErrorMessage(self, option):
        """
        Read error messages from configuration file

        Required Parameters:
            option: Option to read from the file

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        return self.readConfig(option=option, section="FieldErrors",
                               fileName="messages.ini")

    def readFlashMessage(self, option):
        """
        Read flash message from configuration file

        Required Parameters:
            option: Option to read from the file

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        return self.readConfig(option=option, section="FlashMessages",
                               fileName="messages.ini")

    def readSuccessMessage(self, option):
        """
        Read success message from configuration file

        Required Parameters:
            option: Option to read from the file

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        return self.readConfig(option=option, section="SuccessMessages",
                               fileName="messages.ini")

    def readWarningMessage(self, option):
        """
        Read Warning message from configuration file

        Required Parameters:
            option: Option to read from the file

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        return self.readConfig(option=option, section="WarningMessages",
                               fileName="messages.ini")

    def readPageTitle(self, option):
        """
        Read page title from configuration file

        Required Parameters:
            option: Option to read from the file

        Optional Parameters:
            None

        Returns:
            Value associated with the option

        """
        return self.readConfig(option=option, section="PageTitles",
                               fileName="messages.ini")
