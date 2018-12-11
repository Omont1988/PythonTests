from tests.pages.index.IndexLocators import IndexLocators as locators
from tests.pages.BasePage import InvalidPageException
from tests.pages.BasePage import BasePage

import tests.helpers.Helper as helper


class IndexPage(BasePage):
    _page_title = 'DOU'

    def _validate_page(self, driver):
        try:
            assert self._page_title in driver.title
        except:
            raise InvalidPageException('Index page not loaded')

    def fill_in_search_field(self, value):
        helper.fill_field(self.driver, locators.search_field, value).submit()

    def click_login_button(self):
        helper.click_element(self.driver, locators.login_button)

    def click_gmail_signin(self):
        helper.click_element(self.driver,locators.google_login_button)