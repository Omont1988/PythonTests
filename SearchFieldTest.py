from tests.config.config import Config
from tests.pages.index.IndexPage import IndexPage
from tests.pages.search.SearchPage import SearchPage

import unittest
import time


class SearchFieldTest(Config):
    word = 'python automation'
    search_url = 'python+automation'

    def test_search(self):
        page = IndexPage(self.webdriver)
        page.fill_in_search_field(self.word)
        search_page = SearchPage(self.webdriver)
        url = self.webdriver.current_url
        self.assertIn(self.search_url, url)
        res = search_page.get_all_links_text()
        for title in res.keys():
            self.assertIn('python', title.lower())

    def test_login(self):
        index_page = IndexPage(self.webdriver)
        index_page.click_login_button()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
