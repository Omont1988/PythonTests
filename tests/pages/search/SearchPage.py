from tests.pages.BasePage import BasePage
from tests.pages.BasePage import InvalidPageException
from tests.pages.search.SearchLocators import SearchLocators

import tests.helpers.Helper as Helper



class SearchPage(BasePage):
    url = 'search/?q'

    def _validate_page(self, driver):
        try:
            assert self.url in driver.current_url
        except:
            raise InvalidPageException('Search page not loaded')


    def get_all_links_text(self):
        result = {}
        elements = Helper.find_elements(self.driver, SearchLocators.one_item)
        for element in elements:
            if element.text:
                link = element.find_element_by_xpath('.//*').get_attribute('href')
                result[element.text] = link
        return result
