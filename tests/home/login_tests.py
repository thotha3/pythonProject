import unittest
from pages.home.login_page import LoginPage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl
from utilities.teststatus import TestStatus
import logging
import pytest


class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginPage = LoginPage(self.driver)
        self.navigationPage = NavigationPage(self.driver)
        self.testStatus = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        #self.loginPage.login('admin', 'password')
        # result1 = self.loginPage.validateLoginTitle()
        # self.testStatus.mark(result1, 'Title is incorrect')
        result = self.loginPage.validateSuccessfulLogin()
        self.testStatus.markFinal('test_validLogin', result, 'Login successful')
        #self.loginPage.logout()

    @pytest.mark.run(order=2)
    def test_navigation(self):
        self.navigationPage.navigateToHomePage()
        self.navigationPage.navigateToAboutPage()
        self.navigationPage.navigateToEmployeeListPage()
        self.navigationPage.navigateToManageUsersPage()
        self.navigationPage.navigateToUserProfilePage()
        self.loginPage.logout()
    """
    @pytest.mark.run(order=2)
        def test_invalidPassword(self):
        self.loginPage.login(username='admin')
        result = self.loginPage.validateInvalidPassword()
        self.testStatus.markFinal('test_invalidPassword', result, 'Password is invalid')
        self.loginPage.logout()

        @pytest.mark.run(order=1)
        def test_invalidUsername(self):
        self.loginPage.login(password='password')
        result = self.loginPage.validateInvalidUsername()
        self.testStatus.markFinal('test_invalidUsername', result, 'Username is invalid')
    """
