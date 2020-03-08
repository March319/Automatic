import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("stock_name", [("JD")])
    def test_add_and_back(self, stock_name):
        self.main.goto_stocks().search_stocks(stock_name).add_stocks().close_to_back()
