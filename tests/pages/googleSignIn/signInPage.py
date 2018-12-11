from tests.pages.googleSignIn.signInLocators import SignInLocators
from tests.pages.BasePage import BasePage
from tests.pages.BasePage import InvalidPageException

from time import sleep

import tests.helpers.Helper as helper


class SignInPage(BasePage):
    title = 'Sign in'

    def validate_page(self, driver):
        try:
            assert self.title in driver.title
        except:
            raise InvalidPageException('Google Sign in page not loaded')

    def read_credentials(self):
        with open('/tests/credentials.txt') as f:
            creds = [line.rstrip() for line in f]
        return creds

    def login(self):
        values = self.read_credentials()
        fields = [SignInLocators.mail_field, SignInLocators.password_field]
        next_buttons = [SignInLocators.next_button_login, SignInLocators.next_button_password]
        for idx, field in enumerate(fields):
            print(values[idx])
            helper.fill_field(self.driver, field, values[idx])
            sleep(3)
            helper.click_element(self.driver, next_buttons[idx])
