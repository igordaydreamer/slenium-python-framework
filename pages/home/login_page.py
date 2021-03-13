import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[contains(.,'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='zl-navbar-rhs-img ']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[@class='dynamic-text help-block']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToSettings()
        self.elementClick(locator="//a[@href='/logout']", locatorType='xpath')
