from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class Config(unittest.TestCase):
    hub = 'http://hub:4444/wd/hub'

    def setUp(self):
        self.webdriver = webdriver.Remote(self.hub, DesiredCapabilities.CHROME)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(10)

    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()
