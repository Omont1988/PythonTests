from selenium.webdriver.common.by import By
from selenium import webdriver


class IndexLocators(object):
    search_field = (By.ID, 'txtGlobalSearch')
    login_button = (By.ID, 'login-link')