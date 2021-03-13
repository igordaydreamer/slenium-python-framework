import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "ALL COURSES"
    _all_courses = "My Courses"
    _practise = "Practise"
    _user_settings_icon = "//img[@class='zl-navbar-rhs-img ']"


    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType='link')

    def navigateToPractise(self):
        self.elementClick(locator=self._practise, locatorType='link')

    def navigateToSettings(self):
        self.elementClick(self._user_settings_icon, locatorType='xpath')

