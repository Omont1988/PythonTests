from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class Config(unittest.TestCase):

    hub = 'http://hub:4444/wd/hub'
    index_url = 'https://dou.ua/'

    def setUp(self):
        self.webdriver = webdriver.Remote(self.hub, DesiredCapabilities.CHROME)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(10)

        self.webdriver.get(self.index_url)

    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()
