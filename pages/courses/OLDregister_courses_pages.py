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
    _search_course_icon ="//i[@class='fa fa-search']"
    _search_box = "//input[@name='course']"  # promenuo sam u xpath
    _course_2 = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _course = "//h4[contains(.,'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "//button[contains(.,'Enroll in Course')]"
    _cc_num = "//input[@name='cardnumber']"
    _cc_exp = "//input[contains(@name,'exp-date')]"
    _cc_cvv = "//input[contains(@name,'cvc')]"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name,locator=self._search_box, locatorType='xpath') # dodato jer moj nije ID
        self.elementClick(locator=self._search_course_icon, locatorType='xpath')

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType= 'xpath')

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType='xpath')

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num, locatorType='xpath')

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp, locatorType='xpath')

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType='xpath')

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType='xpath')

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction='down')
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result



