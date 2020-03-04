from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_add_and_back(self):
        self.main.goto_stocks().search_stocks().add_stocks().close_to_back()
