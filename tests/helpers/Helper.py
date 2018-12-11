from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def find_element(driver, locator):
    delay = 3  # seconds
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_element_located(locator))

    except TimeoutException:
        print ("element {} was not found".format(locator))

def find_elements(driver, locator):
    delay = 3  # seconds
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located(locator))

    except TimeoutException:
        print ("element {} was not found".format(locator))

def click_element(driver, locator):
    el = find_element(driver, locator)
    el.click()


def fill_field(driver, locator, text):
    el = find_element(driver, locator)
    el.send_keys(text)
    return el


def get_text(driver, locator):
    el = find_element(driver, locator)
    return el.text
