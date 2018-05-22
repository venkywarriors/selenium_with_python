import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num)

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    def clickEnrollSubmitButton(self):
        self.sendKeys(self._submit_enroll, locator="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
