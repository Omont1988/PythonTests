from selenium.webdriver.common.by import By


class IndexLocators(object):
    search_field = (By.ID, 'txtGlobalSearch')
    login_button = (By.ID, 'login-link')
    google_login_button = (By.ID, 'btnGoogle')
