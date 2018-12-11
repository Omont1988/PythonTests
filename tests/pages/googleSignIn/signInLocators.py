from selenium.webdriver.common.by import By


class SignInLocators(object):
    mail_field = (By.ID, 'identifierId')
    password_field = (By.NAME, 'password')
    next_button_password = (By.ID, 'passwordNext')
    next_button_login = (By.ID, 'identifierNext')

