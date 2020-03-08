from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Stocks(BasePage):
    _search_locator = (MobileBy.ID, "action_search")
    _search_input_locator = (MobileBy.ID, "search_input_text")
    _add_stocks_locator = (MobileBy.ID, "follow_btn")
    _close_locator = (MobileBy.ID, "action_close")

    def search_stocks(self, stock_name):
        _result_locator = (By.XPATH, "//*[contains(@resource-id, 'listview')]//*[@text='%s']" % stock_name)
        print(self._search_locator)
        self.find(self._search_locator).click()
        self.find(self._search_input_locator).send_keys(stock_name)
        self.find(_result_locator).click()
        return self

    def add_stocks(self):
        self.find(self._add_stocks_locator).click()
        return self

    def close_to_back(self):
        self.find(self._close_locator).click()
