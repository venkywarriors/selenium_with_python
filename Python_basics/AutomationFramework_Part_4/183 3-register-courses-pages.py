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
        print()

    def selectCourseToEnroll(self, fullCourseName):
        print()

    def clickOnEnrollButton(self):
        print()

    def enterCardNum(self, num):
        print()

    def enterCardExp(self, exp):
        print()

    def enterCardCVV(self, cvv):
        print()

    def clickEnrollSubmitButton(self):
        print()

    def enterCreditCardInformation(self, num, exp, cvv):
        print()

    def enrollCourse(self, num="", exp="", cvv=""):
        print()

    def verifyEnrollFailed(self):
        print()