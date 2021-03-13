import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "//input[@name='course']"
    _search_course_icon = "//i[@class='fa fa-search']"
    _course = "//h4[contains(.,'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "//button[contains(.,'Enroll in Course')]"
    _cc_num = "//input[@name='cardnumber']"
    _cc_exp = "//input[contains(@name,'exp-date')]"
    _cc_cvv = "//input[contains(@name,'cvc')]"
    _zip = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"


    # /parent::div

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_course_icon, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    # def enterZip(self, zip):
    #     # self.switchToFrame(name="__privateStripeFrame11")
    #     self.SwitchFrameByIndex(self._zip, locatorType="name")            # zip is del due to site changes
    #     self.sendKeys(zip, locator=self._zip, locatorType="name")
    #     self.switchToDefaultContent()

    # def clickAgreeToTermsCheckbox(self):
    #     self.elementClick(locator=self._agree_to_terms_checkbox)          # checkbox is del due to site changes

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
       # self.enterZip(zip)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        #self.clickAgreeToTermsCheckbox()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result