from traceback import print_stack

from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class
        :param driver:
        :return none
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page title

        :param titleToVerify:
        :return: True or False
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextXontains(actualTitle, titleToVerify)
        except:
            self.log.error('Failed to get page title')
            print_stack()
            return False
