import time

from selenium.webdriver.common.by import By
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _home_link = '/html/body/div[1]/div/div[2]/ul/li[1]/a'
    _about_link = '/html/body/div[1]/div/div[2]/ul/li[2]/a'
    _employee_list_link = '/html/body/div[1]/div/div[2]/ul/li[3]/a'
    _employee_details_link = '/html/body/div[1]/div/div[2]/ul/li[4]/a'
    _manage_users_link = '/html/body/div[1]/div/div[2]/ul/li[5]/a'
    _user_greeting_link = '//*[@id="logoutForm"]/ul/li[1]/a'

    def navigateToHomePage(self):
        self.elementClick(self._home_link, By.XPATH)

    def navigateToAboutPage(self):
        self.elementClick(self._about_link, By.XPATH)

    def navigateToEmployeeListPage(self):
        self.elementClick(self._employee_list_link, By.XPATH)

    def navigateToEmployeeDetailsPage(self):
        self.elementClick(self._employee_details_link, By.XPATH)

    def navigateToManageUsersPage(self):
        self.elementClick(self._manage_users_link, By.XPATH)

    def navigateToUserProfilePage(self):
        self.elementClick(self._user_greeting_link, By.XPATH)
