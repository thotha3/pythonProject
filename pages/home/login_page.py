import time

from selenium.webdriver.common.by import By
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = 'loginLink'
    _username = 'UserName'
    _password = 'Password'
    _login_button = '//*[@id="loginForm"]/form/div[4]/div/input'
    _invalid_username = '//*[@id="loginForm"]/form/div[1]/div/span/span[contains(text(),"The UserName field is ' \
                        'required.")] '
    _invalid_password = '//*[@id="loginForm"]/form/div[2]/div/span/span[contains(text(),"The Password field is ' \
                        'required.")] '
    _logout_link = '//*[@id="logoutForm"]/ul/li[2]/a'

    def clickLoginLink(self):
        self.elementClick(self._login_link, By.ID)

    def enterUsername(self, username):
        self.sendKeys(username, self._username, By.NAME)

    def enterUserPassword(self, password):
        self.sendKeys(password, self._password, By.NAME)

    def clickLoginButton(self):
        self.elementClick(self._login_button, By.XPATH)

    def validateSuccessfulLogin(self):
        result = self.isElementPresent(self._logout_link, By.XPATH)

        return result

    def validateInvalidUsername(self):
        result = self.isElementPresent(self._invalid_username, By.XPATH)

        return result

    def validateInvalidPassword(self):
        result = self.isElementPresent(self._invalid_password, By.XPATH)

        return result

    def validateLoginTitle(self):
        return self.verifyPageTitle('xyz')

    def clickLogoutLink(self):
        self.elementClick(self._logout_link, By.LINK_TEXT)

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterUsername(username)
        self.enterUserPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.clickLogoutLink()
