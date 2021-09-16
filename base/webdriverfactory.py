"""
@package base

WebDriver package class implementation
It creates a webdriver instance based on the browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        :param browser:
        :return none
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration
        :return: WebDriver instance
        """
        baseURL = 'http://eaapp.somee.com/'
        if self.browser == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument('--remote-debugging-port=9222')
            driver = webdriver.Firefox(executable_path=GeckoDriverManager.install(), options=firefox_options)
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--remote-debugging-port=9222')
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver
