import time

from locators.basepage import BasePageLocators
from driverutils import DriverUtils
from configutils import ConfigUtils


class BasePage:

    def __init__(self):
        self.basepagelocators = BasePageLocators
        self.driver = DriverUtils()
        self.config = ConfigUtils()

    def navigate_to_url(self):
        """
        Navigating to url
        :return: None
        """
        self.driver.navigate_to_url()

